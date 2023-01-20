# Seek.com.au "Software Engineer" web scraper
This project is a web scraper built using the Scrapy framework in Python. Its purpose is to scrape job postings from a website and extract information such as the job title, company, location, and list date. Additionally, it will categorize the job postings based on certain keywords and technologies mentioned in the posting, such as programming languages, cloud technologies, devops tools, and databases. The collected data will then be stored in a SQL database, specifically SQLite, and can be further visualized and analyzed using data visualization tools such as Tableau. The overall goal of this project is to provide valuable insights into the popular technologies used in Australia and to 
aid my search for a job. 

# Installation 
**Prerequisities**
- Python3
- Scrapy
- SQLite

`git clone https://github.com/Donnie-1/Job-Scraper`

`pip install scrapy`

`sqlite3 database.db`

**Run the spider**

`cd Job-Scraper/jobscraper`

`scrapy crawl jobSpider`

# Categorization
The data is being categorized by identifying certain keywords and technologies mentioned in the job postings. These keywords and technologies are pre-determined and stored in separate arrays such as "languages", "cloud", "devops", "web_frameworks", "database", "data", "soft-skills". When the scraper extracts the job description, it will use these arrays to check for any mentions of the keywords or technologies. If a match is found, the job posting will be categorized under that specific technology. For example, if the job posting mentions the word "Python" in the job description, it will be categorized under "languages" with python as the value. The same process applies for the other arrays of technologies. This way the job postings will be categorized into the specific technologies they are related to, making it easier to analyze the data and get insights about the job market for those technologies.

# Visualization
Tableau was used to visualize the data where it was broken up into major cities to see how the 
technologies used changed based ones location. 
The visualization can be found at 
https://public.tableau.com/app/profile/sa8644/viz/SeekSoftwareEngineerjobs/Dashboard1?publish=yes

