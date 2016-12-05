from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import sys
sys.path.append('C:\My files\TRAINING\Course\Python\doubanmovie')
from doubanmovie.items import DoubanmovieItem

class MoiveSpider(CrawlSpider):
    name="doubanmovie"
    allowed_domains=["movie.douban.com"]
    start_urls=["https://movie.douban.com/top250"]
    rules=[
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback="parse_item"),
    ]

    def parse_item(self,response):
        sel=Selector(response)
        item=DoubanmoiveItem()
        item['name']=sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['score']=sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        item['director']=sel.xpath('//*[@id="info"]/span[1]/a/text()').extract()
        item['classification']= sel.xpath('//span[@property="v:genre"]/text()').extract()
        item['actor']= sel.xpath('//*[@id="info"]/span[3]/a[1]/text()').extract()
        return item
