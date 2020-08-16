**********************************************
Mohammadamin Sheikhtaheri		  Jan 27, 2020
0930853

CIS*4010 Assignment 1
README.txt
**********************************************

*********************************************
Installations Needed Before Execution of Code
*********************************************

Please make sure the following libraries and SDKs are installed prior to running the scripts:

	pip install boto3                      --> Used for creating python scripts for AWS

	pip install azure-storage-blob         --> Used for creating python scripts for Azure Storage

	pip install azure-cosmos               --> Used for creating python scripts for Azure CosmosDB

	pip install azure-cosmosdb-table       --> Used for creating python scripts for Azure CosmosDB Table Services

	pip install PTable                     --> Used for formatting and displaying queries

Note that this project was developed in Python 3.7, running this with older versions of Python may be unstable.

**********************
Task 1 Execution - AWS
**********************

Follow the steps below to run the AWS portion of task 1:

	1) Ensure that the files "config" and "credentials" are correctly set up using the user's access keys before execution
	2) Navigate to the AWS folder, where you will find the scripts for the AWS portion of both tasks 1 and 2
	3) To create buckets and upload files to the cloud, enter "python upload.py"
	4) To run the interactive display program, enter "python display.py" (make sure that you are in the /AWS folder in the terminal)
	5) Follow the instructions prompted by the program


************************
Task 1 Execution - Azure
************************

Follow the steps below to run the Azure portion of task 1:

	1) Ensure that the storage connection string of the user is configured by setting it as an environment variable, this can be done 
	   by typing the following instruction in the console (replace <connection_string> with the user's connection string):

		Windows:
			setx AZURE_STORAGE_CONNECTION_STRING "<connection_string>"

		Linux & macOS:
			export AZURE_STORAGE_CONNECTION_STRING="<connection_string>"

		**Please make sure the name of the environment variable is exactly AZURE_STORAGE_CONNECTION_STRING!

	2) Restart all consoles/terminals before going further so that the environment variable can be retrieved
	3) Navigate to the Azure folder, where you will find the scripts for the Azure portion of both tasks 1 and 2
	4) To run the script which will create containers and upload files to the cloud, enter "python upload.py"
	5) To run the interactive display program, enter "python display.py" (make sure that you are in the /Azure folder in the terminal)
	6) Follow the instructions prompted by the program

*********************
Task 1 Things to Note
*********************

	- When displaying all objects in all buckets, the program does not display which bucket the objects are contained in
	- When downloading an object, the program will search all containers and download all files that match the provided name
	- When downloading an object, the downloaded file will be in the "PDFs" folder

**********************
Task 2 Execution - AWS
**********************

Follow the steps below to run the AWS portion of task 2:

	1) Ensure that the files "config" and "credentials" located at ".aws" are correctly set up using the user's region and access keys before execution
	2) Navigate to the AWS folder, where you will find the scripts for the AWS portion of both tasks 1 and 2
	3) To run the script which will create the database table, enter "python createTable.py"
	4) To run the script which will populate the table using the "moviedata.json" file, enter "python populateTable.py"
	5) To run the interactive query program, enter "python query.py"
	6) Follow the instructions prompted by the program

************************
Task 2 Execution - Azure
************************

Follow the steps below to run the Azure portion of task 2:

	1) When creating the Azure CosmosDB account, the type of database should be Azure Table
	2) Ensure that the table connection string of the user is configured by setting it as an environment variable, this can be done 
	   by typing the following instruction in the console (replace <connection_string> with the user's connection string):

		Windows:
			setx AZURE_TABLE_CONNECTION_STRING "<connection_string>"

		Linux & macOS:
			export AZURE_TABLE_CONNECTION_STRING="<connection_string>"

		**Please make sure the name of the environment variable is exactly AZURE_TABLE_CONNECTION_STRING!
	3) Navigate to the Azure folder, where you will find the scritps for the Azure portion of both tasks 1 and 2
	4) To run the script which will create the database table, enter "python createTable.py"
	5) To run the script which will populate the table using the "moviedata.json" file, enter "python populateTable.py"
	6) To run the interactive query program, enter "python query.py"
	7) Follow the instructions prompted by the program

*********************
Task 2 Things to Note
*********************

	- The Primary/Partition Key query portion of the program REQUIRES correct user input (cannot skip this)
	- All other query options are OPTIONAL, meaning you may simply press "Enter" to skip the options listed below:
		=> Secondary/Sort Key query
		=> Filters
		=> Sort
		=> Choosing specific fields to display
	- The interactive query programs make use of PrettyTables, which are an external resource that are acquired by entering "pip install PTable"
	- When querying for a range of a key (# < year < #), the AWS program is inclusive since it uses the "between" function, however the 
	  Azure program is NOT inclusive since it uses lt and gt
	- When referring to attributes in the "info" object for the AWS program, please preppend "info." to the attribute (ex. info.rating, info.rank, etc.)
	- When referring to attributes in the "info" object for the Azure program, please DO NOT preppend anything to the attribute (ex. rating, rank, etc.)
	- When entering the filters for the query in the AWS program, you may only enter ONE filter (ex. info.rating gt 8)
	- The interactive query programs only display year, title, rating, and rank, or a subset of those depending on the fields projected by the user,
	  this is to not clutter the display with too many attributes in a table