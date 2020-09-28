import scrapy
import json
from datetime import date


class Symbol:
    def __init__(self, code, label):
        self.code = code
        self.label = label

    def __getitem__(self, key):
        return getattr(self, key)


class NepseBankSpider(scrapy.Spider):
    name = "nepse"

    def start_requests(self):
        url = 'http://www.nepalstock.com/stockWisePrices'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        options = response.xpath('//select[@id="stock-symbol"]/option')
        del options[0]
        symbols = []
        for o in options:
            symbols.append(Symbol(o.xpath('@value').extract(),o.xpath('text()').get()))

        for s in symbols:
            yield scrapy.http.FormRequest(
                url='http://www.nepalstock.com/stockWisePrices',
                method='POST',
                formdata={
                    'startDate': '2010-01-01',
                    'endDate': date.today().strftime('%Y-%m-%d'),
                    'stock-symbol': s['code'],
                    '_limit': '99999999'
                },
                callback=self.parse2,
                meta={'symbol': s['label']}
            )

    def parse2(self, response):
        symbol = response.meta.get('symbol')
        rows = response.xpath(
            '//*[@class="table table-condensed table-hover"]/tr')
        del rows[0]
        del rows[0]
        data = []
        for r in rows:
            data.append({
                'sn': r.xpath('td[1]//text()').extract_first(),
                'date': r.xpath('td[2]//text()').extract_first(),
                'tran': r.xpath('td[3]//text()').extract_first(),
                'vol': r.xpath('td[4]//text()').extract_first(),
                'amt': r.xpath('td[5]//text()').extract_first(),
                'high': r.xpath('td[6]//text()').extract_first(),
                'low': r.xpath('td[7]//text()').extract_first(),
                'close': r.xpath('td[8]//text()').extract_first(),
            })
        filename = '%s.json' % symbol
        with open(filename, 'wb') as f:
            json.dump(data, f)
        self.log('Saved file %s' % filename)
