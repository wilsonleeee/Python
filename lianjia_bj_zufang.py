# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from Lianjia.items import LianjiaItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
import json
import urllib2
class LianjiaBjZufangSpider(scrapy.Spider):
	name = "lianjia_bj_zufang"
	allowed_domains = ["lianjia.com"]
	with open('lianjia_url.json') as data_file:
		data = json.load(data_file)
	start_urls = []
	for i in range(0,len(data)):
		test = str(data[i]["store_url"].encode('utf-8'))
		pattern = re.compile(r'\/(\w+\d)+\/')
		match = pattern.search(test)
		for j in range(1,data[i]["page_no"] + 1):
			start_urls.append(test[:-len(match.groups()[0]) -1] + "pg" + str(j)  + str(match.groups()[0]) + "/")
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
		#l = ItemLoader(item = LianjiaItem(),response=response)
		for i in range(0,len(response.xpath("//div[@class='info-panel']/h2/a/text()").extract())):
			l = ItemLoader(item = LianjiaItem(),response=response)
			info = response.xpath("//div[@class='info-panel']/h2/a/text()").extract()[i].encode('utf-8')
			local = response.xpath("//div[@class='info-panel']").xpath(".//span[@class='region']/text()").extract()[i].encode('utf-8')
			house_layout = response.xpath("//div[@class='info-panel']").xpath(".//span[@class='zone']//text()").extract()[i].encode('utf-8')
			house_square = response.xpath("//div[@class='info-panel']").xpath(".//span[@class='meters']/text()").extract()[i].encode('utf-8')
			house_orientation = response.xpath("//div[@class='info-panel']").xpath(".//div[@class='where']//span/text()").extract()[(i + 1) * 4 - 1].encode('utf-8')
			district = response.xpath("//div[@class='info-panel']").xpath(".//div[@class='con']/a/text()").extract()[i].encode('utf-8')[:-6]
			floor = response.xpath("//div[@class='info-panel']").xpath(".//div[@class='con']//text()").extract()[(i + 1) * 5 - 3].encode('utf-8')
			building_year = response.xpath("//div[@class='info-panel']").xpath(".//div[@class='con']//text()").extract()[(i + 1) * 5 - 1].encode('utf-8')
			price_month = response.xpath("//div[@class='info-panel']").xpath(".//span[@class='num']//text()").extract()[(i + 1) * 2 - 2].encode('utf-8')
			person_views = response.xpath("//div[@class='info-panel']").xpath(".//span[@class='num']//text()").extract()[(i + 1) * 2 - 1].encode('utf-8')
			tags = []
			for j in range(0,len(response.xpath("//div[@class='view-label left']")[i].xpath(".//span//text()").extract())):
				tags.append(response.xpath("//div[@class='view-label left']")[i].xpath(".//span//text()").extract()[j].encode("utf-8"))
			l.add_value('info',info)
			l.add_value('local',local)
			l.add_value('house_layout',house_layout)
			l.add_value('house_square',house_square)
			l.add_value('house_orientation',house_orientation)
			l.add_value('district',district)
			l.add_value('floor',floor)
			l.add_value('building_year',building_year)
			l.add_value('price_month',price_month)
			l.add_value('person_views',person_views)
			l.add_value('tags',tags)
			print l
			yield l.load_item()
