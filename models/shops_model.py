import sqlite3
from flask import jsonify

def get_shops(order):
    if not order:
        order = "ASC"
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = "SELECT * FROM shops ORDER BY shop_name " + order +";"
        c.execute(sql)
        rows = c.fetchall()
        conn.close()
        return jsonify({'shops':rows})
    except sqlite3.OperationalError as e:
        return {"error": 'table not found'}