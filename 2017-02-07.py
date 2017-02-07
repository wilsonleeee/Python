#coding:utf-8
#爬虫技术对数据挖掘和测试是非常重要的，我们今天实现对目标网站的所有链接进行爬取

#基本知识如下
# Htmllib（sgmllib），这个模块是非常古老的一个模块，偏底层，实际就是简单解析html文档而已，不支持搜索标签，容错性也比较差，这里指的提醒的是，如果传入的html文档没有正确结束的话，这个模块是不会解析的，直到正确的数据传入或者说强行关闭。

# BeautifulSoup，这个模块解析html非常专业，具有很好的容错性，可以搜索任意标签，自带编码处理方案。

# Selenium，自动化web测试方案解决者，类似BeautifulSoup，但是不一样的是，selenium自带了js解释器，也就是说selenium配合浏览器可以用来做动态网页的爬取，分析，挖掘。

# Scrapy框架：一个专业的爬虫框架（单机），有相对完整的解决方案。

# API爬虫：这里大概都是需要付费的爬虫API，比如google，twitter的解决方案，就不在介绍。

#链接爬虫

import re 

def link_crawler(seed_url,link_regex):

	crawl_queue = [seed_url]
	
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)

		for link in get_links(html):
			if re.match(link_regex,link):
				crawl_queue.append(link)

def get_links(html):

	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	return webpage_regex.findall(html)

#调用link_crawler程序就可以获取到路径下的链接