# Product Scraper and OpenAI Enhancer

This project scrapes product data from Nykaa (or Purplle) and uses the OpenAI API to enhance it with automatically generated categories, pricing segments, and taglines.

## Project Overview

The project consists of two main parts:

1.  **Web Scraping:** Scrapes product details (name, price, description, ratings) from Nykaa product pages using `requests` and `Beautiful Soup`.
2.  **OpenAI Enhancement:** Integrates with the OpenAI API (using `gpt-3.5-turbo-1106`) to add further information to the scraped data, including:
    *   **Category:** Assigns a product category from a predefined list (Makeup, Skin, Hair, etc.).
    *   **Pricing Segment:** Classifies the product into a pricing segment (Budget, Mid-market, Premium).
    *   **Tagline:** Generates a catchy one-line tagline for the product.

## Project Structure

```
nykaa-product-scraper/
├── README.md           <- This file: Instructions and project overview
├── requirements.txt    <- Project dependencies
├── data/               <- Directory for storing data files
│   ├── scraped_products.json    <- Output from the web scraper
│   └── enhanced_products.json   <- Output from OpenAI API integration
├── scripts/
│   ├── web_scraper.py          <- Script for scraping product data
│   └── openai_enhancer.py       <- Script for integrating with OpenAI API
└── utils/              <- Directory for utility functions
    └── __init__.py     <- Makes utils a package
    └── scraper_utils.py        <- Helper functions for web scraping
    └── openai_utils.py         <- Helper functions for OpenAI API
```

## Dependencies

*   Python 3.7+
*   `requests`
*   `beautifulsoup4`
*   `openai>=1.0.0`
*   `python-dotenv`

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Web Scraping (Nykaa/Purplle)

*   **Configuration:**
    *   Open `scripts/web_scraper.py`.
    *   Modify the `product_urls` list in the `main()` function with the actual Nykaa (or Purplle) product URLs you want to scrape.
    *   If the website structure has changed, adjust the CSS selectors in `utils/scraper_utils.py` (in the `scrape_product_page` function) accordingly.

*   **Run the scraper:**

    ```bash
    python scripts/web_scraper.py
    ```

*   **Output:** The scraped data will be saved to `data/scraped_products.json`.

### 2. OpenAI API Integration

*   **Configuration:**
    *   Create a `.env` file in the root of the project and add your OpenAI API key:

        ```
        OPENAI_API_KEY=your_api_key_here
        ```
    *   If needed, modify the prompt or function definition in `utils/openai_utils.py` to fine-tune the OpenAI API interaction.

*   **Run the enhancer:**

    ```bash
    python scripts/openai_enhancer.py
    ```

*   **Output:** The enhanced data with categories, pricing segments, and taglines will be saved to `data/enhanced_products.json`.

