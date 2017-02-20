# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from Lianjia.items import LianjiaErshouItem
import json

class LianjiaErshouSpider(scrapy.Spider):
	name = "lianjia_ershou"
	allowed_domains = ["lianjia.com"]
	with open('/root/code/itjuzi/itjuzi/spiders/lianjia_ershou_link.json') as data_file:
		start_urls = json.load(data_file)
#	start_urls = ('http://ajax.lianjia.com/ajax/housesell/area/district?ids=23008619&limit_offset=0&limit_count=100&sort=&&city_id=110000',)
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
#		l = ItemLoader(item = ItjuziItem(),response=response)
		jsonresponse = json.loads(response.body_as_unicode())
		for i in range(0,len(jsonresponse['data']['list'])):
			l = ItemLoader(item = LianjiaErshouItem(),response=response)
			house_code = jsonresponse['data']['list'][i]['house_code']
			price_total = jsonresponse['data']['list'][i]['price_total']
			ctime = jsonresponse['data']['list'][i]['ctime']
			title = jsonresponse['data']['list'][i]['title']
			frame_hall_num = jsonresponse['data']['list'][i]['frame_hall_num']
			tags = jsonresponse['data']['list'][i]['tags']
			house_area = jsonresponse['data']['list'][i]['house_area']
			community_id = jsonresponse['data']['list'][i]['community_id']
			community_name = jsonresponse['data']['list'][i]['community_name']
			is_two_five = jsonresponse['data']['list'][i]['is_two_five']
			frame_bedroom_num = jsonresponse['data']['list'][i]['frame_bedroom_num']
			l.add_value('house_code',house_code)
			l.add_value('price_total',price_total)
			l.add_value('ctime',ctime)
			l.add_value('title',title)
			l.add_value('frame_hall_num',frame_hall_num)
			l.add_value('tags',tags)
			l.add_value('house_area',house_area)
			l.add_value('community_id',community_id)
			l.add_value('community_name',community_name)
			l.add_value('is_two_five',is_two_five)
			l.add_value('frame_bedroom_num',frame_bedroom_num)
			print l
			yield l.load_item()
