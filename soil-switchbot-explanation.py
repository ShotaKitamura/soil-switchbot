#!/usr/bin/env python3

import binascii #バイナリ-ASCII変換用モジュール
from bluepy.btle import Peripheral #bluepyがMACでインストールできないのでエラーが出てる模様をOBにインストールしてエラー確認。

class SwitchBot:
    def __init__(self, mac_address):
        self.p = Peripheral(mac_address, "random") #BLEデバイスへ接続
        hand_service = self.p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b") #サービスオブジェクトの取得（SwitchBotの指定？
        self.hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]

    def press(self):
        self.hand.write(binascii.a2b_hex("570100")) #570101で倒す、570102で引くの命令
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

    clsd = SwitchBot(options.addr)


    getattr(clsd, options.cmd)()


    getattr(clsd, "on")() #    switchbot.press
    getattr(clsd, "off")()
    
    #soil-switchbot-explanation.py -a macaddress -c press　と打った場合、
    #SwitchBot(macaddress).press として処理される？

