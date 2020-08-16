

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Calculator.h"
#include "TestCalculator.h"
#include <assert.h>

void driver(double expectedSum, double expectedDifference, double expectedProduct, double expectedQuotient, double a, double b)
{
	Calculator* calc = newCalculator();
	
	printf("\n\nDRIVER:\n*******\n");
	printf("a: %.2f\n", a);
	printf("b: %.2f\n\n", b);
	
	printf("Expected Sum: %.2f\n", expectedSum);
	printf("Expected Difference: %.2f\n", expectedDifference);
	printf("Expected Product: %.2f\n", expectedProduct);
	printf("Expected Quotient: %.2f\n\n", expectedQuotient);
	
	printf("Function being called: testAdd\n");
	int testAddReturn = testAdd(expectedSum, a, b, calc->add);
	if(testAddReturn == 0)
	{
		goto successAdd;
		successAdd: printf("Expected Value: %.2f\nResult Value: %.2f\ntestAdd function \033[32;1mSUCCESSFUL\033[0m.\n\n", expectedSum, calc->add(a, b));
	}
	else
	{
		goto failAdd;
		failAdd: printf("Expected Value: %.2f\nResult Value: %.2f\ntestAdd function \033[31;1mFAILED\033[0m.\n\n", expectedSum, calc->add(a, b));
	}
	
	printf("Function being called: testSubtract\n");
	int testSubtractReturn = testSubtract(expectedDifference, a, b, calc->subtract);
	if(testSubtractReturn == 0)
	{
		goto successSubtract;
		successSubtract: printf("Expected Value: %.2f\nResult Value: %.2f\ntestSubtract function \033[32;1mSUCCESSFUL\033[0m.\n\n", expectedDifference, calc->subtract(a, b));
	}
	else
	{
		goto failSubtract;
		failSubtract: printf("Expected Value: %.2f\nResult Value: %.2f\ntestSubtract function \033[31;1mFAILED\033[0m.\n\n", expectedDifference, calc->subtract(a, b));
	}
	
	printf("Function being called: testMultiply\n");
	int testMultiplyReturn = testMultiply(expectedProduct, a, b, calc->multiply);
	if(testMultiplyReturn == 0)
	{
		goto successMultiply;
		successMultiply: printf("Expected Value: %.2f\nResult Value: %.2f\ntestMultiply function \033[32;1mSUCCESSFUL\033[0m.\n\n", expectedProduct, calc->multiply(a, b));
	}
	else
	{
		goto failMultiply;
		failMultiply: printf("Expected Value: %.2f\nResult Value: %.2f\ntestMultiply function \033[31;1mFAILED\033[0m.\n\n", expectedProduct, calc->multiply(a, b));
	}
	
	printf("Function being called: testDivide\n");
	int testDivideReturn = testDivide(expectedQuotient, a, b, calc->divide);
	if(testDivideReturn == 0)
	{
		goto successDivide;
		successDivide: printf("Expected Value: %.2f\nResult Value: %.2f\ntestDivide function \033[32;1mSUCCESSFUL\033[0m.\n\n", expectedQuotient, calc->divide(a, b));
	}
	else
	{
		goto failDivide;
		failDivide: printf("Expected Value: %.2f\nResult Value: %.2f\ntestDivide function \033[31;1mFAILED\033[0m.\n\n", expectedQuotient, calc->divide(a, b));
	}
	
    return;
}

int testSubtract(double expectedResult, double a, double b, double (*subtract)(double a, double b))
{
   if(subtract(a, b) == expectedResult)
		return 0;
	else
		return -1;
}

int testAdd(double expectedResult, double a, double b, double (*add)(double a, double b))
{
	if(add(a, b) == expectedResult)
		return 0;
	else
		return -1;
}

int testMultiply(double expectedResult, double a, double b, double (*multilpy)(double a, double b))
{
    if(multiply(a, b) == expectedResult)
		return 0;
	else
		return -1;
}

int testDivide(double expectedResult, double a, double b, double (*divide)(double a, double b))
{
    if(divide(a, b) == expectedResult)
		return 0;
	else
		return -1;
}
