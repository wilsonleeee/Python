from multiprocessing import Process, Lock
import os

def demo(lock, num):

    lock.acquire()

    print "Hello Num: %s -----> %s" % (num, os.getpid())

    lock.release()

if __name__ == '__main__':

    lock = Lock()                                      #这个一定要定义为全局

    for num in range(20):

        Process(target=demo, args=(lock, num)).start()  #这个类似多线程中的threading，但是进程太多了，控制不了。
