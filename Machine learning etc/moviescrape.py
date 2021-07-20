import scrapy
import re
import logging
# import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
# import json
# import sqlite3
import csv

# class dudepipeline(object):
#     def __init__(self):
#         self.create_conn()
#         self.create_tb()
#
#     def create_conn(self):
#         self.conn = sqlite3.connect("dude_db")
#         self.curr = self.conn.curr()
#
#     def create_tb(self):
#         self.curr.execute("""drop table if exists dude_tb""")
#         self.curr.execute("""create table dude_tb(
#                         title text,
#                         rating int,
#                         genre text)
#                     """)
#
#     def parse_item(self, item, spider):
#         self.store_db(item)
#         return item
#
#     def store_db(self, item):
#         self.curr.execute("""insert into dude_tb values(?,?,?)""",(
#                             item['title'][0],
#                             item['rating'][0],
#                             item['genre'][0]
#         ))
#

# class JsonWriterPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = open('duderes\dudeitems6.jl', 'w')
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item
#
class CSVWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('duderes\dudecrl.csv', 'a')
        writer = csv.writer(self.file)
        writer.writerow(['title', 'genre', 'rating'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        writer = csv.writer(self.file)
        # writer.writerow(['title', 'genre', 'rating'])
        writer.writerows([item['title'], item['genre'], item['rating']])
        return item

class DudeItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    rating = scrapy.Field()
    genre = scrapy.Field()


class DudeSpider(scrapy.Spider):
    filename= "dudecrl6"
    name = 'dude'
    start_urls = [
        # "https://3hiidude.me/",
        'https://3hiidude.me/watch/english-movies-2021/',
        'https://3hiidude.me/watch/english-movies-2020/',
        'https://3hiidude.me/watch/english-movies-2019/',
        'https://3hiidude.me/watch/english-movies-2018/',
        'https://3hiidude.me/watch/english-movies-2017/',
        'https://3hiidude.me/watch/english-movies-2016/',
        'https://3hiidude.me/watch/english-movies-2015/',
        'https://3hiidude.me/watch/english-movies-2014/',
        'https://3hiidude.me/watch/english-movies-2013/',
        'https://3hiidude.me/watch/english-movies-2012/',
        'https://3hiidude.me/watch/english-movies-2011/',
        'https://3hiidude.me/watch/english-movies-2010/'
    ]

    # custom_settings = {
    #     'LOG_LEVEL': logging.WARNING,
    #     'ITEM_PIPELINES': {'__main__.CSVWriterPipeline': 1},  # Used for pipeline 1
    #     'FEED_FORMAT': 'csv',  # Used for pipeline 2
    #     'FEED_URI': 'duderes\dudeitems7.csv'  # Used for pipeline 2
    # }

    def __init__(self):
        self.file = open(f"duderes\{filename}.csv", 'w')
        writer = csv.writer(self.file)
        writer.writerow(['title', 'genre', 'rating'])

    def parse(self, response):

        movie_link = response.css("div.cont_display a::attr('href')").extract()
        print("MOVIE LINKS:", movie_link)
        for url in movie_link:
            yield response.follow(url, callback=self.parse_item)


    def parse_item(self, response):
        title = response.css(".entry-title::text").get()
        for i in title:
            if i == ',':
                title = title.replace(i, ' ')

        para = response.css("p:nth-child(4)").get()
        rating = re.findall(r"Rating:</b> (.*(?=\/))", para)
        rating = float(rating[0])
        # rating = rating[0]
        genre = re.findall(r"Genres:(.+[\r\n].+[\r\n].+)", para)
        genre = re.findall(r"(\w+,)+", genre[0])
        genre = "".join(genre)
        for i in genre:
            if i == ',':
                genre = genre.replace(i, ' ')

                # rating = re.findall(r"Rating:</b> (.*(?=\/))", rating),

                # title = response.css(".entry-title::text").get(),
                # title = re.findall(r".*(?=\()", title)[0]

        item = DudeItem()

        item['title'] = title
        item['rating'] = rating,
        item['genre'] = genre

        yield item

        file = open(f"duderes\{filename}.csv", 'a')
        writer = csv.writer(self.file)
        writer.writerow([title, genre, rating])
        # yield {
        #     'Title': title,
        #
        #     'Genres': genre,
        #
        #     # "Title": title,
        #     # 'Title': re.findall(r"\w+, \w+", title),
        #     # 'Title': re.findall(r".*(?=\()", title)[0],
        #     # 'Year': re.findall(r"\((\d+)", title),
        #     'Rating': rating,
        #
        #     # print(f"Title: {title}, Rating: {rating}")
        # }
        #
        # # # self.parse()


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

# process.crawl(AuthorSpider)
process.crawl(DudeSpider)

process.start()
