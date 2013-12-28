#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import time
import re
import httplib
import json
import urllib
import urllib2
import cookielib
 
class Huobi():
    (TRADE_BUY, TRADE_SELL) = range(2)
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cookie_jar = cookielib.CookieJar()
        self.url_handlers = [
            urllib2.HTTPSHandler(debuglevel=1),
            urllib2.HTTPCookieProcessor(self.cookie_jar),
        ]

        self.url_opener = urllib2.build_opener(*self.url_handlers)
        body = urllib.urlencode({'@email': self.email, '@password': self.password})
        request = urllib2.Request("https://www.huobi.com/account/login.php", body)
        headers = {
            "Connection":"keep-alive",
            "Host":"www.huobi.com",
            "Origin":"https://www.huobi.com",
            "Referer":"https://www.huobi.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
        }
        for (k, v) in headers.iteritems():
            request.add_header(k, v)
        resp = self.url_opener.open(request)
 
    def buy(self, price, amount):
        return self.trade(self.TRADE_BUY, price, amount)
        
    def sell(self, price, amount):
        return self.trade(self.TRADE_SELL, price, amount)
    
    def trade(self, trade_type, price, amount):
        trade_type_str = ""
        if trade_type == self.TRADE_BUY:
            trade_type_str = "do_buy"
        else:
            trade_type_str = "do_sell"
        body = urllib.urlencode({'@a': trade_type_str, '@price': price, '@amount': amount})
        request = urllib2.Request("https://www.huobi.com/trade/index.php", body)
        headers = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Connection":"keep-alive",
            "Host":"www.huobi.com",
            "Origin":"https://www.huobi.com",
            "Referer":"https://www.huobi.com/trade/index.php",
            "X-Requested-With":"XMLHttpRequest",
            "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
        }
        for (k, v) in headers.iteritems():
            request.add_header(k, v)
            
        resp = self.url_opener.open(request)
        print(resp.read())
        
    def get_account_info(self, post_data={}):
        pass
 
    def get_market_depth(self, post_data={}):
        pass

    def cancel(self, order_id, post_data={}):
        pass
 
    def get_orders(self, id=None, open_only=True, post_data={}):
        pass

