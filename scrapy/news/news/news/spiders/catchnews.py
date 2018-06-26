# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem

class CatchnewsSpider(scrapy.Spider):
    name = "catchnews"
    allowed_domains = ["http://yingyu.xdf.cn"]
    
    
    start_urls=[]
    for i in range(1,2):
        url='http://yingyu.xdf.cn/list_907_'+str(i)+'.html'
        start_urls.append(url)
        
    
    for href in str(url_list):
        start_urls=href
        print start_urls
    
    
    #start_urls = ['http://yingyu.xdf.cn/list_907_1.html']

    def parse(self, response):
          for u in self.start_urls:
              yield scrapy.Request(u,callback=self.parse_start)
              
    def parse_start(self,response):
        for herf in response.xpath('//ul[contains(@class,"txt_lists01 f-f0")]/li/a/@href').extract():
            request=scrapy.Request(herf,callback=self.parse_question)
            yield request
    """   
    def start_url(self, response):        
        for herf in response.xpath('//ul[contains(@class,"txt_lists01 f-f0")]/li/a/@href').extract():
		yield scrapy.Request(herf,callback=self.parse_question)
    
    """
    
    #定义要提取的文件
    def parse_question(self, response):
        item=NewsItem()
        item['time']=response.xpath('//div[contains(@class,"art_xin")]/p[contains(@class,"art_time")]/text()').extract()[0]
        item['title']=response.xpath('//p[contains(@class,"title1 f-f0")]/text()').extract()[0]
        item['context']=response.xpath('//div[contains(@class,"air_con f-f0")]/p/text()').extract()
        
        #必须要添加不然不会返回item
        yield item
        
