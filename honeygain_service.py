import requests


class HoneyGainManager():
    def __init__(self, _token):
        self.host = "https://dashboard.honeygain.com/"
        self.ses = requests.session()
        self.token = _token
        self.headers = {
            'authorization': f'Bearer {self.token}',
            'referer': 'https://dashboard.honeygain.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
        }

    # 取得裝置資訊
    def get_devices(self):
        url = self.host + "api/v2/devices"
        ret = self.ses.get(url, headers=self.headers)
        if ret:
            return ret.json()['data']
        else:
            return None

    # 取得JMPT餘額
    def get_jmpt_balance(self):
        url = self.host + "api/v1/earnings/jt"
        ret = self.ses.get(url, headers=self.headers)
        if ret:
            return ret.json()['data']
        else:
            return None