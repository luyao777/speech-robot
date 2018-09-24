import requests
import json
import uuid
import base64
from config import DefaultConfig as opt
class recognizer():
    def __init__(self):
        url = "https://openapi.baidu.com/oauth/2.0/token"
        grant_type = "client_credentials"
        api_key = opt.reg_api_key                     # 自己申请的应用
        secret_key = opt.reg_secret_key               # 自己申请的应用
        
        data = {'grant_type': 'client_credentials', 'client_id': api_key, 'client_secret': secret_key}
        r = requests.post(url, data=data)
        self.token = json.loads(r.text).get("access_token")



    def recognize(self,file, rate=8000):
        sig = open(file, "rb").read()
        token = self.token
        url = "http://vop.baidu.com/server_api"
        speech_length = len(sig)
        speech = base64.b64encode(sig).decode("utf-8")
        mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
        rate = rate
        data = {
            "format": "wav",
            "lan": "zh",
            "token": token,
            "len": speech_length,
            "rate": rate,
            "speech": speech,
            "cuid": mac_address,
            "channel": 1,
        }
        data_length = len(json.dumps(data).encode("utf-8"))
        headers = {"Content-Type": "application/json",
                "Content-Length": str(data_length)}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        txt = r.text
        result = txt[txt.find('[')+2:txt.find(']')-1]
        return result


if __name__ == '__main__':
    filename = "test_0.wav"

    a = recognizer()
    print(a.recognize(filename))
