# DBproject
DBMS with python and postgresql. security features are implemented such as sanitizing user imput and using stored procedures to help mitigate SQL injection attacks.
This project is executed based on pgadmin, therefore pgadmin should be used for swift functionality.
<h2> Project Description</h2>
The project implements a system  designed to enhance the operational efficiency of a restaurant by implementing a robust and user-friendly platform for staff management and menu handling. This project involves developing key functionalities such as staff login, menu item management, and search capabilities using Python, Flask, and PostgreSQL. The goal is to create a seamless interface that allows staff members to perform essential tasks efficiently.
<br />

<h2>Key Tasks and Features</h2>

<b> 1. Login Functionality</b>

-  Objective: Enable staff members to securely log in using their username and password.<br />
-  Implementation: Develop a function checkStaffLogin that validates user credentials against the database. 

<b> 2. Viewing Menu Items </b><br />

-  Objective: Allow staff to view a list of menu items with options to order and filter them.<br />
-  Implementation: Create the findMenuItemsByStaff function to retrieve and display menu items from the database.
  
<b> 3. Search Functionality </b><br />

-  Objective: Enable users to search for menu items based on specific criteria.<br />
-  Implementation: Implement the findMenuItemsByCriteria function to query the database for menu items matching the search criteria.
  
<b> 4. Adding New Menu Items </b><br />

-  Objective: Provide functionality for staff to add new menu items to the database.<br />
-  Implementation: Develop the addMenuItem function to insert new menu items into the database.
   
<b> 5. Updating Existing Menu Items </b><br />

-  Objective: Allow staff to update details of existing menu items in the database.<br />
-  Implementation: Implement the updateMenuItem function to modify existing menu items in the database. <br />

## Tools

- Python
- PgAdmin (Postgresql) for database management

## Project execution steps
- Set up the environment to run python
-  download all the python and sql files
-  download python using the commands outlined in python requirements file
- download & install  pgadmin and execute the sql file
- start a CLI in the directory where you downloaded the python files
- execute main.py using python main.py command



