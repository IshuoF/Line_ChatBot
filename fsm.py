from transitions.extensions import GraphMachine
import os
import sys

import requests
import json
import random
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

import globals 
import template
from utils import send_text_message
load_dotenv()
google_key = os.getenv("GOOGLE_API_KEY", None)
findbar_menu=[]
contents=dict()
contents['type']='carousel'
def findbars():
    barsaerch = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={google_key}&location={globals.global_latitude},{globals.global_longitude}&radius=1000&keyword=酒吧&&language=zh-TW'

    barreq = requests.get(barsaerch)
    nearby_bar_dict = barreq.json()
    bar20 = nearby_bar_dict["results"]
    bar_num = (len(bar20))
    print(bar_num)
    bravo=[]
    for i in range(bar_num):
        try:
            if bar20[i]['rating'] >4.6:
                print('rate : ',bar20[i]['rating'])
                bravo.append(i)
        except:
            KeyError
    
    for i in range(3):
        bar = bar20[random.choice(bravo)]

        if bar.get("photos") is None:
            image_url = None
        else:
            photo_ref = bar["photos"][0]["photo_reference"]
            photo_width =  bar["photos"][0]["width"]
            image_url = f'https://maps.googleapis.com/maps/api/place/photo?key={google_key}&photoreference={photo_ref}&maxwidth={photo_width}'
            
        rating= "無" if bar.get("rating") is None else bar["rating"]
        address = "沒有資料"  if bar.get("vicinity") is None else bar["vicinity"]   
        details_rating = f"Google Map評分 : {rating}\n"
        details__address = f"地址 : {address}\n"
        bar_name = bar["name"]
        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": f"{image_url}",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "fit"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": f"{bar_name}",
                        "size": "xl"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": f"{details_rating}",
                        "size": "md"
                    },
                    {
                        "type": "text",
                        "text": f"{details__address}",
                        "size": "md"
                    }
                    ]
                }
                ]
            }
        }
            
        
        findbar_menu.append(bubble)
        print(bar_name+"\n"+details_rating+"\n"+details__address)
    return_menu = {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://img.88icon.com/download/jpg/20200905/38bf50ca892b3be864c8f9abfcc3cf8b_512_512.jpg!88con",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": []
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "快速叫車",
              "text": "快速叫車"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "返回主選單",
                  "text": "返回主選單"
                }
              }
            ]
          }
        ]
      }
    }
    findbar_menu.append(return_menu)
    contents['contents']= findbar_menu
    message = FlexSendMessage("找酒吧",contents=contents)
    return message

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
        message = template.get_location
        message_to_reply = FlexSendMessage("取得位置", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)  
        
    def on_enter_findbar(self, event):
        reply_token = event.reply_token
        message_to_reply = findbars()
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)    
    
    
    def on_enter_taxi(self, event):
        reply_token = event.reply_token
        message = template.Taxi_menu
        message_to_reply = FlexSendMessage("快速叫車", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
          