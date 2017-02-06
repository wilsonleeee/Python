#coding:utf-8

#author:wilsonleeee
#data:2017/2/6

#网络爬虫
#估算网站大小：扫描以及搜索系统的核心就是网络爬虫，那么遇到比较大的网站，扫描系统的性能就会大大降低，所以对目标网站大小的估计是必不可免的。
#估算网站的大小的简单方法是通过Google搜索的site：关键词过滤域名的结果来获取相关的信息。
#e.g: site:example.website.com

#识别网站所用的技术可以使用-buildwith模块
#pip install buildwith

#识别网站所有者可以使用-whois模块
#pip install whois

#下载网页脚本
#--->

import urllib2
def download(url):
	return urllib2.urlopen(url).read()

#如果不存在页面就抛出异常
#--->

import urllib2
def download(url):
	print 'Downloading:',url
	
	try:
		html = urllib2.urlopen(url).read()

	except urllib2.URLError as e:
		print 'Downloading error:',e.reason
		html = None

	return html

# 做为一名爬虫工程师，我们经常会遇到IP被封的事情，那么我们就需要使用代理来减缓压力。
#-->修改下载函数

def download(url):

	print 'Downloading:', url
	headers = {'User-agent' : User_agent}
	request = urllib2.Request(url,headers=headers)

	try :
				html = urllib2.urlopen(url).read()

	except urllib2.URLError as e:
		print 'Downloading error:',e.reason
		html = None

	return html