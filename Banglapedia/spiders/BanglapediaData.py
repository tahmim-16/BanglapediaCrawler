import scrapy
from datetime import datetime


class Banglapedia(scrapy.Spider):
    name = 'bangla'             #name of the class

    start_urls = [
        'https://bn.banglapedia.org/'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 1,            #a delay of 1sec between each requests
    }

    num = 0

    def parse(self, response):
        page = response.url.split('/')
        file = 'Banglapedia.html'
        with open(file, 'wb') as f:
            f.write(response.body)          #to save the html body of the page

        for url in response.css('.mw-parser-output'):
            path = url.css('.table-responsive a::attr(href)').getall()
            #print(path)
            for link in path:
                get_path = str(link)
                get_url = response.urljoin(get_path)

                yield scrapy.Request(get_url, callback=self.parse_main)

    def parse_main(self, response):
        page = response.url.split('/')[-1]
        file1 = page + '.html'
        with open(file1, 'wb') as f1:
            f1.write(response.body)

        main_path = response.css('.mw-allpages-body a::attr(href)').getall()
        for link1 in main_path:
            path_link = str(link1)
            path_url = response.urljoin(path_link)
            #print(path_url)

            yield scrapy.Request(path_url, callback=self.parse_last, meta={
                    'url': path_url
                }
            )

    def parse_last(self, response):
        page = response.url.split('/')[-1]
        file2 = page + '.html'
        with open(file2, 'wb') as f2:
            f2.write(response.body)

        if Banglapedia.num <= 50000:
            Banglapedia.num += 1
        title = response.xpath('//*[@id="firstHeading"]/span/text()').extract()
        content = response.css('.mw-parser-output ::text').getall()
        img = response.css('.mw-parser-output img::attr(src)').get()
        if img is not None:
            img_src = 'https://bn.banglapedia.org' + str(img)
        else:
            img_src = 'None'

        published_date = response.xpath('//*[@id="footer-info-lastmod"]/text()').get()
        date = datetime.now()
        date_time = date.strftime("%d/%m/%Y %I:%M:%S")

        yield {
            'ID': Banglapedia.num,
            'Title': title,
            'Text': content,
            'URL': response.meta['url'],
            'IMG_URL': img_src,
            'Published_Date': published_date,
            'Access_Date': date_time
        }

