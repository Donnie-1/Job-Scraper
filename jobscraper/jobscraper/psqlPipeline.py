import sys
import psycopg2

class JobscraperPipeline:
    def process_item(self, item, spider):
        return item

class PsqlPipeline:
    def __init__(self):
        self.create_connection()
        
    def create_connection(self):
        self.db = psycopg2.connect(
            dbname="jobs",
            user="postgres", 
            password="denver",
            host="localhost", 
            port="5432"              
        )
        self.curr = self.db.cursor()

    def store_db(self, item, spider): 
        try:
            # Insert into Jobs table
            self.curr.execute("""
                INSERT INTO Jobs (title, company, location, list_date, link)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING job_id
            """, (
                    item['title'],
                    item['company'],
                    item['location'],
                    item['list_date'],
                    item['link']
            ))
            
            job_id = self.curr.fetchone()[0]  

            # Inset in Programming_Languages table
            for language in item['languages'].split(' '):
                if language.strip():  # Ensure the language is not an empty string
                    # Insert into Programming_Languages table
                    self.curr.execute("""
                        INSERT INTO Programming_Languages (language_name)
                        VALUES (%s)
                        ON CONFLICT (language_name) DO NOTHING
                        RETURNING language_id
                    """, (language.strip(),))
                    
                    # Capture the language_id, if it's not returned (because of conflict), fetch it manually
                    language_id = self.curr.fetchone()
                    if not language_id:
                        self.curr.execute("""
                            SELECT language_id FROM Programming_Languages WHERE language_name = %s
                        """, (language.strip(),))
                        language_id = self.curr.fetchone()[0]
                    else:
                        language_id = language_id[0]

                    # Insert into Job_Languages table
                    self.curr.execute("""
                        INSERT INTO Job_Languages (job_id, language_id)
                        VALUES (%s, %s)
                    """, (job_id, language_id))

            self.db.commit()

        except psycopg2.Error as e:
            self.db.rollback()
            spider.logger.error(f"Error processing item: {item} | Error: {e}")
    
    def process_item(self, item, spider):
        self.store_db(item, spider)
        return item
         