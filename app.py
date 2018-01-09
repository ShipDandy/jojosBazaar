from flask import Flask, request, send_file
from deliver import xmlSample
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
    logging.info("Connecting from: " + request.remote_addr)
    logging.info(str(request.data))
    return "Hello!"

@app.route("/postlogs")
def view_post_logs():
    open_log = open("logfile.log", "r")
    log_info = str(open_log.read())
    open_log.close()
    # return {"logs": log_info}
    return send_file("logfile.log")

if __name__ == '__main__':
    app.run(port=5000)

#comment