import datetime
import json
import random
import threading
import time
from functools import partial

from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *
from pywebio.platform.tornado import start_server

import honeygain_service


# 讀取 Config
def load_config():
    with open('config.json') as f:
        data = json.load(f)
    return data


@config(theme="dark")
def main():
    for i in token["token"]:
        app = honeygain_service.HoneyGainManager(i)
        devices = app.get_devices()
        balance = app.get_jmpt_balance()
        table = []
        # list ip,manufacturer,platform,total_traffic,total_credit,status,last_active_time from devices
        for i in devices:
            table.append(
                [i["ip"], i["manufacturer"], i["platform"], f"{round(i['stats']['total_traffic'] / 1000000, 2)}",
                 i["stats"]["total_credits"],
                 i["status"], i["last_active_time"]])

        put_markdown(f"`Jumptask Balance : {balance['total_credits']}`")
        put_table(header=['ip', 'manufacturer', 'platform', 'total_traffic', 'total_credits', 'status',
                          'last_active_time'], tdata=table)


# 取得蜜罐線程事件
def loop_get_contest_winnings():
    while True:
        try:
            for i in token:
                app = honeygain_service.HoneyGainManager(i)
                ret = app.get_contest_winnings()
                if ret:
                    put_markdown(f"`[{datetime.datetime}]: 已獲得蜜罐 {ret}`")
                time.sleep(random.randint(3600, 7200))

        except Exception as e:
            print(e)


def event_loop():
    t = threading.Thread(target=loop_get_contest_winnings)
    t.start()
    print("獲得蜜罐線程開始")


token = load_config()
if token["auto_get_contest_winnings"]:
    event_loop()
start_server(main, debug=True, port=8082, host="0.0.0.0")
