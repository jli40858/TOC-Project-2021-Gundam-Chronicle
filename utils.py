import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_yes_no_button(id, template):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, template)

    return "OK"


def send_img(id, target):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, ImageSendMessage(original_content_url=target, preview_image_url=target))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
