import sqlite3
import random
import home
import base64
import hashlib

def users_database():
  #establishes a connection
  sqliteConnection = sqlite3.connect('users_database.db')
  cursor = sqliteConnection.cursor()

  #creates a table
  cursor.execute('''CREATE TABLE IF NOT EXISTS users_database
      (key INTEGER PRIMARY KEY AUTOINCREMENT,
          first_name TEXT,
          last_name TEXT,
          username TEXT,
          password TEXT
      )''')
  #saves the creation of the table
  sqliteConnection.commit()


#saves the data obtained from creating an account into the sql database
def save_credentials():
    user_data = home.user_data

    sqliteConnection = sqlite3.connect('users_database.db')
    cursor = sqliteConnection.cursor()

    #creates a random key
    key = random.randrange(100000, 999999)

    #makes sure each key is different
    cursor.execute("SELECT key FROM users_database WHERE key = {key}".format(key=key))
    ans = cursor.fetchall() 
    while ans !=[]:
      key = random.randrange(100000,999999)

    #inserts the data from create account into the database
    cursor.execute('INSERT INTO users_database VALUES ({key}, "{first_name}", "{last_name}", "{username}", "{password}")'.format(key=key, first_name=user_data['first name'], last_name=user_data['last name'], username=str(user_data['username']), password=str(hashlib.sha256(user_data['password'].encode()).hexdigest())))

    # print(user_data['username'], user_data['password'], hashlib.sha256(user_data['password'].encode()).hexdigest())

    #commits changes and closes connection
    sqliteConnection.commit()
    sqliteConnection.close()


#extracts username and password from sql database
def get_data(userValue, passValue):
    sqliteConnection = sqlite3.connect('users_database.db')
    cursor = sqliteConnection.cursor()

    # print(userValue, passValue, hashlib.sha256(passValue.encode()).hexdigest())

    #hashes password    
    cursor.execute("SELECT * FROM users_database WHERE username = '{a}' AND password = '{b}'".format(a=userValue, b=hashlib.sha256(passValue.encode()).hexdigest()))
    user_found = cursor.fetchall()

    #commits changes and closes connection
    sqliteConnection.commit()
    sqliteConnection.close()
    #returns that the user exists for the username and password that was found in the sql database
    if len(userValue) > 0 and len(passValue) > 0:
        return user_found
    else:
        return None