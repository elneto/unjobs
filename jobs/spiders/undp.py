from scrapy.spiders import Spider
from scrapy.selector import Selector

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
            item['title'] = tr.xpath('.//td[position()=1]//text()').extract()[0].strip(' \t\n\r')
            print 'title: ' + item['title']
            item['position'] = tr.xpath('.//td[position()=3]//text()').extract()[0].strip(' \t\n\r')
            print 'position' + item['position']
            item['deadline'] = tr.xpath('.//td[position()=4]//text()').extract()[0].strip(' \t\n\r')
            print 'deadline: ' + item['deadline']
            item['location'] = tr.xpath('.//td[position()=5]//text()').extract()[0].strip(' \t\n\r')
            print 'location: ' + item['location']
            print "*************"


        #return items
#response.xpath('//tr[@class="even"][position()=1]//td').extract()
