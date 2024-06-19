from flask import Flask, request
import models.treasures_model as treasure
import models.shops_model as shops
import re

app = Flask(__name__)

@app.route("/")
def home():
    return '''<p>Treasures API</p>
            <p>Endpoints available: </p>
            <p>GET: /api/treasures</p>
            <p>POST: /api/treasures - takes request in format (treasure_name, colour, age, cost_at_auction, shop_id)</p>
            <p>GET: /api/treasures/<treasure_id></p>
            <p>GET: /api/shops order by ASC/DESC</p>
            <p>GET: /api/treasures/shops/shop_id </p>
            '''

@app.route("/api/shops")
def show_shops():
    if request.method=="GET":
        order = request.args.get("order")
        return shops.get_shops(order)
    
@app.route("/api/treasures/shops/<shop_id>")
def treasures_by_shop(shop_id):
    if request.method=="GET":
        return treasure.get_treasures_by_shop(shop_id)
    
@app.route("/api/treasures", methods=['GET', 'POST'])
def treasures():
    if request.method =="GET":
        return treasure.get_treasures()
    if request.method=="POST":
        body = request.get_json()
        return treasure.post_treasure(body)

@app.route("/api/treasures/<treasure_id>", methods=['GET',"DELETE"])
def treasure_by_id(treasure_id):
    is_valid = re.search("^[0-9]$",treasure_id)
    if not is_valid:
        return {"message":"id not valid"}, 404
    if request.method =="GET":
        return treasure.get_treasure_by_id(treasure_id)
    if request.method =="DELETE":
        return treasure.delete_treasure(treasure_id)