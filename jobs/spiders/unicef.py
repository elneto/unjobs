from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import datetime

from jobs.items import JobsItem

class UnicefSpider(Spider):
    name = "unicef"
    allowed_domains = ["unicef.org/"]
    start_urls = ["http://www.unicef.org/about/employ/index_temporary_appointments.html", "http://www.unicef.org/about/employ/index_consultancy_assignments.html"]

    def parse(self, response):
        links = response.xpath('//div[@id="bodyarea"]//a')
        items = []

        for link in links:
            item = JobsItem()
            item['agency'] = 'UNICEF'
            item['title'] = link.xpath('./text()').extract()[0]
            item['link'] = response.urljoin(link.xpath('./@href').extract()[0])
            item['datetime'] = datetime.now()
            yield item

