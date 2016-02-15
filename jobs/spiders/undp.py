from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import datetime

from jobs.items import JobsItem

class UndpSpider(Spider):
    name = "undp"
    allowed_domains = ["undp.org/"]
    start_urls = ["http://jobs.undp.org/cj_view_jobs.cfm?cur_rgn_id_c=OTHER"]

    def parse(self, response):
        trevenodd = response.xpath('//tr[@class="even" or @class="odd"]')
        items = []

        for tr in trevenodd: #the tds in every tr line
            item = JobsItem()
            item['agency'] = 'UNDP'
            item['title'] = tr.xpath('./td/a/text()').extract()[0]
            item['link'] = response.urljoin(tr.xpath('./td/a/@href').extract()[0])
            item['position'] = tr.xpath('./td[3]//text()').extract()[0].strip(' \t\n\r')
            item['deadline'] = tr.xpath('./td[4]//text()').extract()[1].strip(' \t\n\r')
            item['location'] = tr.xpath('./td[5]//text()').extract()[0].strip(' \t\n\r')
            item['datetime'] = datetime.now()
            yield item

