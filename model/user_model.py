import mysql.connector
import json

class User_Model():
    def __init__(self):
        # connection establish:
        try:
            self.con = mysql.connector.connect(host='localhost', user='root', password='testing', database='flask_rest_api')
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection established successfully")
        except:
            print("Unable to establish connection.")

    def user_get_all_model(self):
        # Query execution code
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) < 0:
            return json.dumps(result)
        else:
            return "No Data Found"
    
    def user_add_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email,  role, password, phone) VALUES('{data['name']}', '{data['email']}', '{data['role']}', '{data['password']}', '{data['phone']}')")
       
        return "User created successfully."