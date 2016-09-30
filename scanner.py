#/usr/bin/env python
# _*_ coding:utf-8 _*_

#By:wilsonleee
#date:2016-09-30

#主要完成信息的爬取，通常我们需要对爬虫捕捉的数据进行分析，处理，再次利用或者格式化，
#显然我们不能只是把爬虫捕捉到的数据在内存中处理，然后打印在屏幕上，我将介绍几种主流
#的数据存储方法。爬虫处理数据的能力往往是决定爬虫价值的决定性因素，同时一个稳定的存
#储数据的方法也绝对是一个爬虫的价值体现，采用多线程爬虫创造多个并行线程协调工作也是
#绝对提高爬虫效率，降低失败率的好方法

#Python多线程使用

import time
import thread
def timer(no,interval):
    cnt = 0
    while cnt < 10:
        print 'Tread:(%d) Time:%s\n'%(no,time.ctime())
        time.sleep(interval)
        cnt += 1
    thread.exit_thread()

def test():
    thread.start_new_thread(timer,(1,1))
    thread.start_new_thread(timer,(2,2))

if __name__=='__main__':
    test()