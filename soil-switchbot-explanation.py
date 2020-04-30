#!/usr/bin/env python3

import binascii #バイナリ-ASCII変換用モジュール
from bluepy.btle import Peripheral #bluepyがMACでインストールできないのでエラーが出てる模様をOBにインストールしてエラー確認。

class SwitchBot:
    def __init__(self, mac_address):
        self.p = Peripheral(mac_address, "random") #BLEデバイスへ接続
        hand_service = self.p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b") #サービスオブジェクトの取得（SwitchBotの指定？
        self.hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0] #命令を書き込む場所。読み出せば最終命令が確認できる。

    def press(self):
        self.hand.write(binascii.a2b_hex("570100")) #570103で倒す、570104で引くの命令 ※01と02はアプリ用の模様
        self.p.disconnect()

    def on(self):
        self.p.disconnect()
        raise NotImplementedError()

    def off(self):
        self.p.disconnect()
        raise NotImplementedError()

if __name__ == "__main__": #importでプログラムが動かないように
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="addr", help="MAC address of SwitchBot")
    parser.add_option("-c", "--command", dest="cmd",  help="Command for SwitchBot (press|on|off)")
    (options, args) = parser.parse_args()

    getattr(SwitchBot(options.addr), options.cmd)() #SwitchBot(options.addr)で-aを取得、クラスの指定と立ち上げ、options.cmdで-cを取得し実行



