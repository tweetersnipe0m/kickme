# -*- encoding=utf8 -*-
from airtest.core.api import *
import pyotp
import json
import os
import sys
from datetime import datetime
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

import socket
from contextlib import closing
#import logging
#logger = logging.getLogger("airtest")
#logger.setLevel(logging.ERROR)

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print("Port is open")
            return True
        else:
            print("Port is not open")
            return False

secretjson = json.load(open('point_hb.json'))
adbportsjson = json.load(open('adbports.json'))


def startVirtual(index, Adbport):
    yeshenDIR = "E:\\夜神数据\\Nox\\bin"
    yeshenEXE = "NoxConsole.exe"
    yeshenStartCommand = "start /d " + yeshenDIR + " " + yeshenEXE + " launch -index:" + str(index)
    print(yeshenStartCommand)
    os.system(yeshenStartCommand)
    while True:
        sleep(5)
        if check_socket('localhost', Adbport):
            sleep(10)
            break
