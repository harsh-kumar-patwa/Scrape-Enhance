import json
import openai
import os
from dotenv import load_dotenv
from utils.openai_utils import categorize_product

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def openai_enhancer():
    with open('data/scraped_products.json', 'r') as f:
        scraped_data = json.load(f)

    enhanced_data = []

    for product in scraped_data:
        categorized_product_data = categorize_product(product)
        if "error" not in categorized_product_data:
            enhanced_product = {**product, **categorized_product_data} # I am saving both the product and the enhanced data
            enhanced_data.append(enhanced_product)
        else:
            print(f"Skipping product due to error: {product['product_name']}")

    with open('data/enhanced_products.json', 'w') as f:
        json.dump(enhanced_data, f, indent=4)

    print("Enhanced data is saved in data/enhanced_products.json")

if __name__ == "__main__":
    openai_enhancer()
