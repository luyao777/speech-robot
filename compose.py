#coding: utf-8 
from aip import AipSpeech
from config import DefaultConfig as opt

class composer():
    def __init__(self):
        pass
    def compose(self,text ='你好'):
        #百度后台获取的秘�?
        APP_ID = opt.baidu_app_id
        API_KEY = opt.baidu_api_key
        SECRET_KEY =opt.baidu_secret_key
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = client.synthesis(text,'zh',1,{
                    'vol':5,})
        file_name = 'ans.mp3' 

        if not isinstance(result, dict):
            with open(file_name, 'wb') as f:
                f.write(result)
        return file_name

