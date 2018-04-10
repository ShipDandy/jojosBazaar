from flask import Flask, request, send_file, jsonify
from fakeDB import xmlSample
import logging

logging.basicConfig(filename="logfile.log", level=logging.DEBUG, format="%(levelname)s:%(asctime)s: %(message)s")

app = Flask(__name__)

# @app.before_request
# def before_request():
#     if True:
#         print("HEADERS", request.headers)
#         print("REQ_path", request.path)
#         print("ARGS",request.args)
#         print("DATA",request.data)
#         print("FORM",request.form)

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

    return xmlSample, 200
        


@app.route("/bazaar", methods=["POST"])
def bazaar_import_orders():
    logging.info("Connecting from: " + request.remote_addr)
    logging.info("Arguments included: " + str(request.url))
    logging.info("Headers included: " + str(request.headers))
    logging.info(str(request.data))
    return "Hello!"

@app.route("/postlogs")
def view_post_logs():
    return send_file("logfile.log")

if __name__ == '__main__':
    app.run()

# app.run(port=5000)

