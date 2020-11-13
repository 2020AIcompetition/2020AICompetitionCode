# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from time import sleep


class KkDataSourcesSpider(scrapy.Spider):
    name = "kk_data_sources"
    allowed_domains = ["www.kekenet.com"]
    start_urls = ['http://www.kekenet.com/Article/media/economist/']

    def start_requests(self):
        yield scrapy.Request(url=KkDataSourcesSpider.start_urls[0], callback=self.parse, meta={'page': 1}, dont_filter=True)

    def parse(self, response):  # resonse相当于从网络中返回内容所存储的或对应的对象
        # print(response.body)
        # with open(fname, 'wb') as f:  # 从响应的url中提取文件名字作为保存为本地的文件名，然后将返回的内容保存为文件
        #         #     f.write(response.body)
        # print(response.xpath("//div[@class='page th']/a[contains(text(),'285')]/text()").extract())
        # this_page = response.xpath("//div[@class='page th']/b/text()").extract()[0]

        next_href = response.xpath("//div[@class='page th']/a[text()='下页']/@href").extract()
        self.log('Saved file %s.')  # self.log是运行日志，不是必要的
        if next_href is not None and len(next_href):  # 判断是否存在下一页
            next_page = response.urljoin(next_href[0])
        yield scrapy.Request(next_page, callback=self.parse)
