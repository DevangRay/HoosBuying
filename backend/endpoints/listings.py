from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)

from backend.endpoints.connector import connect
from flask import jsonify

def getAllListings():
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql = """select l.*, dm.method_name, s.status_name, u.username, u.fname , u.lname , u.computing_id, tl.tag_id 
            from Listings l join DeliveryMethod dm on l.delivery_id = dm.delivery_id  
                            join Status s on l.status_id = s.status_id 
                            join `User` u on l.owner_id = u.uid 
                            join TagListing tl on l.listing_id = tl.listing_id """
            cursor.execute(sql)
            result = cursor.fetchall()
            
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def getOneListing(listing_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Get one listing based on listing_id
            cursor.execute("""select l.*, dm.method_name, s.status_name, u.username, u.fname , u.lname , u.computing_id, tl.tag_id 
            from Listings l join DeliveryMethod dm on l.delivery_id = dm.delivery_id  
                            join Status s on l.status_id = s.status_id 
                            join `User` u on l.owner_id = u.uid 
                            join TagListing tl on l.listing_id = tl.listing_id
            where l.listing_id = %s;""", (listing_id))
            result = cursor.fetchall()
            
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def insertListing(description, status_id, delivery_id, owner_uname, title, price, tag_id=8):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.callproc('listing_insert', [description, status_id, delivery_id, owner_uname, title, float(price), tag_id])
            connection.commit()
            result = cursor.fetchall()
            
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def updateListing(column_dict, listing_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            for key in column_dict.keys():
                print("key is", key)
                print("value is", column_dict[key])
                if key == "description":
                    cursor.execute("UPDATE Listings SET description = %s WHERE listing_id = %s;", (column_dict["description"], int(listing_id)))
                    connection.commit()
                elif key == "status_id":
                    cursor.execute("UPDATE Listings SET status_id = %s WHERE listing_id = %s;", (column_dict["status_id"], int(listing_id)))
                    connection.commit()
                elif key == "delivery_id":
                    cursor.execute("UPDATE Listings SET delivery_id = %s WHERE listing_id = %s;", (column_dict["delivery_id"], int(listing_id)))
                    connection.commit()
                elif key == "title":
                    cursor.execute("UPDATE Listings SET title = %s WHERE listing_id = %s;", (column_dict["title"], int(listing_id)))
                    connection.commit()
                elif key == "price":
                    cursor.execute("UPDATE Listings SET price = %s WHERE listing_id = %s;", (column_dict["price"], int(listing_id)))
                    connection.commit()
            
    response = "listing is " + str(listing_id)
    return response

def filterByTags(tag_array):
    query = ""
    if len(tag_array) > 1:
        ids = tuple(tag_array)  
        query = """
            select l.*, dm.method_name, s.status_name, u.username, u.fname , u.lname , u.computing_id, tl.tag_id 
            from Listings l join DeliveryMethod dm on l.delivery_id = dm.delivery_id  
                join Status s on l.status_id = s.status_id 
                join `User` u on l.owner_id = u.uid 
                join TagListing tl on l.listing_id = tl.listing_id
            where tl.tag_id in {}""".format(ids)
    else:
        ids = tag_array[0]
        query = """
                select l.*, dm.method_name, s.status_name, u.username, u.fname , u.lname , u.computing_id, tl.tag_id 
                from Listings l join DeliveryMethod dm on l.delivery_id = dm.delivery_id  
                    join Status s on l.status_id = s.status_id 
                    join `User` u on l.owner_id = u.uid 
                    join TagListing tl on l.listing_id = tl.listing_id
                where tl.tag_id ={}""".format(ids)
    print("filterByTags post query is", query)
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Get all Listings by Tuple
            cursor.execute(query)
            result = cursor.fetchall()
            
    print("result is", result)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response