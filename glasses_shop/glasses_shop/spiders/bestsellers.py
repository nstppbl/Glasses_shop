# -*- coding: utf-8 -*-
import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@id='product-lists']/div"):
            yield {
                'url' : product.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url' : product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                'name' : product.xpath(".//div[@class='p-title']/a/@title").get(),
                'price' : product.xpath(".//div[@class='p-price']/div/span/text()").get()

            }
    
        next_page = response.xpath("//li[@class='page-item col-6 p-0']/a/@href").get()

        if next_page:
          yield scrapy.Request(url=next_page, callback=self.parse)

