#!/usr/bin/env python3

import binascii
from bluepy.btle import Peripheral

class SwitchBot:
    def __init__(self, mac_address):
        self.p = Peripheral(mac_address, "random")
        hand_service = self.p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
        self.hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
        self.receive = hand_service.getCharacteristics("cba20003-224d-11e6-9fb8-0002a5d5c51b")[0]

    def press(self):
        self.hand.write(binascii.a2b_hex("570100")) #スイッチON・OFF命令、一度出て戻る。
        self.p.disconnect()

    def on(self):
        self.hand.write(binascii.a2b_hex("570103")) #スイッチON命令
        self.p.disconnect()
        #raise NotImplementedError()

    def off(self):
        self.hand.write(binascii.a2b_hex("570104")) #スイッチOFF命令
        self.p.disconnect()
        #raise NotImplementedError()

    def notify(self): #現在値読み出し確認用
        receive001 = self.receive.read()
        print('receive001:')
        print(receive001)
        receive002 = self.hand.read()
        print('receive002:')
        print(receive002)
        self.p.disconnect()


if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="addr", help="MAC address of SwitchBot")
    parser.add_option("-c", "--command", dest="cmd",  help="Command for SwitchBot (press|on|off)")
    (options, args) = parser.parse_args()

    getattr(SwitchBot(options.addr), options.cmd)()
