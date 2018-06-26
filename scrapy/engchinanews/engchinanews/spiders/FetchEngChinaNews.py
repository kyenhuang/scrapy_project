# -*- coding: utf-8 -*-
import scrapy

class FetchengchinanewsSpider(scrapy.Spider):
    #有两个属性
    name = "FetchEngChinaNews"
    allowed_domains = ["http://yingyu.xdf.cn"]
    start_urls='http://yingyu.xdf.cn/list_907_1.html'
    
    '''
    for i in range(1,454):
        url='http://yingyu.xdf.cn/list_907_'+str(i)+'.html'
        start_urls = url
    '''
        
    count=0   
    #抓取每业url
    def parse(self, response):
        FetchengchinanewsSpider.count+=1
        for herf in response.xpath('//ul[contains(@class,"txt_lists01 f-f0")]/li/a/@href'):
		yield scrapy.Request(herf,callback=self.parse_question)
    
    def parse_question(self, response):
        yield {
        #文章的更新时间
	 	'time':response.xpath('//div[contains(@class,"art_xin")]/p[contains(@class,"art_time")]/text()').extract()[0],
        #文章的标题
		'title':response.xpath('//p[contains(@class,"title1 f-f0")]/text()').extract()[0],
        #文章的内容
		'context':response.xpath('//div[contains(@class,"air_con f-f0")]/p/text()').extract()	
        }
       

