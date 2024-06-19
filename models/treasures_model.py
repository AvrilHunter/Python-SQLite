from flask import jsonify, request
import sqlite3


def get_treasures():
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        c.execute("SELECT * FROM treasures;")
        rows = c.fetchall()
        conn.close()
        return jsonify({'treasures':rows})
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400
    
def get_treasures_by_shop(shop_id):
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = "SELECT * FROM treasures WHERE shop_id = ?;"
        c.execute(sql, (shop_id,))
        rows = c.fetchall()
        conn.close()
        return jsonify({'treasure':rows})
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400

def post_treasure(treasure):
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = """INSERT INTO treasures
            (treasure_name, colour, age, cost_at_auction, shop_id)
            VALUES """ + treasure +";"
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
        sql = "SELECT * FROM treasures WHERE treasure_id=?;"
        c.execute(sql, (id,))
        rows = c.fetchall()
        conn.close()
        return jsonify({'treasure':rows[0]})
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
        conn.commit()
        conn.close()
        return jsonify({'treasure':rows[0]})      
    except sqlite3.OperationalError as e:
        return jsonify({"error": "bad request"}),400
    except IndexError:
        return {"message":"treasure does not exist"}, 404