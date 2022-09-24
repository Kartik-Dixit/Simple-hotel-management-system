import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",                                      #change user to your mysql user name
  password="system",                                #change password to your mysql password
  database="hotel_bill",
  auth_plugin='mysql_native_password'
)

# create database
mycursor= mydb.cursor()
mycursor.execute("CREATE DATABASE hotel_bill")
mycursor.execute("CREATE TABLE customer_details (id INT AUTO_INCREMENT PRIMARY KEY,roomno INT(3), name VARCHAR(255), address VARCHAR(255), phoneno VARCHAR(12), date_in VARCHAR(10) , date_out VARCHAR (10),food_cost INT(5), room_cost INT(6), gst float(8), total_cost float (8)) ;")


