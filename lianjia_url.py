# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from Lianjia.items import LianjiaUrlItem
import json

class LianjiaUrlSpider(scrapy.Spider):
	name = "lianjia_url"
	allowed_domains = ["lianjia.com"]
	#chengqu_list = ['dongcheng','xicheng','chaoyang','haidian','fengtai','shijingshan','tongzhou','changping','daxing','yizhuangkaifaqu','shunyi','fangshan','mentougou','yanjiao']
	#area_list = ['ra1','ra2','ra3','ra4','ra5','ra6','ra7','ra8','ra9']
	#rent_list = ['rp1','rp2','rp3','rp4','rp5','rp6','rp7']
	#start_urls = []
	#for j in chengqu_list:
	#	for i in area_list:
	#		for k in rent_list:
	#			start_urls.append('http://bj.lianjia.com/zufang/%s/%s%s/'%(j,i,k))
	chengqu_list = ['dongcheng','xicheng','chaoyang','haidian','fengtai','shijingshan','tongzhou','changping','daxing','yizhuangkaifaqu','shunyi','fangshan','mentougou','yanjiao']
	area_list = ['ra1','ra2','ra3','ra4','ra5','ra6','ra7','ra8','ra9']
	rent_list = ['rp1','rp2','rp3','rp4','rp5','rp6','rp7']
	forward_list = ['f1','f2','f3','f4','f5',]
	start_urls = []
	for k in forward_list:
		start_urls.append('http://bj.lianjia.com/zufang/%s/%s%s%s/'%(chengqu_list[-1],k,area_list[3],rent_list[1]))
	headers = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip,deflate",
		"Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
		"Connection": "keep-alive",
		"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
		"Referer": "http://www.itjuzi.com/"
		}

	def parse(self, response):
		if response.xpath("//div[@class='page-box house-lst-page-box']").re(':(\w+)'):
			house_no = int(str(response.xpath("//div[@class='page-box house-lst-page-box']").re(':(\w+)')[0]))
			if house_no:
				item = LianjiaUrlItem()
				store_url = response.url
				item['store_url'] = store_url
				item['page_no'] = house_no
				yield item
			else:
				pass
		else:
			pass		
