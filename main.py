from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return '''<p>Treasures API</p>
            <p>Endpoints available: GET: /api/treasures</p>
            <p>GET: /api/shops</p>'''

@app.get("/api/treasures")
def show_treasures():
        return get_treasures()
    
@app.route("/api/shops")
def show_shops():
    if request.method=="GET":
        return get_shops()

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
    
def get_shops():
    try:
        conn = sqlite3.connect("treasures.db")
        c = conn.cursor()
        c.execute("SELECT * FROM shops;")
        rows = c.fetchall()
        conn.close()
        return jsonify({'shops':rows})
    except sqlite3.OperationalError as e:
        return {"error": 'table not found'}