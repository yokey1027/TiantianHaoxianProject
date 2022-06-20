# -*- coding: utf-8 -*-
SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False

#有可能你使用浏览器看到的一串字符串不是那么容易看懂的，这是因为python底层使用unicode编码。
#通过设置下面的参数可以解决这个问题。
JSON_AS_ASCII = False

AUTH_COOKIE_NAME = "mooc_food"

SEO_TITLE = "@天天好鲜-"
##过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

MINA_APP = {
    'appid':'wxc6413801f88825b2',
    'appkey':'6c05e17e72f898d14ec54532729d6db7',
    'paykey':'cs89SK8ndf39gjcv87hifIjf23n4bd9j',
    'mch_id':'1624187916',
    'callback_url':'/api/order/callback'
}


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    # 'domain':'http://10.0.82.202:8999'
    # 'domain':'http://10.3.99.195:8999'
    'domain':'http://10.3.97.228:8999'
}


PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待收货",
    "-5":"待评价"
}