import binascii
import sys
import time

from bluepy.btle import Peripheral


def push(mac_address):
    p = Peripheral(mac_address, 'random')
    hand_service = p.getServiceByUUID('cba20d00-224d-11e6-9fb8-0002a5d5c51b')
    hand = hand_service.getCharacteristics(
        'cba20002-224d-11e6-9fb8-0002a5d5c51b')[0]
    hand.write(binascii.a2b_hex('570100'))
    p.disconnect()


def set_timer():
    # テストモード
    if sys.argv[1] == '--test':
        try:
            pushT(sys.argv[2])
            print('Success !!')
        except Exception as ex:
            print('Failed ...')

    # タイマーセット
    elif str.isdecimal(sys.argv[1]):
        intervals = int(sys.argv[1])
        mac_address = sys.argv[2]
        push(mac_address)
        last_time = time.time()
        while True:
            if time.time() - last_time > intervals * 60:
                push(mac_address)
                last_time = time.time()
            # return

    # その他
    else:
        print('got unexpected arguments.')


if __name__ == '__main__':
    set_timer()
