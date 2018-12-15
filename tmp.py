
import time
# # from daemonize import *
# import Deropy.deamonize as dmn
#
# # 5分おきに実行
# # @interval_run(5)
# @dmn.interval_run(5)
# def test(arg, kws=None):
#     print(arg, kws)
#
# dmn.start_daemon(test, 'Test', kws='keyword')

import daemon
from switchbot_timer import push

def main():
    while True:
        # print('ue')
        # push()
        time.sleep(10)

with daemon.DaemonContext():
    main()
