import mysql.connector
import json

class UserModel():
    def __init__(self):
        # Connection Establishment Code
        try:
           self.my_sql =  mysql.connector.connect(host="localhost",user="root",password="hpsubu2309", database="train_data")  
           self.cursor = self.my_sql.cursor(dictionary=True)  # Dictinory mean it will come list of dictinary format
           print("connection Successfully",self.cursor)    # cursor mean its connect to db into 
        except Exception as e :
            print(e)

    def users_details(self):
        try:
            self.cursor.execute('SELECT * FROM subu')
            data = self.cursor.fetchall()
            if len(data) > 0:
                return json.dumps(data)
            else:
                return "Data not available"
        except Exception as e:
            print(e)
    
      
    def Regestration(self):


        return "This is regestration Model"