import mysql.connector

class User_Model():
    def __init__(self):
        # connection establish:
        try:
            mysql.connector.connect(host='localhost', user='root', password='', database='flask_rest_api')
            print("Connection established successfully")
        except:
            print("Unable to establish connection.")
    def user_get_all_model(self):
        # connection establish:

        # Query execution code

        return "this is user signup model"