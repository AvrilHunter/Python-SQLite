from flask import jsonify, request
import sqlite3
import utils.utils as utils
import json

def get_treasures():
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        c.execute("SELECT treasure_id, treasure_name, colour, age, cost_at_auction, shop_id FROM treasures;")
        rows = c.fetchall()
        headers = [i[0] for i in c.description]
        conn.close()
        treasures = utils.nested_list_to_dict(rows,headers)
        return jsonify({'treasures':treasures})
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400
    
def get_treasures_by_shop(shop_id):
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = "SELECT treasure_id, treasure_name, colour, age, cost_at_auction, shop_id FROM treasures WHERE shop_id = ?;"
        c.execute(sql, (shop_id,))
        rows = c.fetchall()
        headers = [i[0] for i in c.description]
        conn.close()
        treasures = utils.nested_list_to_dict(rows,headers)
        return jsonify({'treasure':treasures})
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400

def post_treasure(treasure):
    treasure_tuple = tuple((treasure["treasure_name"],treasure["colour"],treasure["age"],treasure["cost_at_auction"],treasure["shop_id"]))
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = """INSERT INTO treasures
            (treasure_name, colour, age, cost_at_auction, shop_id)
            VALUES """ + str(treasure_tuple) +";"
        c.execute(sql)
        conn.commit()
        newID = c.lastrowid
        conn.close()
        newTreasure = get_treasure_by_id(str(newID))
        return newTreasure
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400

def get_treasure_by_id(id):
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = "SELECT treasure_id, treasure_name, colour, age, cost_at_auction, shop_id FROM treasures WHERE treasure_id=?;"
        c.execute(sql, (id,))
        rows = c.fetchall()
        headers = [i[0] for i in c.description]
        conn.close()
        treasure = utils.list_to_dict(rows[0],headers)
        return jsonify({'treasure':treasure})
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400
    except IndexError:
        return {"message":"treasure does not exist"}, 404
    
def delete_treasure(id):
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = """DELETE FROM treasures WHERE treasure_id=? RETURNING *;"""
        c.execute(sql, (id,))
        rows = c.fetchall()
        headers =[item[0] for item in c.description]
        conn.commit()
        conn.close()
        treasure = utils.nested_list_to_dict(rows, headers)
        return jsonify({'treasure':treasure})      
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400
    except IndexError:
        return {"message":"treasure does not exist"}, 404