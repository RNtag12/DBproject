#!/usr/bin/env python3
# !pip3 install psycopg2
import psycopg2

#####################################################
##  Database Connection
#####################################################

'''
Connect to the database using the connection string
'''
def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y24s1c9120_yzha4025"
    passwd = "vCjNykg4"
    myHost = "awsprddbs4836.shared.sydney.edu.au"

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

    conn = openConnection()
    if conn is None:
        print('You are not connected to the database!')
        return None

    else: 
        print('You are successfully connected to the database')

        try:
            curs = conn.cursor()
            curs.callproc('stafflogin', [staffID, password])
            row = curs.fetchall()

            # print(row)
            # print('---')
            # print(list(row[0]))

            return list(row[0])


        except psycopg2.Error as sqle:
            print("Error during query execution")
            print(sqle.pgerror)
            return None
        
        finally:
            curs.close()
            conn.close()


'''
List all the associated menu items in the database by staff
'''
def findMenuItemsByStaff(staffID):

    results1 = []

    conn = openConnection()
    if conn is None:
        print('You are not connected to the database!')
        return None

    else: 
        print('You are successfully connected to the database')

        try:
            curs = conn.cursor()
            curs.callproc('findMenuItemsByStaff', [staffID])

            nr = 0
            row = curs.fetchone()

            while row is not None:
                nr+=1
                que = {}

                que['menuitem_id'] = row[0]
                que['name'] = row[1]
                que['description'] = row[2]
                que['category'] = row[3]
                que['coffeeoption'] = row[4]
                que['price'] = row[5]
                que['reviewdate'] = row[6]
                que['reviewer'] = row[7]

                results1.append(que)

                # print(results1)

                row = curs.fetchone()


            if nr == 0:
                print("No entries found.")
            
            curs.close()

            return results1


        except psycopg2.Error as sqle:
            print("Error during query execution")
            print(sqle.pgerror)
            return None
        
        finally:
            curs.close()
            conn.close()



'''
Find a list of menu items based on the searchString provided as parameter
See assignment description for search specification
'''
def findMenuItemsByCriteria(keyword):

    results1 = []

    conn = openConnection()
    if conn is None:
        print('You are not connected to the database!')
        return None

    else: 
        print('You are successfully connected to the database')

        try:
            curs = conn.cursor()
            curs.callproc('findMenuItemsByCriteria', [keyword])

            nr = 0
            row = curs.fetchone()

            while row is not None:
                nr+=1
                que = {}

                que['menuitem_id'] = row[0]
                que['name'] = row[1]
                que['description'] = row[2]
                que['category'] = row[3]
                que['coffeeoption'] = row[4]
                que['price'] = row[5]
                formatreviewdate = row[6] if row[6] else ''
                que['reviewdate'] = formatreviewdate
                formatreviewer = row[7] if row[7] else ''
                que['reviewer'] = formatreviewer

                results1.append(que)

                print(results1)

                # for each in results1:
                # for each in results1:
                #     each['reviewdate'] = each['reviewdate'].strftime('%d-%m-%Y')


                row = curs.fetchone()


            if nr == 0:
                print("No entries found.")
            
            curs.close()

            return results1


        except psycopg2.Error as sqle:
            print("Error during query execution")
            print(sqle.pgerror)
            return None
        
        finally:
            curs.close()
            conn.close()



def addMenuItem(name, description, categoryone, categorytwo, categorythree, coffeetype, milkkind, price):


    # Open database connection
    connection = openConnection()
    cursor = connection.cursor()

    try:
        # Call the stored procedure
        cursor.callproc('AddMenuItem', [name, description, categoryone, categorytwo, categorythree,coffeetype,milkkind,price])
        result = cursor.fetchone()
        
        # Commit the changes
        connection.commit()

        # return True
        
        # print("Menu item added successfully!")

        if result and result[0]:
            print("Menu item Added successfully!")
            return True
        else:
            print("Added failed: Menu item not found or other issue.")
            return False
    except Exception as e:
        # Handle any errors that occur during the procedure call
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and the connection
        cursor.close()
        connection.close()





# def updateMenuItem(menuitem_id, name, description, categoryone, categorytwo, categorythree, coffeetype, milkkind, price, reviewdate, reviewer):
#     # Open database connection
#     connection = openConnection()
#     cursor = connection.cursor()

#     try:
#         # Call the stored procedure
#         cursor.callproc('UpdateMenuItem', [
#             menuitem_id, name, description, categoryone, categorytwo, categorythree,
#             coffeetype, milkkind, price, reviewdate, reviewer
#         ])
#         result = cursor.fetchone()

#         # Commit the changes
#         connection.commit()

#         print(result)
#         print('---')
#         print(result[0])

#         return result
#         print("Menu item updated successfully!")

#         # if result[0]:
#         #     print("Menu item updated successfully!")
#         #     return True
#         # else:
#         #     print("Update failed: Menu item not found.")
#         #     return False
#     except Exception as e:
#         # Handle any errors that occur during the procedure call
#         print(f"An error occurred: {e}")
#         return False
#     finally:
#         # Close the cursor and the connection
#         cursor.close()
#         connection.close()

def updateMenuItem(menuitem_id, name, description, categoryone, categorytwo, categorythree, coffeetype, milkkind, price, reviewdate, reviewer_full_name):
    # Open database connection
    connection = openConnection()
    cursor = connection.cursor()

    try:
        # Convert full name to StaffID
        cursor.execute("SELECT StaffID FROM Staff WHERE FirstName || ' ' || LastName = %s", (reviewer_full_name,))
        reviewer_record = cursor.fetchone()
        if reviewer_record is None:
            print(f"Reviewer {reviewer_full_name} not found in Staff table.")
            return False
        reviewer_id = reviewer_record[0]

        cursor.callproc('UpdateMenuItem', [
            menuitem_id, name, description, categoryone, categorytwo, categorythree,
            coffeetype, milkkind, price, reviewdate, reviewer_id
        ])
        result = cursor.fetchone()

        # Commit the changes
        connection.commit()

        if result and result[0]:
            print("Menu item updated successfully!")
            return True
        else:
            print("Update failed: Menu item not found or other issue.")
            return False


    except Exception as e:
        # Handle any errors that occur during the procedure call
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and the connection
        cursor.close()
        connection.close()


















