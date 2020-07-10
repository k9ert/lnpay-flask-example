from flask import Flask, request, redirect, current_app
from random import randrange
import json

app = Flask(__name__)

paywall_link="https://paywall.link/to/548b9"

# This is where we're remembering "users" or maybe better requests
app.requests = {}

@app.route('/')
def hello_world():
    print(randrange(10))
    if request.cookies.get("requestid") == None:
        print("No cookie! Setting cookie and redirect to paywall!")
        request_id = str(randrange(10000)) # random integer
        resp = redirect(paywall_link+"?userId="+request_id)
        resp.set_cookie("requestid", value=request_id)
        current_app.requests[request_id] = False # haven't paid yet
        return resp
    else:
        # check whether the user has paid
        if current_app.requests.get(request.cookies.get("test")):
            print("User has paid, all fine!")
            return 'Hello, World!'
        else:
            return 'sorry, you have not paid yet. Consider a reload!'

@app.route('/webhook',methods=["POST"])
def lnpay_webhook():
    myjson = request.json
    print(str(myjson))
    request_id = myjson["data"]["wtx"]["passThru"]["userId"]
    if request_id in current_app.requests:
        current_app.requests[request_id] = True
        print("request_ID {} paid!".format(request_id))
    print("request:"+str(myjson))
    return "ok"