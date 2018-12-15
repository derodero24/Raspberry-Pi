
# from daemonize import *
import Deropy.deamonize as dmn

# 5分おきに実行
# @interval_run(5)
@dmn.interval_run(5)
def test(arg, kws=None):
    print(arg, kws)

dmn.start_daemon(test, 'Test', kws='keyword')
