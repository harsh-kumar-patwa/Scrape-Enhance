import requests
from bs4 import BeautifulSoup
import time
import re

# def save_soup_to_file(soup, filename='soup_output.txt'):
#     try:
#         with open(filename, 'w', encoding='utf-8', errors='replace') as f:
#             f.write(str(soup))
#     except Exception as e:
#         print(f"Error saving soup to file: {e}")


def scrape_product_page(url, session):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = session.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        # save_soup_to_file(soup.prettify())

        product_name = soup.find('h1', class_='css-1gc4x7i').text.strip()
        price = soup.find('span', class_='css-1jczs19').text.strip()
        price = re.sub(r'[^\d]', '', price) 
        ratings_element = soup.find('div', class_='css-1hvvm95').text.strip()
        potential_desc =  soup.find_all('script')
        for i in potential_desc:
            if "window.__INITIAL_STATE__" in str(i):
                potential_desc = str(i)
                break

        potential_desc = str(potential_desc)

        # if text description is present then extracting else if image description is present then adding no description
        if "<p>" in potential_desc and "</p>" in potential_desc:
            product_description = potential_desc.split("<p>")[1].split("</p>")[0]
        else:
            product_description = "No description"


        time.sleep(2) 

        return {
            'product_name': product_name,
            'price': price,
            'product_description': product_description,
            'num_ratings': ratings_element,
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
    except Exception as e:
        print(f"Error parsing data from {url}: {e}")
    return None