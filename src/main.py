# -*- coding: utf-8 -*-
import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(".")#加入默认的扫描路径

import atexit
import logging
from core.functions import writePID, deletePID, Usage, stop, init_log
from core.config import Config

def init():
    path=os.path.split(os.path.realpath(__file__))[0]
    config_path = '%s/config.ini'%path
    Config.init(config_path)
    CACHEFOLDER = os.getenv('HOME') + '/.cache/autohome/'
    if not os.path.exists(CACHEFOLDER):
        os.makedirs(CACHEFOLDER)
    PIDLOG="%sautohome.pid"%CACHEFOLDER
    Config.set("global",'PID',PIDLOG)
    init_log()

def main():
    writePID(PIDLOG)
    from cmd.weather import Weather
    target = Weather('上海')
    target.get()

if __name__ == "__main__":
    init()
    PIDLOG = Config.get('global','PID')
    atexit.register(lambda:deletePID(PIDLOG))
    params=sys.argv
    if len(params)<2:
        Usage()
    else:
        if params[1]=="start":
            if os.path.exists(PIDLOG):
                logging.info("Program is running")
                Usage()
            else:
                main()
        elif params[1]=="stop":
            stop(PIDLOG)
        elif params[1]=="restart":
            pass
