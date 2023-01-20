import scrapy
import re
import random 
import sqlite3
from urllib.parse import urlencode

API_KEY = 'a6c39127-0d1a-4b5e-a850-be51e7ff5e51'

header = { 
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "seek-request-brand": "seek",
    "seek-request-country": "AU",
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
}

class JobSpider(scrapy.Spider):
    name = 'jobSpider'
    # start_urls = ['https://www.seek.com.au/software-engineer-jobs']
    download_delay = 1/5

    def start_requests(self):
        
        start_url = 'https://www.seek.com.au/software-engineer-jobs'
        yield scrapy.Request(url=start_url, callback = self.parse, headers=header)
    
    def parse (self, response):
        
        results = response.xpath("//*[@id='app']")
        for job in results.css("article"):
            
            subpage_link = job.css("a[data-automation='jobTitle']").attrib["href"]
            
            data = {
                'title': job.css("a[data-automation='jobTitle']::text").get(),
                'company': job.css("a[data-automation='jobCompany']::text").get(),
                'location': job.css("a[data-automation='jobLocation']::text").get(),
                'list_date': job.css("span[data-automation='jobListingDate']::text").get(),
                'link': subpage_link,
            }
            
            yield response.follow(subpage_link, self.parse_subpage, 
                                  meta = {"data": data, 'original_url': response.url}, headers=header)
            
        # goto next page 
        next_page = response.css("a[aria-label='Next']").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_subpage (self, response):
        languages = ["python", "java ", "c#", "c++", "javascript", "ruby", "typescript", "rust", "shell"]    
        cloud = ["aws", "azure", "gcp", "redhat"]
        devops = ["kubernetes", "ci/cd", "jenkins", "docker", "ansible", "terraform", "nagios", "prometheus"]
        database = ["mysql", "postgresql", "mongodb", "mongo", "cassandra", "firebase", "redis", "sqllite", "oracle", "sql server", "sql", "nosql"]
        education = ["degree", "tertiary"]
        soft_skills = ["communication", "teamwork", "leadership", "proactive", "problem solv", "work ethic", "reliable"]
        web_frameworks = ["react", "angular", "vue", "express", "laravel"]
        data_analytics = ["matplotlib", "powerbi", "pandas", "numpy", "tableau", "power bi", "qlikview", "d3"]
        
        names = ["languages", "cloud", "devops", "database", "education", "soft_skills", "web_frameworks", "data_analytics"]
        technologies = [languages, cloud, devops, database, education, soft_skills, web_frameworks, data_analytics]
        
        inner_page = response.xpath("//*[@id='app']")
        data = response.meta["data"]
        
        # formats subpage text
        text = inner_page.css("div[data-automation='jobAdDetails'] ::text").extract()
        text = ' '.join(map(str, text))
        text = text.lower()

        # gets all languages from subpage

        for i, sub_array in enumerate(technologies):
            string = ""
            for key in sub_array:
                if (key in text):    
                    string += " " + key

            data[f'{names[i]}'] = string
            
        yield data
        yield response.follow(response.meta['original_url'], self.parse)


# https://proxy.scrapeops.io/v1/?api_key=a6c39127-0d1a-4b5e-a850-be51e7ff5e51&url=www.seek.com.au%2Fjob%2F59750070%3Ftype%3Dstandard


