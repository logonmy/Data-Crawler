# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import eduItem
from tutorial.selenium.myscrapy import SeleniumRequest
from tutorial.selenium.myscrapy import SeleniumSpider

from lxml import html


class EduSpider(scrapy.Spider):
    name = 'ls'
    # allowed_domains = ['www.dpm.org.cn']
    # start_urls = ['https://www.dpm.org.cn/activity/educations/p/1.html']

    def start_requests(self):
        for page in range(1, 6):
            URL = 'http://www.lvshunmuseum.org/Education/news.aspx?SortID=12&Page={}'.format(page)
            # print(URL)
            yield scrapy.Request(url=URL,callback=self.parse)

    def parse(self, response):
        index = 28
        # / html / body / div[5] / div / div[2] / div[2] / ul / li[1]
        # print(response.xpath('/html/body/div/div/div[2]/div[2]/ul[1]/li[2]/div/a/h3'))
       # ' / html / body / div / div / div[2] / div[2] / ul[1] / li[2] / div / a / h3 / strong'
        for line in response.xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/ul/li'):  # 教育信息爬取
            # print(1)
            item = eduItem()
            item['mid'] = index
            # print(item['mid'])
            item['name'] = line.xpath('./a/div/h1/text()').extract()[0]
            print(item['name'])
            # print(line.xpath('./h2/a/@href').extract())
            item['url'] = "http://www.lvshunmuseum.org" + line.xpath('./a/@href').extract()[0]
            print(item['url'])
            item['details'] = line.xpath('./a/div/span/text()').extract()[0].strip()
            yield item
