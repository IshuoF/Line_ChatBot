import os
import sys
import globals
from flask import Flask, jsonify, request, abort, send_file
import json
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,LocationMessage, LocationSendMessage
from fsm import TocMachine
from utils import send_text_message

load_dotenv()

global_latitude=0.0
global_longitude = 0.0

machine = TocMachine(
    states=["user", "menu", "introduction","getlocation","findbar",
            "select","select_high","select_med","select_low","taxi"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "introduction",
            "conditions": "is_going_to_introduction",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "getlocation",
            "conditions": "is_going_to_getlocation",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "select",
            "conditions": "is_going_to_select",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "taxi",
            "conditions": "is_going_to_taxi",
        },
        {
            "trigger": "advance",
            "source": "introduction",
            "dest": "menu",
            "conditions": "is_going_to_backmenu",
        },
        {
            "trigger": "advance",
            "source": "getlocation",
            "dest": "findbar",
            "conditions": "is_going_to_findbar",
        },
        {
            "trigger": "advance",
            "source": "findbar",
            "dest": "taxi",
            "conditions": "is_going_to_taxi",
        },
        {
            "trigger": "advance",
            "source": "findbar",
            "dest": "menu",
            "conditions": "is_going_to_backmenu",
        },
        {
            "trigger": "advance",
            "source": "select",
            "dest": "select_high",
            "conditions": "is_going_to_select_high",
        },
        {
            "trigger": "advance",
            "source": "select",
            "dest": "select_med",
            "conditions": "is_going_to_select_med",
        },
        {
            "trigger": "advance",
            "source": "select",
            "dest": "select_low",
            "conditions": "is_going_to_select_low",
        },
        {
            "trigger": "advance",
            "source": "select_high",
            "dest": "select",
            "conditions": "is_going_to_backselect",
        },
        {
            "trigger": "advance",
            "source": "select_med",
            "dest": "select",
            "conditions": "is_going_to_backselect",
        },
        {
            "trigger": "advance",
            "source": "select_low",
            "dest": "select",
            "conditions": "is_going_to_backselect",
        },
        {
            "trigger": "advance",
            "source": "select_high",
            "dest": "menu",
            "conditions": "is_going_to_backmenu",
        },
        {
            "trigger": "advance",
            "source": "select_med",
            "dest": "menu",
            "conditions": "is_going_to_backmenu",
        },
        {
            "trigger": "advance",
            "source": "select_low",
            "dest": "menu",
            "conditions": "is_going_to_backmenu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "taxi",
            "conditions": "is_going_to_taxi",
        },
        {
            "trigger": "advance",
            "source": "taxi",
            "dest": "menu",
            "conditions": "is_going_to_backmenu",
        },
        
        {"trigger": "go_back", "source": ["findbar",
            "select_high","select_med","select_low","taxi"], "dest": "menu"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    arr = body.split(',')
    if arr[4][:10] == '''"latitude"''':
        print(arr[4][11:])
        print(arr[5][12:])
        globals.global_latitude = float(arr[4][11:])
        globals.global_longitude = float(arr[5][12:])
        print(f' global_latitude : {globals.global_latitude}\n')
        print(f'global_longtitude : {globals.global_longitude}\n')
    
    
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: {body}")
        
        print(f"event : {event}")
        response = machine.advance(event)
        
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"
      

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

# show_fsm()

if __name__ == "__main__":
    globals.initialize()
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port, debug=True)
