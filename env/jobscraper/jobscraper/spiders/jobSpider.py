import scrapy



class JobSpider(scrapy.Spider):
    name = 'jobSpider'
    start_urls = ['https://www.seek.com.au/software-engineer-jobs']
    
    def updatePageNumber(val):
        return val + 1
        
    def parse(self, response):
        languages = ["python", "java", "c#", "c++", "javascript", "ruby", "typescript", "go", "rust"]
        results = response.xpath("//*[@id='app']")
        next_page = response.css("a[aria-label='Next']").attrib["href"]
        for job in results.css("article"):
            link = response.css("a[data-automation='jobTitle']").attrib["href"]
            yield {
                'title': job.css("a[data-automation='jobTitle']::text").get(),
                'company': job.css("a[data-automation='jobCompany']::text").get(),
                'location': job.css("a[data-automation='jobLocation']::text").get(),
                'list date': job.css("span[data-automation='jobListingDate']::text").get(),
                'link': link,
            }
            yield response.follow(link)
            inner_page = response.xpath("//*[@id='app']")
            # for key in keywords:
                
            #     keywords = job.css('a[data-automation="jobAdDetails"]')
            # if (next_page[-1] == 2):
                
        # next_page = response.css("a[aria-label='Next']").attrib["href"]
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)