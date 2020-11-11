from flask import Flask, request, abort
import csv
import random
import re
import pandas as pd
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

LINE_BOT_API = os.environ["LINE_BOT_API"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
MY_USER_ID = os.environ["MY_USER_ID"]
line_bot_api = LineBotApi(LINE_BOT_API)
handler = WebhookHandler(CHANNEL_SECRET)
my_user_id = MY_USER_ID

from main import *
@handler.add(MessageEvent, message=TextMessage)
def handle_message2(event):
    if event.message.text == "おかわり" or event.message.text == "お":
        main()
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="ちょっと何言ってるかわかんないです"))

if __name__ == "__main__":
    app.run()