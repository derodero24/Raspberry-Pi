import binascii
import sys
import time

import daemon

from bluepy.btle import Peripheral
from timeout_decorator import timeout


@timeout(10)
def push(mac_address):
    p = Peripheral(mac_address, 'random')
    hand_service = p.getServiceByUUID('cba20d00-224d-11e6-9fb8-0002a5d5c51b')
    hand = hand_service.getCharacteristics(
        'cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]
    hand.write(binascii.a2b_hex('570100'))
    p.disconnect()


def set_timer(interval, mac_address):
    while True:
        push(mac_address)
        time.sleep(interval * 60)


def main():
    # Macアドレスのテスト
    if sys.argv[1] in ('-t', '--test'):
        try:
            push(sys.argv[2])
            print('Success !!')
        except Exception as ex:
            print('Failed ...')

    # タイマーセット
    elif str.isdecimal(sys.argv[1]):
        with daemon.DaemonContext():
            set_timer(sys.argv[1], sys.argv[2])

    # その他
    else:
        print('got unexpected arguments.')


if __name__ == '__main__':
    main()
