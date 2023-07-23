import os
import json
import time
import random
import scrapy
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('.env.local'))

MAIN_FILE_PATH = os.getenv('MAIN_FILE_PATH')
COUNTIES_DIR_PATH = os.getenv('COUNTIES_DIR_PATH')

class DownloadPdfSpider(scrapy.Spider):
    name = "download_pdf"
    city_downloads = 0

    def __init__(self, cities=None, *args, **kwargs):
        super(DownloadPdfSpider, self).__init__(*args, **kwargs)
        # self.start_urls = urls or []
        self.cities = cities
    
    def start_requests(self):
        filtered_cities = list(filter(lambda x: x["planning_agency"] in ["SACOG"] and x["county"], self.cities))
        print(len(filtered_cities))

        for city in filtered_cities:
            city_name = city["city"]
            county_name = city["county"]
            urls = city["housing_element"]
            destination = COUNTIES_DIR_PATH + f"/{county_name}/cities/{city_name}"
            os.makedirs(destination, exist_ok=True)
            # if city["city"] == "West Sacramento":
            
            for url in urls:
                file_url = os.path.join(destination, "input", url.split("/")[-1])
                if not os.path.exists(file_url):
                    yield scrapy.Request(url=url, meta={'city': city})
                else:
                    print("Skipping. " + file_url + " already exists.")
            self.city_downloads = self.city_downloads + 1
        print(self.city_downloads)
        

    def parse(self, response):
        url = response.url
        city = response.meta.get('city')
        city_name = city["city"]
        county_name = city["county"]

        
        folder_path = os.path.join(COUNTIES_DIR_PATH, county_name, "cities", city_name, "input")
        os.makedirs(folder_path, exist_ok=True)
        file_name = url.split("/")[-1]  # Extract the file name from the URL
        file_path = folder_path + "/" + file_name # The desired download path

        with open(file_path, "xb") as f:
            f.write(response.body)
        
        delay = random.uniform(4, 11)  # Random delay between 2 to 6 seconds
        time.sleep(delay)

if __name__ == "__main__":
    with open(MAIN_FILE_PATH, 'r') as file:
        data = json.load(file)

    # urls = 0
    # filtered_cities = list(filter(lambda x: x["planning_agency"] in ["SACOG", "ABAG"] and x["county"], data))
    # for city in filtered_cities:
    #     urls = urls + len(city["housing_element"])
    # print(urls)
    # Create Scrapy settings object
    settings = Settings()
    settings.set("DOWNLOAD_TIMEOUT", 600)  # Increase the timeout to 300 seconds (5 minutes)

    process = CrawlerProcess(settings=settings)
    process.crawl(DownloadPdfSpider, cities=data)
    process.start()