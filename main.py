from flask import Flask, request
import models.treasures_model as treasure
import models.shops_model as shops

app = Flask(__name__)

@app.route("/")
def home():
    return '''<p>Treasures API</p>
            <p>Endpoints available: </p>
            <p>GET: /api/treasures</p>
            <p>POST: /api/treasures - takes request in format (treasure_name, colour, age, cost_at_auction, shop_id)</p>
            <p>GET: /api/treasures/<treasure_id></p>
            <p>DELETE: /api/treasures/<treasure_id></p>
            <p>GET: /api/shops queries available - order by ASC/DESC</p>
            <p>GET: /api/shops/<shop_id> </p>
            <p>PATCH: /api/shops/<shop_id> Can update slogan -body example {"slogan": "new-slogan"}
            </p>
            <p>GET: /api/treasures/shops/<shop_id> </p>
            '''

@app.route("/api/shops")
def all_shops():
    if request.method=="GET":
        order = request.args.get("order")
        return shops.get_shops(order)

@app.route("/api/shops/<int:shop_id>", methods=['GET',"PATCH"] )
def shop_by_id(shop_id):
    if request.method=="GET":
        return shops.get_shop_by_id(str(shop_id))
    if request.method =="PATCH":
        body = request.get_json()
        return shops.update_shop(str(shop_id), body)
    
@app.route("/api/treasures/shops/<int:shop_id>")
def treasures_by_shop(shop_id):
    if request.method=="GET":
        return treasure.get_treasures_by_shop(str(shop_id))
    
@app.route("/api/treasures", methods=['GET', 'POST'])
def treasures():
    if request.method =="GET":
        return treasure.get_treasures()
    if request.method=="POST":
        body = request.get_json()
        return treasure.post_treasure(body)

@app.route("/api/treasures/<int:treasure_id>", methods=['GET',"DELETE"])
def treasure_by_id(treasure_id):
    if request.method =="GET":
        return treasure.get_treasure_by_id(str(treasure_id))
    if request.method =="DELETE":
        return treasure.delete_treasure(str(treasure_id))