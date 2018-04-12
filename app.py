from flask import Flask, request, send_file, jsonify
from fakeDB import sampleOrder, sampleOrderUpdate
import logging

logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(levelname)s:%(asctime)s: %(message)s")

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to your website!"

@app.route("/bazaar", methods=["GET"])
def bazaar_export_orders():
    logging.info("Import request from: " + request.remote_addr)
    logging.info("Arguments included: " + str(request.args))

    try:
        username = request.args['SS-UserName']
        password = request.args['SS-Password']
        action = request.args['action']
        startDate = request.args['start_date']
        endDate = request.args['end_date']
        page = request.args['page']
    except Exception:
        return jsonify({"message": "Expected Parameters not received."}), 400

    if username != 'mango' or password != 'papaya':
        return jsonify({"message": "Authorization failed."}), 401

    return sampleOrder, 200
        


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

    if username != 'mango' or password != 'papaya':
        return jsonify({"message": "Authorization failed."}), 401

    if request.args['service']:
        carrierService = request.args['service']
    else:
        carrierService = "marked_as_shipped"

    sampleOrderUpdate = str(request.data)

    return jsonify({"message": "Shipment notification received."}), 200

"""Endpoint on site from which log files can be downloaded"""
@app.route("/postlogs", methods=["GET"])
def view_post_logs():
    # html_response = ""

    # with open("logfile.log") as readlogs:
    #     for line in readlogs:
    #         html_response += "<p>{}</p>".format(line)

    # return html_response
    return send_file("logfile.log", as_attachment=True)


if __name__ == '__main__':
    app.run()

"""Runs app as a local Flask server for testing"""
# app.run(port=5000, debug=True)

