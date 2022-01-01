import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()
machine = {}
app = Flask(__name__, static_url_path="")

machine = TocMachine(
    states=["page1", "page2", "page3",
            "page1_menu", "page2_menu", "page3_menu",
            "state0079", "state0083", "state0087",
            "state0088", "state0093", "state0096",
            "state0123", "state0133", "state0153",
            "state0079_main", "state0079_rival", "state0079_menu",
            "state0083_main", "state0083_rival", "state0083_menu",
            "state0087_main", "state0087_rival", "state0087_menu",
            "state0088_main", "state0088_rival", "state0088_menu",
            "state0093_main", "state0093_rival", "state0093_menu",
            "state0096_main", "state0096_rival", "state0096_menu",
            "state0123_main", "state0123_rival", "state0123_menu",
            "state0133_main", "state0133_rival", "state0133_menu",
            "state0153_main", "state0153_rival", "state0153_menu",
            ],
    transitions=[
        {"trigger": "advance", "source": "page1", "dest": "page2", "conditions": "is_going_to_page2", },
        {"trigger": "advance", "source": "page2", "dest": "page3", "conditions": "is_going_to_page3", },
        {"trigger": "advance", "source": "page3", "dest": "page1", "conditions": "is_going_back_to_page1", },
        {"trigger": "advance", "source": "page1", "dest": "state0079", "conditions": "is_going_to_state0079", },
        {"trigger": "advance", "source": "page1", "dest": "state0083", "conditions": "is_going_to_state0083", },
        {"trigger": "advance", "source": "page1", "dest": "state0087", "conditions": "is_going_to_state0087", },
        {"trigger": "advance", "source": "page1", "dest": "page1_menu", "conditions": "is_going_to_page1_menu", },
        {"trigger": "advance", "source": "page2", "dest": "state0088", "conditions": "is_going_to_state0088", },
        {"trigger": "advance", "source": "page2", "dest": "state0093", "conditions": "is_going_to_state0093", },
        {"trigger": "advance", "source": "page2", "dest": "state0096", "conditions": "is_going_to_state0096", },
        {"trigger": "advance", "source": "page2", "dest": "page2_menu", "conditions": "is_going_to_page2_menu", },
        {"trigger": "advance", "source": "page3", "dest": "state0123", "conditions": "is_going_to_state0123", },
        {"trigger": "advance", "source": "page3", "dest": "state0133", "conditions": "is_going_to_state0133", },
        {"trigger": "advance", "source": "page3", "dest": "state0153", "conditions": "is_going_to_state0153", },
        {"trigger": "advance", "source": "page3", "dest": "page3_menu", "conditions": "is_going_to_page3_menu", },

        {
            "trigger": "advance",
            "source": "state0079",
            "dest": "state0079_main",
            "conditions": "is_going_to_state0079_main",
        },
        {
            "trigger": "advance",
            "source": "state0079",
            "dest": "state0079_rival",
            "conditions": "is_going_to_state0079_rival",
        },
        {
            "trigger": "advance",
            "source": "state0079",
            "dest": "state0079_menu",
            "conditions": "is_going_to_state0079_menu",
        },
        {
            "trigger": "advance",
            "source": "state0083",
            "dest": "state0083_main",
            "conditions": "is_going_to_state0083_main",
        },
        {
            "trigger": "advance",
            "source": "state0083",
            "dest": "state0083_rival",
            "conditions": "is_going_to_state0083_rival",
        },
        {
            "trigger": "advance",
            "source": "state0083",
            "dest": "state0083_menu",
            "conditions": "is_going_to_state0083_menu",
        },
        {
            "trigger": "advance",
            "source": "state0087",
            "dest": "state0087_main",
            "conditions": "is_going_to_state0087_main",
        },
        {
            "trigger": "advance",
            "source": "state0087",
            "dest": "state0087_rival",
            "conditions": "is_going_to_state0087_rival",
        },
        {
            "trigger": "advance",
            "source": "state0087",
            "dest": "state0087_menu",
            "conditions": "is_going_to_state0087_menu",
        },
        {
            "trigger": "advance",
            "source": "state0088",
            "dest": "state0088_main",
            "conditions": "is_going_to_state0088_main",
        },
        {
            "trigger": "advance",
            "source": "state0088",
            "dest": "state0088_rival",
            "conditions": "is_going_to_state0088_rival",
        },
        {
            "trigger": "advance",
            "source": "state0088",
            "dest": "state0088_menu",
            "conditions": "is_going_to_state0088_menu",
        },
        {
            "trigger": "advance",
            "source": "state0093",
            "dest": "state0093_main",
            "conditions": "is_going_to_state0093_main",
        },
        {
            "trigger": "advance",
            "source": "state0093",
            "dest": "state0093_rival",
            "conditions": "is_going_to_state0093_rival",
        },
        {
            "trigger": "advance",
            "source": "state0093",
            "dest": "state0093_menu",
            "conditions": "is_going_to_state0093_menu",
        },
        {
            "trigger": "advance",
            "source": "state0096",
            "dest": "state0096_main",
            "conditions": "is_going_to_state0096_main",
        },
        {
            "trigger": "advance",
            "source": "state0096",
            "dest": "state0096_rival",
            "conditions": "is_going_to_state0096_rival",
        },
        {
            "trigger": "advance",
            "source": "state0096",
            "dest": "state0096_menu",
            "conditions": "is_going_to_state0096_menu",
        },
        {
            "trigger": "advance",
            "source": "state0123",
            "dest": "state0123_main",
            "conditions": "is_going_to_state0123_main",
        },
        {
            "trigger": "advance",
            "source": "state0123",
            "dest": "state0123_rival",
            "conditions": "is_going_to_state0123_rival",
        },
        {
            "trigger": "advance",
            "source": "state0123",
            "dest": "state0123_menu",
            "conditions": "is_going_to_state0123_menu",
        },
        {
            "trigger": "advance",
            "source": "state0133",
            "dest": "state0133_main",
            "conditions": "is_going_to_state0133_main",
        },
        {
            "trigger": "advance",
            "source": "state0133",
            "dest": "state0133_rival",
            "conditions": "is_going_to_state0133_rival",
        },
        {
            "trigger": "advance",
            "source": "state0133",
            "dest": "state0133_menu",
            "conditions": "is_going_to_state0133_menu",
        },
        {
            "trigger": "advance",
            "source": "state0153",
            "dest": "state0153_main",
            "conditions": "is_going_to_state0153_main",
        },
        {
            "trigger": "advance",
            "source": "state0153",
            "dest": "state0153_rival",
            "conditions": "is_going_to_state0153_rival",
        },
        {
            "trigger": "advance",
            "source": "state0153",
            "dest": "state0153_menu",
            "conditions": "is_going_to_state0153_menu",
        },
        {"trigger": "go_back", "source": "page1_menu", "dest": "page1"},
        {"trigger": "go_back", "source": "page2_menu", "dest": "page2"},
        {"trigger": "go_back", "source": "page3_menu", "dest": "page3"},
        {"trigger": "go_back", "source": ["state0079_main", "state0079_rival", "state0079_menu"], "dest": "state0079"},
        {"trigger": "go_back", "source": ["state0083_main", "state0083_rival", "state0083_menu"], "dest": "state0083"},
        {"trigger": "go_back", "source": ["state0087_main", "state0087_rival", "state0087_menu"], "dest": "state0087"},
        {"trigger": "go_back", "source": ["state0088_main", "state0088_rival", "state0088_menu"], "dest": "state0088"},
        {"trigger": "go_back", "source": ["state0093_main", "state0093_rival", "state0093_menu"], "dest": "state0093"},
        {"trigger": "go_back", "source": ["state0096_main", "state0096_rival", "state0096_menu"], "dest": "state0096"},
        {"trigger": "go_back", "source": ["state0123_main", "state0123_rival", "state0123_menu"], "dest": "state0123"},
        {"trigger": "go_back", "source": ["state0133_main", "state0133_rival", "state0133_menu"], "dest": "state0133"},
        {"trigger": "go_back", "source": ["state0153_main", "state0153_rival", "state0153_menu"], "dest": "state0153"},

        {
            "trigger": "advance",
            "source": ["state0079", "state0083", "state0087"],
            "dest": "page1",
            "conditions": "is_going_back_page1",
        },
        {
            "trigger": "advance",
            "source": ["state0088", "state0093", "state0096"],
            "dest": "page2",
            "conditions": "is_going_back_page2",
        },
        {
            "trigger": "advance",
            "source": ["state0123", "state0133", "state0153"],
            "dest": "page3",
            "conditions": "is_going_back_page3",
        },
    ],
    initial="page1",
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

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "未定義操作，請輸入「選單」以開啟輸入選項")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
