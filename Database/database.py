"""
    Author: Nick Bout
    Class: DatabaseClass

    This class contains functions to handle everything related to the database.
    We use the PyMySQL module to connect with the database. (https://github.com/PyMySQL/PyMySQL)
"""

#Imports
import pymysql
import datetime
from Utils.config import DB_HOST, DB_PASS, DB_USER, DB

# Create a connection to the database
connection = pymysql.connect(host=DB_HOST,
                             user=DB_USER,
                             passwd=DB_PASS,
                             db=DB)
current = connection.cursor(pymysql.cursors.DictCursor)


class DatabaseClass:
    """
             Databaseclass containing all the functions
    """

    def close_connection(self):
        """
            Closed the database connection.
        """
        connection.close()

    def select(self, query) -> dict:
        """
            Function to use a SQL SELECT based on a given SQL query.

            Args:
                STRING: query: SQL query
            Returns:
                select: dictionary with the data returned from the SQL query
        """
        try:
            current.execute(query)
            result = current.fetchall()

            return result if len(result) > 1 else result[0]
        except Exception as error:
            print("Exception:", error)

    def insert(self, query):
        """
            Function to use a SQL INSERT based on a given SQL query.

            Args:
                STRING: query: SQL query
            Returns:
                --
        """
        try:
            with connection.cursor() as cursor:
                # Create a new record
                cursor.execute(query)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except Exception as error:
            print("Exception:", error)

    def update(self, query):
        """
            Function to use a SQL UPDATE based on a given SQL query.

            Args:
                STRING: query: SQL query
            Returns:
                --
        """

        try:
            with connection.cursor() as cursor:
                # Create a new record
                cursor.execute(query)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except Exception as error:
            print("Exception:", error)

    def delete(self, query):
        """
            Function to use a SQL DELETE based on a given SQL query.

            Args:
                STRING: query: SQL query
            Returns:
                --
        """
        try:
            with connection.cursor() as cursor:
                # Create a new record
                cursor.execute(query)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except Exception as error:
            print("Exception:", error)

    def get_customer(self, email, password) -> dict:
        """"
            Gets login data using the email and password. This function is used for login checks

            Args:
                STRING: email: Email of user
                STRING: password: Password of user
            Returns:
                Dict: dictionary with the Email, User_ID, User_Role_ID from the SQL query, Returns None if no results
        """
        query = "SELECT " \
                "Login.Email, " \
                "Login.User_ID, " \
                "Login.User_Role_ID " \
                "FROM Login WHERE email = '{0}' AND password = '{1}' LIMIT 1".format(email, password)
        return self.select(query)

    def get_equipment(self) -> dict:
        query = "SELECT ID, Name FROM Equipment"
        return self.select(query)

    def get_locations(self) -> dict:
        """"
            Gets every location

            Args:
                --
            Returns:
                Dict: dictionary with the locations
        """
        query = "SELECT ID, name FROM Location"
        return self.select(query)

    def set_sport_activity(self, equipment_id, user_id, time, calories):
        query = "INSERT INTO " \
                "`Equipment_used`(`" \
                "Equipment_ID`, " \
                "`User_ID`, " \
                "`Time`, " \
                "`Calories`) VALUES ({0},{1},{2},{3})".format(equipment_id, user_id, time, calories)
        self.insert(query)
