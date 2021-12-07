from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('ZRjyjNwSVRqlhznKRP7Ls7IUV8pgmyUxdGnBGMfEf6teuPM+qtWQg8BuOwnsUUAEC6h7RRTRssYO4Gt2NguYF7etzhJiU0JBWZdfdAbIkFxHalnIumMN/8710BIrVnn3Xj7NxjcHkbq8I8b20s36VQdB04t89/1O/w1cDnyilFU=')

try:
    line_bot_api.push_message('Ua8dbc2f97b9014c36aac262f1a8bd285', TextSendMessage(text='Train เสร็จแล้ว ไอ้สัส !!'))
except LineBotApiError as e:
    # error handle
    ...