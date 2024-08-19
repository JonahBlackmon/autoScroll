import time
from obswebsocket import obsws, requests
import sys

host = 'localhost'
port = 4455
password = 'secret'

class OBSWebsocketsManager():
    def __init__(self):
        self.ws = obsws(host, port, password)
        try:
            self.ws.connect()
        except:
            print("error")
            time.sleep(3)
            sys.exit()
        print("Connected to OBS Websockets!\n")
    def startRecord(self):
        self.ws.call(requests.StartRecord())
    def stopRecord(self):
        self.ws.call(requests.StopRecord())

