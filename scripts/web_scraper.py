import requests
import concurrent.futures
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.scraper_utils import scrape_product_page  
from openai_enhancer import openai_enhancer  

def main():
    product_urls = [
        "https://www.nykaa.com/bombay-shaving-company-eau-de-parfum-cairo/p/10787835?productId=10787835&pps=23",
        "https://www.nykaa.com/philips-hair-dryer-hp8100-46/p/1041154?productId=1041154&pps=9",
        "https://www.nykaa.com/zaveri-pearls-pink-austrian-diamonds-pearls-necklace-earring-ring-set-zpfk17286/p/14336014?productId=14336014&pps=1",
        "https://www.nykaa.com/wommune-keto-slim-tablets/p/7681549?productId=7681549&pps=15",
        "https://www.nykaa.com/pilgrim-squalane-roll-on-under-eye-eream-serum-with-phyto-retinol-caffeine/p/5171430?productId=5171430&pps=20",
        "https://www.nykaa.com/dove-daily-shine-shampoo-conf/p/5940?productId=5940&pps=11&skuId=774838",
        "https://www.nykaa.com/beardo-chrome-beast-multipurpose-trimmer-set-for-men/p/13221378?productId=13221378&pps=1"
    ]

    scraped_data = []

    with requests.Session() as session:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for url in product_urls:
                futures.append(executor.submit(scrape_product_page, url, session))

            for future in concurrent.futures.as_completed(futures):
                data = future.result()
                if data:
                    scraped_data.append(data)
                else:
                    print(f"Error scraping URL {url}")

    with open('data/scraped_products.json', 'w') as f:
        json.dump(scraped_data, f, indent=4)

    print("Scraping is completed and Data is saved in data/scraped_products.json")

    openai_enhancer()

if __name__ == "__main__":
    main()