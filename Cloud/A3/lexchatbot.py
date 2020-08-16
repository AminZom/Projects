import math
import dateutil.parser
import datetime
import time
import os
import logging
import boto3
import csv
import io

s3 = boto3.resource("s3")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_slots(intent_request):
    return intent_request['currentIntent']['slots']

def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }

def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response

def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }

def parse_int(n):
    try:
        return int(n)
    except ValueError:
        return float('nan')

def build_validation_result(is_valid, violated_slot, message_content):
    if message_content is None:
        return {
            "isValid": is_valid,
            "violatedSlot": violated_slot,
        }

    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }


def isvalid_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except ValueError:
        return False


def validate_order_services(service_type, first_name, last_name, street_address, city, email, phone_number, date, time):
    service_types = ['taxi', 'food delivery', 'home care', 'cleaning']
    if service_type is not None and service_type.lower() not in service_types:
        return build_validation_result(False,
                                       'ServiceType',
                                       'We do not offer that service, would you like a different type of service?  ')

    if date is not None:
        if not isvalid_date(date):
            return build_validation_result(False, 'Date', 'I did not understand that, what date would you like to receive this service?')
        elif datetime.datetime.strptime(date, '%Y-%m-%d').date() <= datetime.date.today():
            return build_validation_result(False, 'Date', 'You can receive the service from tomorrow onwards.  What day would you like to receive it?')

    if time is not None:
        if len(time) != 5:
            # Not a valid time; use a prompt defined on the build-time model.
            return build_validation_result(False, 'Time', None)

        hour, minute = time.split(':')
        hour = parse_int(hour)
        minute = parse_int(minute)
        if math.isnan(hour) or math.isnan(minute):
            # Not a valid time; use a prompt defined on the build-time model.
            return build_validation_result(False, 'Time', None)

    return build_validation_result(True, None, None)

def order_services(intent_request):

    service_type = get_slots(intent_request)["ServiceType"]
    first_name = get_slots(intent_request)["FirstName"]
    last_name = get_slots(intent_request)["LastName"]
    street_address = get_slots(intent_request)["StreetAddress"]
    city = get_slots(intent_request)["City"]
    email = get_slots(intent_request)["EmailAddress"]
    phone_number = get_slots(intent_request)["PhoneNumber"]
    date = get_slots(intent_request)["Date"]
    time = get_slots(intent_request)["Time"]
    source = intent_request['invocationSource']

    if source == 'DialogCodeHook':
        slots = get_slots(intent_request)

        validation_result = validate_order_services(service_type, first_name, last_name, street_address, city, email, phone_number, date, time)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(intent_request['sessionAttributes'],
                               intent_request['currentIntent']['name'],
                               slots,
                               validation_result['violatedSlot'],
                               validation_result['message'])
                               
        content = 'First Name: ' + str(first_name) + '\n'
        content = content + 'Last Name: ' + str(last_name) + '\n'
        content = content + 'Street Address: ' + str(street_address) + '\n'
        content = content + 'City: ' + str(city) + '\n'
        content = content + 'Email: ' + str(email) + '\n'
        content = content + 'Phone Number: ' + str(phone_number) + '\n'
        content = content + 'Date: ' + str(date) + '\n'
        content = content + 'Time: ' + str(time) + '\n'
        content = content + 'Type of Service: ' + str(service_type)
        s3.Bucket('msheikht-service').put_object(Body=content, Key='serviceOrder.txt')

        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}

        return delegate(output_session_attributes, get_slots(intent_request))

    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Thanks, your order for {} has been placed and will be arriving by {} on {}'.format(service_type, time, date)})

def dispatch(intent_request):

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    if intent_name == 'OrderService':
        return order_services(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')

def lambda_handler(event, context):
    os.environ['TZ'] = 'Canada/Toronto'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)
