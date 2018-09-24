import requests
import json
from config import DefaultConfig as opt

class turing():
    def __init__(self):
        self.key = opt.turing_key
    def ask(self,info):
        url = 'http://www.tuling123.com/openapi/api?key='+self.key+'&info='+info
        res = requests.get(url)
        res.encoding = 'utf-8'
        jd = json.loads(res.text)
        self.response = jd
        return jd['text']


if __name__ == '__main__':
   a = turing()
   print(a.ask('你好'))