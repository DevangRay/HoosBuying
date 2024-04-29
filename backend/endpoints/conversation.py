from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)

from backend.endpoints.connector import connect
from flask import jsonify

def getAllConvoIds(user_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("SELECT c.*, u.username as host_user, u.fname as host_fname, u.lname as host_lname, u.computing_id as host_cid, u2.username as cust_user, u2.fname as cust_fname, u2.lname as cust_lname, u2.computing_id as cust_cid, l.title, l.price, l.status_id , s.status_name FROM Conversation c join `User` u on c.host_id = u.uid join `User` u2 on c.customer_id =u2.uid join Listings l on c.listing_id = l.listing_id  join Status s on l.status_id = s.status_id WHERE host_id = %s OR customer_id = %s order by c.last_updated DESC;", (user_id, user_id, ))
            result = cursor.fetchall()
    return result
    # print(type(result))
    # for value in result:
    #     print("value is", value)
    # response = jsonify(result)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response
    
def getAllOwnerConvoIds(user_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("SELECT c.*, u.username as host_user, u.fname as host_fname, u.lname as host_lname, u.computing_id as host_cid, u2.username as cust_user, u2.fname as cust_fname, u2.lname as cust_lname, u2.computing_id as cust_cid, l.title, l.price, l.status_id , s.status_name FROM Conversation c join `User` u on c.host_id = u.uid join `User` u2 on c.customer_id =u2.uid join Listings l on c.listing_id = l.listing_id  join Status s on l.status_id = s.status_id WHERE host_id = %s order by c.last_updated DESC;", (user_id, ))
            result = cursor.fetchall()
    return result

def getAllCustomerConvoIds(user_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("SELECT c.*, u.username as host_user, u.fname as host_fname, u.lname as host_lname, u.computing_id as host_cid, u2.username as cust_user, u2.fname as cust_fname, u2.lname as cust_lname, u2.computing_id as cust_cid, l.title, l.price, l.status_id , s.status_name FROM Conversation c join `User` u on c.host_id = u.uid join `User` u2 on c.customer_id =u2.uid join Listings l on c.listing_id = l.listing_id  join Status s on l.status_id = s.status_id WHERE customer_id = %s order by c.last_updated DESC;", (user_id, ))
            result = cursor.fetchall()
    return result

def getConversationObject(user_id, convo_arr):
    connection = connect()
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            for i in range(len(convo_arr)):
                cursor.execute("select * from Message m where convo_id = %s order by time DESC;", (convo_arr[i]["convo_id"], ))
                message_arr = cursor.fetchall()
                convo_arr[i]["message_array"] = message_arr
                
    response = jsonify(convo_arr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def getAllConversations(user_id):
    convo_arr = getAllConvoIds(user_id)
    response = getConversationObject(user_id, convo_arr)
    return response

def getOwnerConversations(user_id):
    convo_arr = getAllOwnerConvoIds(user_id)
    response = getConversationObject(user_id, convo_arr)
    return response

def getCustomerConversations(user_id):
    convo_arr = getAllCustomerConvoIds(user_id)
    response = getConversationObject(user_id, convo_arr)
    return response




def getConvoById(convo_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("SELECT c.*, u.username as host_user, u.fname as host_fname, u.lname as host_lname, u.computing_id as host_cid, u2.username as cust_user, u2.fname as cust_fname, u2.lname as cust_lname, u2.computing_id as cust_cid, l.title, l.price, l.status_id , s.status_name FROM Conversation c join `User` u on c.host_id = u.uid join `User` u2 on c.customer_id =u2.uid join Listings l on c.listing_id = l.listing_id  join Status s on l.status_id = s.status_id WHERE c.convo_id = %s;", (convo_id, ))
            result = cursor.fetchone()
            cursor.execute("select * from Message m where convo_id = %s order by time DESC;", (convo_id, ))
            message_arr = cursor.fetchall()
            result["message_array"] = message_arr    
    return result

def getConversationById(convo_id):
    convo= getConvoById(convo_id)
    response = jsonify(convo)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def addNewMessage(listing_id,host_id,customer_id,new_message,user_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    try:
        with connection:
            with connection.cursor() as cursor:
            # Create a new record
                cursor.execute("CALL add_message(%s,%s,%s,%s,%s)", (listing_id,host_id,customer_id,new_message,user_id))
                connection.commit()
                return "Successfully sent message", 200
    except Exception as e:
        print(e)
        return "Problem sending message", 500  