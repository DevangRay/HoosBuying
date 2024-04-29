import pymysql

def connect():
    connection = pymysql.connect(
        host="", 
        user="", 
        password="", 
        database= "",
        cursorclass=pymysql.cursors.DictCursor
    )
    if connection:
        return connection
    else:
        return "Connection Error", 404
