# -*- coding: utf-8 -*-
import scrapy
from anjukeSpider.items import AnjukespiderItem

class ProxyspiderSpider(scrapy.Spider):
    name = 'proxySpider'
    allowed_domains = ['http://www.xicidaili.com/nn/']
    start_urls = []
    for i in range(1, 3462):
        start_urls.append('http://www.xicidaili.com/nn/'+str(i))

    def parse(self, response):
        for each in response.xpath("//tr[@class='odd']|//tr[@class]"):
                item = AnjukespiderItem()
                item['HOST'] = each.xpath('./td[2]/text()').extract()[0]
                item['POST'] = each.xpath('./td[3]/text()').extract()[0]
                item['address'] = each.xpath('./td[4]/a/text()').extract()[0]
                item['survivingTime'] = each.xpath('./td[9]/text()').extract()[0]
                item['checkTime'] = each.xpath('./td[10]/text()').extract()[0]
                yield item

# //*[@id="ip_list"]/tbody/tr[2]
# //*[@id="ip_list"]/tbody/tr[2]/td[2]
# //*[@id="ip_list"]/tbody/tr[2]/td[3]
# //*[@id="ip_list"]/tbody/tr[2]/td[4]/a#服务器地址
# //*[@id="ip_list"]/tbody/tr[2]/td[9]#存活时间
# //*[@id="ip_list"]/tbody/tr[2]/td[10]#验证时间