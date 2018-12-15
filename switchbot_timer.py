
import binascii
#!/usr/bin/env python
# import os
# import sys
import time

from bluepy.btle import Peripheral
import daemon

# import Deropy.deamonize as dmn
# from daemon.runner import DaemonRunner

# from timeout_decorator import timeout

MAC_ADRESS = 'F7:B0:EE:23:DC:77'


def push():
    p = Peripheral(MAC_ADRESS, 'random')
    hand_service = p.getServiceByUUID(
        'cba20d00-224d-11e6-9fb8-0002a5d5c51b')
    hand = hand_service.getCharacteristics(
        'cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]
    hand.write(binascii.a2b_hex('570100'))
    p.disconnect()


def set_timer():
    while True:
        push()
        time.sleep(60)


if __name__ == '__main__':
    with daemon.DaemonContext():
        set_timer()
