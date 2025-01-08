import json
import openai

def categorize_product(product_data):
    prompt = f"""
    Categorize the following product:
    Name: {product_data['product_name']}
    Price: {product_data['price']}
    Description: {product_data['product_description']}

    Assign the following:
    - Category (choose from: Makeup, Skin, Hair, Appliances, Bath & Body, Natural, Mom & Baby, Health & Wellness, Men, Fragrance, Lingerie & Accessories)
    - Pricing Segment (choose from: Budget, Mid-market, Premium)
    - A 1-line Tagline for the product
    """

    tools = [
        {
            "type": "function",
            "function": {
                "name": "categorize_and_tag",
                "description": "Categorizes a product and provides a tagline",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category of the product",
                            "enum": ["Makeup", "Skin", "Hair", "Appliances", "Bath & Body", "Natural", "Mom & Baby", "Health & Wellness", "Men", "Fragrance", "Lingerie & Accessories"]
                        },
                        "pricing_segment": {
                            "type": "string",
                            "description": "The pricing segment of the product",
                            "enum": ["Budget", "Mid-market", "Premium"]
                        },
                        "tagline": {
                            "type": "string",
                            "description": "A catchy 1-line tagline for the product"
                        }
                    },
                    "required": ["category", "pricing_segment", "tagline"]
                }
            }
        }
    ]

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": prompt}],
            tools=tools,
            tool_choice="auto"
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        if tool_calls:
            for tool_call in tool_calls:
                function_args = json.loads(tool_call.function.arguments)
                return function_args
        else:
            return {"error": "No tool calls found in response"}

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return {"error": str(e)}