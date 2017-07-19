# coding:utf-8

from multiprocessing import Pool
import os
import time

def test(i):

    print i, "------>ID %s" % (os.getpid())
    time.sleep(2)

if __name__ == "__main__":

    lists = [1, 2, 3, 4, 5, 6, 7, 8]
    pool = Pool(processes=2)     
    pool.map(test, lists)        
    pool.close()
    pool.join()
