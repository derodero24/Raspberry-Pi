 #!/usr/bin/env python
import binascii
# import os
import sys
import time

from bluepy.btle import Peripheral
# import Deropy.deamonize as dmn
# from daemon.runner import DaemonRunner

# from timeout_decorator import timeout

MAC_ADRESS = 'F7:B0:EE:23:DC:77'

def push(mac_address):
    p = Peripheral(mac_address, 'random')
    hand_service = p.getServiceByUUID(
        'cba20d00-224d-11e6-9fb8-0002a5d5c51b')
    hand = hand_service.getCharacteristics(
        'cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]
    hand.write(binascii.a2b_hex('570100'))
    p.disconnect()


if __name__ == '__main__':
    while True:
        push(MAC_ADRESS)
        time.sleep(60)
