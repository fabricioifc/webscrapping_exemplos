import scrapy
import ipdb

class AosFatosSpider(scrapy.Spider):
	name = 'aos_fatos'
	start_urls = ['https://aosfatos.org/']

	def parse(self, response):
		links = response.xpath('//nav//ul//li//a[re:test(@href, "checamos")]/@href').getall() 
		for link in links:
			yield scrapy.Request(
				response.urljoin(link),
				callback=self.parse_category
			)

	def parse_category(self, response):
		ipdb.set_trace()
		pass