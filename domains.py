# -*- coding: utf8 -*-
#

# 域名收集工具
# 批量
import urllib2
import gevent
from multiprocessing import Process
from gevent import monkey;monkey.patch_all()
from BeautifulSoup import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def subdomainapi(url):

    if 'www' in url:
        try:
            subdomain = []
            target_url = url.strip('http:').strip('/').strip('www.')
            api = 'http://i.links.cn/subdomain/'+target_url+'.html'
            i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
            req = urllib2.Request(api, headers=i_headers)
            body_text = urllib2.urlopen(req).read()
            soup = BeautifulSoup(body_text)
            links = soup.findAll('a')

            for link in links:
                url = link.get('href')
                if target_url in url:
                    url = url.strip('http:').strip('/')
                    subdomain.append(url)
            return subdomain
        except:
            pass
    else:
        return None


def savedomains(url):

    list = subdomainapi(url)

    path = "C:\Users\XXX\Desktop\%s.txt" % (url)
    f = open(path, 'w')

    for domain in list:
        f.write(domain)
        f.write("\n")
    f.close()


def taskstart(file):

    task_list = []
    domains = open(file, 'r').readlines()

    for domain in domains:
        domain = domain.split('\n')
        domain = domain[0]
        task_list.append(gevent.spawn(savedomains, domain))

    gevent.joinall(task_list)


if __name__ == '__main__':

    taskstart("C:\Users\XXX\Desktop\domains.txt")