#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connection
#####################################################

'''
Connect to the database using the connection string
'''
def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = ""
    passwd = ""
    myHost = ""

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database=userid,
                                    user=userid,
                                    password=passwd,
                                    host=myHost)
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    
    # return the connection to use
    return conn

'''
Validate staff based on username and password
'''
def checkStaffLogin(staffID, password):

    userInfo = None

    try:
        conn = openConnection()
        curs = conn.cursor()

        # execute the query
        curs.execute("SELECT StaffID, Password, FirstName, LastName, Age, Salary FROM Staff \
            WHERE LOWER(StaffID) = LOWER(%s) AND Password = %s",(staffID,password,))
        user = curs.fetchone()

        if user is not None:
            userInfo = [user[0], user[1], user[2], user[3], user[4], user[5]]
        else:
            print("Wrong login userName or password")

    except psycopg2.Error as sqle:
        print("There is a problem with check staff login. " + sqle.pgerror)

    finally:
        # commit the transaction
        conn.commit()

        # clean up #/
        curs.close()
        conn.close()

    return userInfo


'''
List all the associated menu items in the database by staff
'''
def findMenuItemsByStaff(staffID):

    menuItem_list = []

    try:
        conn = openConnection()
        curs = conn.cursor()

        # Execute the query to retrieve menu items
        curs.execute("""SELECT m.MenuItemID, m.Name, COALESCE(m.Description,'') as description, 
                            CONCAT_WS('|',c1.CategoryName,c2.CategoryName,c3.CategoryName) as category, 
                            CONCAT_WS(' - ', t.CoffeeTypeName, k.MilkKindName) as coffeeoption, m.price, 
                            COALESCE(to_char(m.ReviewDate, 'DD-MM-YYYY'),'') as reviewdate, CONCAT_WS(' ', s.FirstName, s.LastName) as staff
                        FROM MenuItem m JOIN Category c1 ON m.CategoryOne = c1.CategoryID
                            LEFT JOIN Category c2 ON m.CategoryTwo = c2.categoryid
							LEFT JOIN Category c3 ON m.CategoryThree = c3.categoryid
                            LEFT JOIN CoffeeType t ON m.CoffeeType = t.CoffeeTypeID
                            LEFT JOIN MilkKind k ON m.MilkKind = k.MilkKindID
                            JOIN Staff s ON m.Reviewer = s.StaffID
                        WHERE Reviewer = %s
                        ORDER BY ReviewDate ASC, Description ASC, Price DESC""", (staffID,))
        menuItems = curs.fetchall()

        menuItem_list = [{
            'menuitem_id': row[0],
            'name': row[1],
            'description': row[2],
            'category': row[3],
            'coffeeoption': row[4],
            'price': row[5],
            'reviewdate': row[6],
            'reviewer': row[7]
        } for row in menuItems]

    except psycopg2.Error as sqle:
        print("There is a problem with find menu items by staff. " + sqle.pgerror)

    finally:
        # commit the transaction
        conn.commit()

        # clean up #/
        curs.close()
        conn.close()

    return menuItem_list


'''
Find a list of menu items based on the searchString provided as parameter
See assignment description for search specification
'''
def findMenuItemsByCriteria(searchString):

    menuItem_list = []

    try:
        conn = openConnection()
        curs = conn.cursor()

        # Execute the query to retrieve menu items by search criteria
        curs.callproc('findMenuItemsByCriteria', [searchString])
        menuItems = curs.fetchall()

        menuItem_list = [{
            'menuitem_id': row[0],
            'name': row[1],
            'description': row[2],
            'category': row[3],
            'coffeeoption': row[4],
            'price': row[5],
            'reviewdate': row[6],
            'reviewer': row[7]
        } for row in menuItems]

    except psycopg2.Error as sqle:
        print("There is a problem with find menu items by criteria. " + sqle.pgerror)

    finally:
        # commit the transaction
        conn.commit()

        # clean up #/
        curs.close()
        conn.close()

    return menuItem_list


'''
Add a new menu item
'''
def addMenuItem(name, description, categoryone, categorytwo, categorythree, coffeetype, milkkind, price):

    try:
        if not price.isdecimal():
            raise ValueError
    except ValueError as error:
        print("There is a problem with add menu item. Invalid price.")
        return False

    try:
        conn = openConnection()
        curs = conn.cursor()

        # Execute insert a new menu
        curs.callproc('addMenuItem', [name, description, categoryone, categorytwo, categorythree, coffeetype, milkkind, price])

    except psycopg2.Error as sqle:
        print("There is a problem with add menu item. " + sqle.pgerror)
        return False

    finally:
        # commit the transaction
        conn.commit()

        # clean up #/
        curs.close()
        conn.close()

    return True


'''
Update an existing menu item
'''
def updateMenuItem(menuitem_id, name, description, categoryone, categorytwo, categorythree, coffeetype, milkkind, price, reviewdate, reviewer):

    try:
        if not price.isdecimal():
            raise ValueError
    except ValueError as error:
        print("There is a problem with update menu item. Invalid price.")
        return False

    try:
        conn = openConnection()
        curs = conn.cursor()

        # Execute update a menu
        curs.callproc('updateMenuItem', [menuitem_id, name, description, categoryone, categorytwo, categorythree, coffeetype, milkkind, price, reviewdate, reviewer])

    except psycopg2.Error as sqle:
        print("There is a problem with update menu item. " + sqle.pgerror)
        return False

    finally:
        # commit the transaction
        conn.commit()

        # clean up #/
        curs.close()
        conn.close()

    return True
