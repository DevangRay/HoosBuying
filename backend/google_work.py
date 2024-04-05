import json
import pymysql
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def connect():
    # Please fill in these values.
    # project_id = "cs4750db-413417"
    print("IN CONNECT")
    connection = pymysql.connect(
        host="34.145.170.154", 
        user="website", 
        password="websitepassword", 
        database= "HoosBuying",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("CONNECTION TO RETURN IS", connection)
    return connection

@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql = "SELECT * FROM `User`"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print("RESULT is ", result)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    

if __name__ == '__main__':
   app.run(port=5000)
#    print("IN MAIN")
#    connection = connect()
#    getRecord(connection)