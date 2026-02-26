import re
import json

def parse_receipt(file_path):
    with open(file_path, 'r') as f:
        data = f.read()

    # 1. Extract Date and Time
    # Matches DD/MM/YYYY and HH:MM:SS
    date = re.search(r'(\d{2}/\d{2}/\d{4})', data).group(1)
    time = re.search(r'(\d{2}:\d{2}:\d{2})', data).group(1)

    # 2. Extract Product Names and Prices
    # Pattern: Matches text at start of line, then spaces, then a decimal number
    # Group 1: Product Name | Group 2: Price
    product_pattern = r'^([A-Za-z\s]+?)\s+(\d+\.\d{2})'
    items_found = re.findall(product_pattern, data, re.MULTILINE)

    products = []
    prices = []
    for item in items_found:
        name = item[0].strip()
        price = float(item[1])
        # Filter out "TOTAL AMOUNT" from the product list if it's caught
        if "TOTAL" not in name.upper():
            products.append(name)
            prices.append(price)

    # 3. Calculate Total
    total_calculated = sum(prices)

    # 4. Extract Payment Method
    # Matches word after "PAYMENT METHOD:"
    payment_match = re.search(r'PAYMENT METHOD:\s+(\w+)', data)
    payment_method = payment_match.group(1) if payment_match else "Unknown"

    # 5. Create Structured Output
    receipt_json = {
        "store_info": {
            "date": date,
            "time": time
        },
        "items": [
            {"product": p, "price": pr} for p, pr in zip(products, prices)
        ],
        "summary": {
            "total_amount": round(total_calculated, 2),
            "payment_method": payment_method
        }
    }

    return receipt_json

if __name__ == "__main__":
    result = parse_receipt("raw.txt")
    print(json.dumps(result, indent=4))