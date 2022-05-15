import requests


class JumpTaskManager():
    def __init__(self, _token):
        self.host = "https://api.jumptask.io/"
        self.ses = requests.session()
        self.token = _token
        self.headers = {
            'authorization': f'Bearer {self.token}',
            'referer': 'https://dashboard.honeygain.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
        }

    # 取得裝置資訊
    def get_devices(self):
        try:
            url = self.host + "api/v2/devices"
            ret = self.ses.get(url, headers=self.headers)
            if ret.status_code >= 400:
                return "Cookies失效"
            if ret:
                return ret.json()['data']
            else:
                return None
        except:
            return None

    # 取得 JMPT 轉換匯率
    def get_jmpt_currency(self, _currency):
        try:
            url = self.host + "currency"
            ret = self.ses.get(url, headers=self.headers)
            if ret.status_code >= 400:
                return "Cookies失效"
            if ret:
                if _currency.lower() == 'bnb':
                    return ret.json()['data']['bnb']
                else:
                    return ret.json()['data']['usd']
            else:
                return None
        except:
            return None

    # 取得JMPT餘額
    def get_jmpt_balance(self):
        try:
            url = self.host + "accounting/balances"
            ret = self.ses.get(url, headers=self.headers)
            if ret:
                return ret.json()['data']['total']
            else:
                return None
        except:
            return None

    # 取得Gas Fee
    def get_gas_fee(self):
        try:
            url = self.host + "payments/gas-estimate/"
            ret = self.ses.get(url, headers=self.headers)
            if ret:
                return ret.json()['data']['gas_fee']
            else:
                return None
        except:
            return None

    # 取得JMPT餘額實際價值
    def get_jmpt_balance_in_usd(self):
        try:
            jmpt_balance = float(self.get_jmpt_balance())
            jmpt_currency = float(self.get_jmpt_currency('usd'))
            return jmpt_balance * jmpt_currency
        except:
            return None
