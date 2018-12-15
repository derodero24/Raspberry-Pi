import binascii
import sys
import time

import daemon

from bluepy.btle import Peripheral
from timeout_decorator import timeout

# address: Macアドレス, interval: 実行間隔
switch_list = [{'address': 'F7:B0:EE:23:DC:77', 'interval': 100}]


@timeout(10)
def push(address):
    p = Peripheral(address, 'random')
    hand_service = p.getServiceByUUID('cba20d00-224d-11e6-9fb8-0002a5d5c51b')
    hand = hand_service.getCharacteristics(
        'cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]
    hand.write(binascii.a2b_hex('570100'))
    p.disconnect()


def set_timer():
    while True:
        for switch in switch_list:
            if time.time() - switch['last_time'] > switch['interval'] * 60:
                try:
                    push(switch['address'])
                except:
                    pass
                switch['last_time'] = time.time()


if __name__ == '__main__':
    for switch in switch_list:
        switch['last_time'] = time.time()
    with daemon.DaemonContext():
        set_timer()
