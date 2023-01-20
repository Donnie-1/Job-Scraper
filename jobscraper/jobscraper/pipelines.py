# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class JobscraperPipeline:
    def process_item(self, item, spider):
        return item

class SQLitePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('jobs.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists jobs_tb""")
        self.curr.execute("""create table jobs_tb(title text, company text, location text, link text, languages text, cloud text, devops text, database text, education text, soft_skills text, web_frameworks text, data_analytics text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into jobs_tb values (?,?,?,?,?,?,?,?,?,?,?,?)""",(
                            item['title'],
                            item['company'],
                            item['location'],
                            item['link'],
                            item['languages'],
                            item['cloud'],
                            item['devops'],
                            item['database'],
                            item['education'],
                            item['soft_skills'],
                            item['web_frameworks'],
                            item['data_analytics']
                            ))
        self.conn.commit()


