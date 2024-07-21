# DBproject
DBMS with python and postgresql. security features are implemented such as sanitizing user imput and using stored procedures to help mitigate SQL injection attacks.
This project is executed based on pgadmin, therefore pgadmin should be used for swift functionality.
<h2> Project Description</h2>
The project implements a system  designed to enhance the operational efficiency of a restaurant by implementing a robust and user-friendly platform for staff management and menu handling. This project involves developing key functionalities such as staff login, menu item management, and search capabilities using Python, Flask, and PostgreSQL. The goal is to create a seamless interface that allows staff members to perform essential tasks efficiently.
<br />

<h2>Key Tasks and Features</h2>

<b> 1. Login Functionality</b>

-  Objective: checkStaffLogin() enables staff members to securely log in using their username and password.<br />
-  Implementation:  validates user credentials against the database. 

<b> 2. Viewing Menu Items </b><br />

-  Objective: findMenuItemsByStaff() Allows staff to view a list of menu items with options to order and filter them.<br />
-  Implementation: retrieve and display menu items from the database.
  
<b> 3. Search Functionality </b><br />

-  Objective: findMenuItemsByCriteria() Enables users to search for menu items based on specific criteria.<br />
-  Implementation: query the database for menu items matching the search criteria.
  
<b> 4. Adding New Menu Items </b><br />

-  Objective: addMenuItem() Provides functionality for staff to add new menu items to the database.<br />
-  Implementation: insert new menu items into the database.
   
<b> 5. Updating Existing Menu Items </b><br />

-  Objective: updateMenuItem() Allows staff to update details of existing menu items in the database.<br />
-  Implementation: modify existing menu items in the database. <br />

## Tools

- Python IDE
- PgAdmin (Postgresql) for database management
  
## Database project interaction
The code employs a variety of Python modules to provide a basic browser-based GUI for the DBsystem. The major components are the Flask framework for the user interface and the psycopg2 module for PostgreSQL database access.  You'll need to install the Psycopg2 and Flask modules. the project comprises two main files:

- <b> DBSchema.sql</b>: a file that includes SQL statements need to be run to construct and initialize the system database before running the application.
- <b> DBProject file</b>: a file that contains the Python project for the DB system.
  
The main program begins in the main.py file. You must provide the right username/password information in the data layer databaseconnection.py.
The presentation layer uses a basic HTML interface accessible through a web browser. The matching page templates are found in the templates/ subfolder, and their CSS style file. The routes.py file handles the transition between the various GUI pages as well as the Flask framework's initialisation. You may execute the code by executing "python main.py". This launches a local web server and displays some debug messages in the terminal; the GUI may then be viewed with any web browser on the same machine using the local URL http://127.0.0.1:5000/ (if that doesn't work, try http://0.0.0.0:5000/). Please keep in mind that in order to end the program, you must first stop the local web server that is currently operating in the background.

## Project execution steps
- Set up the environment to run python
-  download all the python and sql files
-  download python using the commands outlined in python requirements file
- download & install  pgadmin and execute the sql file
- start a CLI in the directory where you downloaded the python files
- execute main.py using python main.py command



