import scrapy
import re
import random 

class JobSpider(scrapy.Spider):
    name = 'jobSpider'
    # start_urls = ['https://www.seek.com.au/software-engineer-jobs']
    # proxy_list = [
    #     "185.199.229.156:7492",
    #     "185.199.228.220:7300",
    #     "185.199.231.45:8382",
    #     "188.74.210.207:6286",
    #     "188.74.183.10:8279",
    #     "188.74.210.21:6100",
    #     "45.155.68.129:8133",
    #     "154.95.36.199:6893",
    #     "45.94.47.66:8110",
    #     "144.168.217.88:8780"
    # ]
    
    def start_requests(self):
        # proxy = random.choice(self.proxy_list)
        # proxy = f"http://letbvmwx:3i8ujr8shrwk@{proxy}"
        
        # headers = { 
        #     "accept": "*/*",
        #     "accept-encoding": "gzip, deflate, br",
        #     "accept-language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        #     "seek-request-brand": "seek",
        #     "seek-request-country": "AU",
        #     "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        # }
        
        yield scrapy.Request('https://www.seek.com.au/software-engineer-jobs', 
                    # meta = {'proxy': proxy}, 
                    # headers = headers, 
                    callback = self.parse)
    
    def parse (self, response):
        
        results = response.xpath("//*[@id='app']")
        
        for job in results.css("article"):
            subpage_link = job.css("a[data-automation='jobTitle']").attrib["href"]
            
            data = {
                'title': job.css("a[data-automation='jobTitle']::text").get(),
                'company': job.css("a[data-automation='jobCompany']::text").get(),
                'location': job.css("a[data-automation='jobLocation']::text").get(),
                'list date': job.css("span[data-automation='jobListingDate']::text").get(),
                'link': subpage_link,
            }
            
            yield response.follow(subpage_link, self.parse_subpage, 
                                  meta = {"data": data, 'original_url': response.url})
            
        # goto next page 
        next_page = response.css("a[aria-label='Next']").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_subpage (self, response):
        keywords = ["python", "java", "C#", "c++", "javascript", "ruby", "typescript", "rust", "aws", "api"]    
        inner_page = response.xpath("//*[@id='app']")
        data = response.meta["data"]
        
        # formats subpage text
        text = inner_page.css("div[data-automation='jobAdDetails'] ::text").extract()
        text = ' '.join(map(str, text))
        text = text.lower()

        # gets all keywords from subpage
        array = []
        for key in keywords:
            if (key in text): 
                array.append(key)
        
        data['keywords'] = array
            
        yield data
        yield response.follow(response.meta['original_url'], self.parse)