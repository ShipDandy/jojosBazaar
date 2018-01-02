from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "cranston"

@app.route("/bazaar", methods=["GET"])
def bazaar_export_orders():
    if request.args['action'] == "export":
        username = request.args['SS-UserName']
        password = request.args['SS-Password']
        action = request.args['action']
        startDate = request.args['start_date']
        endDate = request.args['end_date']
        page = request.args['page']

        if username == 'mango' and password == "papaya":
            return "Hi Mango", 200
        else:
            return "You are no Mango!", 401
    else:
        return "Me no understand", 400

@app.route("/bazaar", methods=["POST"])
def bazaar_import_orders():
    pass

app.run(debug=True)

#comment