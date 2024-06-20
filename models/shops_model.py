import sqlite3
from flask import jsonify
import utils.utils as utils

def get_shops(order):
    if not order:
        order = "ASC"
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = """
        SELECT shop_id, shop_name, owner, slogan 
        FROM shops 
        ORDER BY shop_name """ + order +";"
        c.execute(sql)
        rows = c.fetchall()
        headers = [item[0] for item in c.description]
        shops = utils.nested_list_to_dict(rows, headers)
        conn.close()
        return jsonify({'shops':shops})
    except sqlite3.OperationalError as e:
        return {"error": "bad request"},400


def get_shop_by_id(shop_id):
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        sql = """
        SELECT shop_id, shop_name, owner, slogan 
        FROM shops 
        WHERE shop_id=""" + shop_id +";"
        c.execute(sql)
        rows = c.fetchall()
        headers = [i[0] for i in c.description]
        conn.close()
        shop = utils.list_to_dict(rows[0],headers)
        return jsonify({'shop':shop})
    except sqlite3.OperationalError as e:
        return {"error": "bad request"}, 400
    except IndexError:
        return {"message":"shop does not exist"}, 404

def update_shop(shop_id, body):
   try:
        conn = sqlite3.connect("treasures.db")
        c= conn.cursor()
        sql = """
        UPDATE shops
        SET slogan =?
        WHERE shop_id = ?;"""
        c.execute(sql, (body, shop_id))
        conn.commit()
        conn.close()
        new_shop =get_shop_by_id(str(shop_id))
        return new_shop
   except sqlite3.OperationalError as e:
       return {"error": "bad request"}, 400
   except IndexError:
        return {"message":"shop does not exist"}, 404
    
