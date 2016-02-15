from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# undp and unicef are spiders of the project.
process.crawl('undp')
process.crawl('unicef')
process.start() # the script will block here until the crawling is finished