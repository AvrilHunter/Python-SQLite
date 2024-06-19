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
        return {"error": 'table not found'}
    
def get_treasures_by_shop(shop_id):
    conn = sqlite3.connect("treasures.db")
    c = conn.cursor()
    sql = "SELECT * FROM treasures WHERE shop_id = ?;"
    c.execute(sql, shop_id)
    rows = c.fetchall()
    conn.close()
    return jsonify({'treasure':rows})

def post_treasure(treasure):
    conn = sqlite3.connect("treasures.db")
    c = conn.cursor()
    sql = """INSERT INTO treasures
		(treasure_name, colour, age, cost_at_auction, shop_id)
		VALUES """ + treasure +";"
    c.execute(sql)
    conn.commit()
    newID = c.lastrowid
    conn.close()
    return jsonify({"treasure":treasure})