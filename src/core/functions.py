# -*- coding: utf-8 -*-
import os, signal, logging

def Usage():
    logging.info('Usage:  python main.py start/stop/restart')
    exit()


#为了防止并发加入PID文件
def writePID(pid_path):
    fd=os.open(pid_path,os.O_CREAT|os.O_EXCL|os.O_RDWR)
    os.write(fd,"%s" % str(os.getpid()))
    os.close(fd)

#删除本应用程序的PID
def deletePID(pid_path):
    try:
        os.remove(pid_path)
    except:
        pass

def stop(pid_path):
    if os.path.exists(pid_path):
        fd=open(pid_path)
        pid=int(fd.readline())
        fd.close()
        try:
            deletePID()
            os.kill(pid,signal.SIGTERM)
        except:
            raise SystemExit('1:收到终止命令,退出程序')
    raise SystemExit('2:收到终止命令,退出程序')

def init_log():
    #日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='myapp.log',
        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-6s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)