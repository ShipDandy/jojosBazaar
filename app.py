from flask import Flask, request
from deliver import xmlSample

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
            return xmlSample, 200
        else:
            header("Content-type: text/xml")
            return "You are no authorize!", 401
    else:
        return "Me no understand", 400

@app.route("/bazaar", methods=["POST"])
def bazaar_import_orders():
    pass

if __name__ == '__main__':
    app.run()

#comment