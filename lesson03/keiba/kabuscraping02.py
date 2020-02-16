import scrapy


class PredictSpider(scrapy.Spider):
	name = "predict"

        custom_settings = {
            "DOWNLOAD_DELAY": 1,
        }

	start_urls = ["http://info.finance.yahoo.co.jp/kabuyoso/article/"]

	def parse(self, response):
		for href in response.css("h3.st02 a::attr('href')"):
			url = response.urljoin(href.extract())
			
			#ここから下が追加分
			#スクレイピングしたURLをたどるためにparse_topicsに投げる
			yield scrapy.Request(url, self.parse_topics)


	def parse_topics(self, response):
		#個別ページのHTML構造を確認する
		#h3タグのクラスst02にタイトルが格納されていることがわかる
		title = response.css("h3.st02 ::text").extract_first()

		#本文はdlタグのクラスmarB20に格納されていることがわかる
		#これを::textで抽出するとbrタグも含めまれて上手くスクレイピングできない
		#xpathのstring()を使用すると、うまい具合にスクレイピングすることができる
		body = response.css("dl.marB20").xpath("string()").extract()

		#辞書形式で格納する
		yield {
			"title" : title,
			"body" : body
		}
