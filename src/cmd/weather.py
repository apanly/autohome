# -*- coding: utf-8 -*-
import requests, hashlib, urllib, json

# from cmd.weather import Weather
# target = Weather('上海')
# target.get()

class Weather:
    def __init__(self,city):
        self.ak = "721lCBGTp217nYZ5DLAuzCob"
        self.sk = "rHtM1RS581VBYNOiC3j8GpEVb3qtihkL"
        self.domain = "http://api.map.baidu.com"
        self.city = city
        self.url = "/telematics/v3/weather"

    def get(self):
        sn = self.caculateAKSN()
        weather_url = '%s%s?location=%s&output=json&ak=%s&sn=%s'%(self.domain,self.url,self.city,self.ak,sn)
        r = requests.get(weather_url)
        data = json.loads(r.content)
        if data['error'] == 0:
            pm25 = data['results'][0]['pm25']
            weather = data['results'][0]['weather_data']
            print 'PM2.5:%s'%pm25
            for item in weather:
                print '----------------'
                print '日期:%s'%item['date']
                print '温度:%s'%item['temperature']
                print '风速:%s'%item['wind']
                print '天气:%s'%item['weather']

    def caculateAKSN(self):
        querystring = "location=%s&output=json&ak=%s"%(urllib.quote_plus(self.city), self.ak)
        sn = '%s?%s%s'%(self.url,querystring,self.sk)
        sn = urllib.quote_plus(sn)
        return hashlib.md5(sn.encode('utf-8')).hexdigest()
