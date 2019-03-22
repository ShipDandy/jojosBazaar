from flask import Flask, request, send_file, jsonify
from fakeDB import sampleOrder, sampleOrderUpdate # in place of a database we will use this python file with a pre-composed order.
import logging

import settings
import services as se

"""When developing custom endpoints having logging capture incoming information from ShipStation in invaluable."""
logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(levelname)s:%(asctime)s: %(message)s")

app = Flask(__name__)

"""This endpoint represents the public-facing side of your system if there is one."""
@app.route("/")
def home():
    return "Welcome to your website!"

"""An idempotent endpoint set up to communicate order information with ShipStation. GET requests for orders created or modified between the startDate and endDate parameters sent as part of a string query sent from ShipStation."""
@app.route("/bazaar", methods=["GET"])
def bazaar_export_orders():
    logging.info("Import request from: " + request.remote_addr)
    logging.info("Arguments included: " + str(request.args))

    # extract values passed in the string parameters of the GET request from ShipStation.
    try:
        username = request.args['SS-UserName']
        password = request.args['SS-Password']
        action = request.args['action']
        startDate = request.args['start_date']
        endDate = request.args['end_date']
        page = request.args['page']
    except Exception:
        return jsonify({"message": "Expected Parameters not received."}), 400 # useful check that all parameters are being sent when mocking your own calls for testing purposes.

    # After successful authorization you would normally take the startDate and endDate and query your database for new/updated orders to pass back as XML. If you needed to send you orders over multiple pages you would also take advantage of the page value passed along. For this example we simply contact our fakeDB.py file for our response.

    if se.authorizeCreds(username, password):
        return sampleOrder, 200
    else:
        return jsonify({"message": "Authorization failed."}), 401

    
    
        

"""An idempotent endpoint set up to receive updated order information from ShipStation. POST requests pass along shipping information for orders including carrier used as well as tracking numbers."""
@app.route("/bazaar", methods=["POST"])
def bazaar_ship_notify():
    logging.info("Notification from: " + request.remote_addr)
    logging.info("Arguements included: " + str(request.args))
    logging.info(str(request.data))

    try:
        username = request.args['SS-UserName']
        password = request.args['SS-Password']
        action = request.args['action']
        orderNumber = request.args['order_number']
        carrier = request.args['carrier']
        trackingNumber = request.args['tracking_number']
    except Exception:
        return jsonify({"message": "Expected Parameters not received."}), 400

    if se.authorizeCreds(username, password):
        pass
    else:
        return jsonify({"message": "Authorization failed."}), 401

    # The carrier service selected when a label is generated in ShipStation will be passed along, if an order was marked as shipped either in app or via API a value will not be passed in the string parameter.
    if request.args['service']:
        carrierService = request.args['service']
    else:
        carrierService = "marked_as_shipped"

    # In production you would ingest information from the string paramters passed and/or the accompanying XML data passed back to update the order's entry in your database, for this example simply send it back to fakeDB.py.
    sampleOrderUpdate = str(request.data)

    return jsonify({"message": "Shipment notification received."}), 200

"""Endpoint on site from which log files can be downloaded."""
@app.route("/getlogs", methods=["GET"])
def download_logs():    
    return send_file("logfile.log", as_attachment=True, attachment_filename="logfile.log")

"""Provides an in browser view of logs, helpful when hosting on ephmeral filesystems like Heroku."""
@app.route("/logs", methods=["GET"])
def view_logs():
    html_response = ""

    with open("logfile.log") as readlogs:
        for line in readlogs:
            html_response += "<p>{}</p>".format(line)

    return html_response


# if __name__ == '__main__':
#     app.run()

"""Runs app on a local Flask server for testing"""
app.run(port=5000, debug=True)
