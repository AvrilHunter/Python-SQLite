from flask import Flask, jsonify, request
import controllers.treasures_controllers as treasure
import models.shops_model as shops

app = Flask(__name__)

@app.route("/")
def home():
    return '''<p>Treasures API</p>
            <p>Endpoints available: </p>
            <p>GET: /api/treasures</p>
            <p>GET: /api/shops order by ASC/DESC</p>
            <p>GET: /api/treasures/shop_id </p>
            '''

@app.get("/api/treasures")
def show_treasures():
        return treasure.get_treasures()
    
@app.route("/api/shops")
def show_shops():
    if request.method=="GET":
        order = request.args.get("order")
        return shops.get_shops(order)
    
@app.route("/api/treasures/<shop_id>")
def treasures_by_shop(shop_id):
    if request.method=="GET":
        return treasure.get_treasures_by_shop(shop_id)