from itemadapter import ItemAdapter
import sqlite3
import psycopg2

class JobscraperPipeline:
    def process_item(self, item, spider):
        return item

class SQLitePipeline:
    def __init__(self):
        self.create_connection()
        self.create_tables()

    def create_connection(self):
        self.conn = sqlite3.connect('jobs.db')
        self.curr = self.conn.cursor()

    def create_tables(self):
        self.curr.execute("""drop table if exists jobs_tb""")
        self.curr.execute("""
            create or replace table jobs_tb(
                title text, 
                company text, 
                location text, 
                link text, 
                languages text, 
                cloud text, 
                devops text, 
                database text
            )""")

    def process_item(self, item, spider):
        self.store_db(item, spider)
        return item

    def store_db(self, item, spider):
        self.curr.execute("""insert into jobs_tb values (?,?,?,?,?,?,?)""", 
            (
                item['title'],
                item['company'],
                item['location'],
                item['link'],
                item['languages'],
                item['cloud'],
                item['devops'],
                item['database']
            ))
        self.conn.commit()


