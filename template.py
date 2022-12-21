main_menu = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.grandcosmos.com.tw/wp-content/uploads/sites/214/2017/11/%E7%91%9E%E7%A9%97%E6%98%A5%E5%A4%A9%E5%9C%8B%E9%9A%9B%E8%A7%80%E5%85%89%E9%85%92%E5%BA%97-A%E6%A3%9F%E5%9F%8E%E5%A0%A1-%E5%A4%A7%E5%BB%B3%E9%85%92%E5%90%A7-2.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "MENU",
        "size": "xl",
        "weight": "bold",
        "align": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "介紹與說明",
              "text": "功能介紹與說明"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "找酒吧",
              "text": "取得位置"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "來點特調",
              "text": "自己調"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "快速叫車",
              "text": "快速叫車"
            }
          }
        ],
        "action": {
          "type": "message",
          "label": "介紹與說明",
          "text": "主選單"
        }
      }
    ]
  }
}

intro_menu ={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "功能介紹",
        "size": "3xl",
        "weight": "bold",
        "align": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "提供想喝酒的朋友方便的小幫手",
            "size": "md"
          },
          {
            "type": "text",
            "text": "● 為你推薦鄰近的酒吧",
            "size": "md"
          },
          {
            "type": "text",
            "text": "● 當想動動手時也能自己調酒"
          },
          {
            "type": "text",
            "text": "● 喝醉了也可以馬上幫你叫車"
          }
        ]
      },
      {
        "type": "text",
        "text": "使用說明",
        "size": "3xl",
        "weight": "bold",
        "align": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "輸入「主選單」來開始所有操作，",
            "size": "md",
            "wrap": True
          },
          {
            "type": "text",
            "text": "依照按鈕提示進行點選即可",
            "size": "md",
            "wrap": True
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "margin": "xxl",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "返回主選單"
        }
      }
    ]
  }
}

select_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "url": "https://images.chinatimes.com/newsphoto/2021-01-20/656/20210120006098.jpg",
        "margin": "none",
        "offsetTop": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "none",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "label": "高濃度",
              "text": "濃度高"
            },
            "height": "md",
            "color": "#876D5A",
            "offsetTop": "none"
          }
        ]
      },
      "styles": {
        "body": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNNpUvFo269SEf_m_TxNsEk7xz3QTjG1799oqq_3sXhCEVx_6N-8p5JprCpqr5LoorDs0&usqp=CAU",
        "margin": "none",
        "offsetTop": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "none",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "label": "普通濃度",
              "text": "濃度中"
            },
            "height": "md",
            "color": "#876D5A",
            "offsetTop": "none"
          }
        ]
      },
      "styles": {
        "body": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "url": "https://static.wikia.nocookie.net/bahapedia/images/e/ef/025c3937969d2ff9591374cb6dcd0cad.JPG/revision/latest?cb=20180806122947&path-prefix=zh",
        "margin": "none",
        "offsetTop": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "none",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "message",
              "label": "低濃度",
              "text": "濃度低"
            },
            "height": "md",
            "color": "#876D5A",
            "offsetTop": "none"
          }
        ]
      },
      "styles": {
        "body": {
          "separator": False
        }
      }
    }
  ]
}

select_high = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://assets.juksy.com/files/articles/91190/800x_100_w-6268ea3e70798.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Zombie",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "高濃度蘭姆酒",
                    "wrap": True,
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "白蘭姆酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "45 ml",
                    "size": "sm"
                  }
                ],
                "flex": 5
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "香料蘭姆酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "20 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "費勒南糖漿",
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "15 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "現榨鳳梨汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "60 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "現榨葡萄柚汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "15 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "現榨檸檬汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "15 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "法式茴香酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "4 drop",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "紅石榴糖漿",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "1 tsp",
                    "size": "sm"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "作法:",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "１．雪克杯加入所有材料及冰塊，搖盪均勻。",
                "size": "xs"
              },
              {
                "type": "text",
                "text": " ２．濾掉冰塊，將酒液倒入颶風或Tiki杯。",
                "size": "xs"
              }
            ],
            "height": "50px"
          }
        ],
        "height": "150px"
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://attach.setn.com/newsimages/2015/09/03/330809.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Adios MotherFucker",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "高濃度蘭姆酒",
                    "wrap": True,
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "40 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "琴酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "40 ml",
                    "size": "sm"
                  }
                ],
                "flex": 5
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "龍舌蘭",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "40 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "伏特加",
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "40 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "藍色香甜酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "15 ml"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "蘇打水",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "20 ml"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "作法:",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "１．杯中倒入藍柑糖漿及冰塊準備",
                "size": "xs"
              },
              {
                "type": "text",
                "text": " ２．其他材料倒入雪克杯與冰塊高速搖盪",
                "size": "xs"
              },
              {
                "type": "text",
                "text": "再緩緩注入杯中，才有美麗的漸層效果。",
                "size": "xs"
              }
            ]
          }
        ],
        "height": "150px"
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://robbreport.com/wp-content/uploads/2022/08/GettyImages_Long_Island_Iced_Tea.jpg?w=1000",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Long Island Iced Tea",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "伏特加",
                    "wrap": True,
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "琴酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ],
                "flex": 5
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "龍舌蘭",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "蘭姆酒",
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "柑橘酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "現榨檸檬汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "作法:",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "１．所有酒類素材、檸檬汁通通丟進雪克杯裡加冰用力搖",
                "size": "xs"
              },
              {
                "type": "text",
                "text": " ２．加入少許可樂上色",
                "size": "xs"
              }
            ],
            "height": "50px"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://img.ixintu.com/upload/jpg/20210523/aac53c5976caaabcf6e6c69e7e2a7287_8936_512_512.jpg!ys",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回選擇濃度",
              "text": "返回選擇濃度"
            }
          }
        ]
      },
      "footer": {
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
    }
  ]
}

select_med = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://cocktail4party.com/wp-content/uploads/2021/10/cosmopolitan-cocktail-3.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Cosmopolitan",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "伏特加",
                    "wrap": True,
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "45 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "蔓越莓汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "60 ml",
                    "size": "sm"
                  }
                ],
                "flex": 5
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "現榨葡萄柚汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "60 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "通寧水",
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "作法:",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "１．以搖盪法調製，搖盪完成後到入馬丁尼杯。",
                "size": "xs"
              },
              {
                "type": "text",
                "text": " ２．附柑橘和檸檬皮油作為裝飾。",
                "size": "xs"
              }
            ],
            "height": "50px"
          }
        ],
        "height": "150px"
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://i0.wp.com/cocktail4party.com/wp-content/uploads/2021/10/Bay-Breeze-Cocktail-7.jpg?fit=1000%2C821&ssl=1",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Sea Breeze",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "伏特加",
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "20 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "蘭姆酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "20 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "藍柑橘酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "15 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "鳳梨汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "90 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "酸甜汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "作法:",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "1．颶風杯盛裝並補滿碎冰，放上鳳梨",
                "size": "xs"
              },
              {
                "type": "text",
                "text": "2．將酒液倒入威士忌杯，加入冰塊。",
                "size": "xs"
              },
              {
                "type": "text",
                "text": "3．再加入通寧水至滿杯，稍加攪拌。",
                "size": "xs"
              }
            ]
          }
        ],
        "height": "150px"
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://d3u2gohddm28e7.cloudfront.net/wp-content/uploads/2021/10/8638464113_63e36da7a4_b.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Blue Hawaii",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "蘭姆酒",
                    "wrap": True,
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "20 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "伏特加",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "20 ml",
                    "size": "sm"
                  }
                ],
                "flex": 5
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "藍柑橘酒",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "15 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "鳳梨汁",
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "90 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "酸甜汁",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "30 ml",
                    "size": "sm"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "作法:",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "１．颶風杯盛裝並補滿碎冰，放上鳳梨",
                "size": "xs"
              }
            ],
            "height": "50px"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://img.ixintu.com/upload/jpg/20210523/aac53c5976caaabcf6e6c69e7e2a7287_8936_512_512.jpg!ys",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回選擇濃度",
              "text": "返回選擇濃度"
            }
          }
        ]
      },
      "footer": {
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
    }
  ]
}

select_low ={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://tokyo-kitchen.icook.network/uploads/recipe/cover/421743/8cd355b03485f681.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "蜂蜜檸檬沙瓦+冷凍芒果",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "蜂蜜檸檬口味的沙瓦",
                    "wrap": True,
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "500 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "冷凍芒果",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "數顆",
                    "size": "sm"
                  }
                ],
                "flex": 5
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/img-1211-png-1617794015.png?crop=1xw:1xh;center,top&resize=480:*",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "養樂多沙瓦+低糖優格",
            "weight": "bold",
            "size": "lg",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "養樂多沙瓦",
                    "wrap": True,
                    "size": "sm",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "500 ml",
                    "size": "sm"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "低糖優格",
                    "flex": 5,
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "20 ml",
                    "size": "sm"
                  }
                ],
                "flex": 5
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://img.ixintu.com/upload/jpg/20210523/aac53c5976caaabcf6e6c69e7e2a7287_8936_512_512.jpg!ys",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回選擇濃度",
              "text": "返回選擇濃度"
            }
          }
        ]
      },
      "footer": {
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
    }
  ]
}

recommend_menu = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Store",
        "weight": "bold",
        "size": "xxl",
        "margin": "md",
        "action": {
          "type": "message",
          "label": "storename",
          "text": " "
        }
      },
      {
        "type": "text",
        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
        "size": "xs",
        "color": "#aaaaaa",
        "wrap": True,
        "action": {
          "type": "message",
          "label": "address",
          "text": " "
        }
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Energy Drink",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$2.99",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Chewing Gum",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$0.99",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Bottled Water",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$3.33",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
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
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}