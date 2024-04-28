from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)

import random
import string
import bcrypt
from backend.endpoints.connector import connect
from flask import jsonify


def getAllUsers():
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a sql statement
            sql = "SELECT * FROM `User`"
            cursor.execute(sql)
            result = cursor.fetchall()

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
    print("getAllUsers result is", result)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def checkToken(token):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # call a stored procedure    
            cursor.callproc('auth_select', [token,])
            connection.commit()
            result = cursor.fetchall()
        
    if not result:
        return "Error: No Token Found", 401
    else:
        return "Success, Token Found", 200
    
    
def getUser(username):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("SELECT * FROM `User` WHERE username = %s", (username,))
            result = cursor.fetchone()
    return result


def create_random_token(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

    
def login(username, password):
    # check username/password is valid
    user = getUser(username)
    print("auth.py user is", user)
    db_password = user["password"]
    print(db_password)
    
    
    if not bcrypt.checkpw(str.encode(password),str.encode(db_password)):
        return f'password: {password}, is wrong', 401
    else:
        random_string = create_random_token(50)
        print("random string is", random_string)
        
        # ISSUE A TOKEN
        connection = connect()
        result = "GOT NOTHING PAL"
        with connection.cursor() as cursor:
        # call a stored procedure    
            cursor.callproc('auth_insert', [random_string,])
            connection.commit()
            result = cursor.fetchall()
        print("result is", result)
        
        if result:
            response = {
                "u_id" : user['uid'],
                "token" : random_string

            }
            response = jsonify(response)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            return "Unable to login", 401


def register(username,password,fname,lname,computing_id,address,phone_number):
    user = getUser(username)
    print("auth.py user is", user)
    if user:
        return "Username already in use", 400
    
    connection = connect()
    result = "GOT NOTHING PAL"
    try:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("INSERT INTO `User`(username, password, fname, lname, computing_id, address, phone_number)VALUES(%s, %s, %s, %s, %s, %s, %s);",(username,password,fname,lname,computing_id,address,phone_number))
            connection.commit()
            result = cursor.fetchall()
            print("Successfully created new account")
            return "Successfully created new account", 200
    except Exception as e:
        print(e)
        return "Problem creating new account", 500
