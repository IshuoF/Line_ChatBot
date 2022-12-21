from transitions.extensions import GraphMachine

import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

import template
from utils import send_text_message


load_dotenv()
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        
    def is_going_to_menu(self,event):
        text = event.message.text
        return text == "主選單"
    
    def is_going_to_backmenu(self,event):
        text = event.message.text
        return text == "返回主選單"
    
    def is_going_to_introduction(self, event):
        text = event.message.text
        return text == "功能介紹與說明"
    
    def is_going_to_getlocation(self,event):
        text = event.message.text
        return text == "取得位置"
    
    def is_going_to_findbar(self,event):
        text = event.message.text
        return text == "找酒吧"
    
    
    def is_going_to_select(self,event):
        text = event.message.text
        return text == "自己調"
    
    def is_going_to_select_high(self,event):
        text = event.message.text
        return text == "濃度高"
    
    def is_going_to_select_med(self,event):
        text = event.message.text
        return text == "濃度中"
    
    def is_going_to_select_low(self,event):
        text = event.message.text
        return text == "濃度低"
    
    def is_going_to_backselect(self,event):
        text = event.message.text
        return text == "返回選擇濃度"
    
    def is_going_to_diy_select(self,event):
        text = event.message.text
        return text == "選擇濃度"
    
    def is_going_to_taxi(self,event):
        text = event.message.text
        return text == "快速叫車"
    
    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = template.main_menu
        message_to_reply = FlexSendMessage("開啟主選單", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    def on_enter_introduction(self,event):
        reply_token = event.reply_token
        message = template.intro_menu
        message_to_reply = FlexSendMessage("功能介紹與說明", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()
        
    
    def on_enter_select(self, event):
        reply_token = event.reply_token
        message = template.select_menu
        message_to_reply = FlexSendMessage("選擇特調濃度", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
    
    def on_enter_select_high(self, event):
        reply_token = event.reply_token
        message = template.select_high
        message_to_reply = FlexSendMessage("選擇高濃度", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
        
    def on_enter_select_med(self, event):
        reply_token = event.reply_token
        message = template.select_med
        message_to_reply = FlexSendMessage("選擇普通濃度", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
        
    def on_enter_select_low(self, event):
        reply_token = event.reply_token
        message = template.select_low
        message_to_reply = FlexSendMessage("選擇低濃度", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    
    def on_enter_getlocation(self, event):
        reply_token = event.reply_token
        # message = template.select_high
        # message_to_reply = FlexSendMessage("選擇高濃度", message)
        # line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        # line_bot_api.reply_message(reply_token, message_to_reply)  
        
    def on_enter_findbar(self, event):
        reply_token = event.reply_token 
          
    def on_enter_findbar_book(self, event):
        reply_token = event.reply_token       
    
    def on_enter_taxi(self, event):
        reply_token = event.reply_token
          