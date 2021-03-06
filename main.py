from flask import Flask, request, abort
import csv
import sys
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

def main():
    word_data = pd.read_csv("word.csv").values.tolist()
    target_word = random.choice(word_data)

    messages = TextSendMessage(text=target_word[0])
    line_bot_api.push_message(my_user_id, messages=messages)

    messages = TextSendMessage(text=target_word[1])
    line_bot_api.push_message(my_user_id, messages=messages)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

if __name__ == "__main__":
    main()
