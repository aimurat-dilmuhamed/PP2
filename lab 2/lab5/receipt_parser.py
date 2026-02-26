import re
import json

def parse_receipt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: raw.txt not found."

    # --- RegEx Patterns ---
    
    # 1. Prices: Matches digits followed by a dot/comma and two decimals (e.g., 10.99 or 5,00)
    price_pattern = r'\d+[.,]\d{2}'
    prices = re.findall(price_pattern, content)
    
    # 2. Date: Matches DD.MM.YYYY or DD/MM/YYYY
    date_pattern = r'\d{2}[./]\d{2}[./]\d{4}'
    date = re.search(date_pattern, content)
    
    # 3. Time: Matches HH:MM:SS or HH:MM
    time_pattern = r'\d{2}:\d{2}(?::\d{2})?'
    time = re.search(time_pattern, content)
    
    # 4. Payment Method: Matches keywords like Cash, Card, Debit, etc. (Case Insensitive)
    payment_pattern = r'(?i)(cash|card|debit|credit|kashpi|visa|mastercard)'
    payment_method = re.search(payment_pattern, content)

    # 5. Product Names: 
    # Usually, products are on a line followed by a price. 
    # This pattern looks for text at the start of a line followed by a price.
    product_pattern = r'^(.+?)\s+\d+[.,]\d{2}'
    products = re.findall(product_pattern, content, re.MULTILINE)

    # --- Data Processing ---
    
    # Convert prices to floats for calculation (replacing comma with dot)
    float_prices = [float(p.replace(',', '.')) for p in prices]
    total_amount = sum(float_prices[:-1]) # Often the last price is the total, check your raw.txt!

    # --- Structured Output ---
    receipt_data = {
        "items": products,
        "all_prices": float_prices,
        "total": max(float_prices) if float_prices else 0, # Usually the largest number is the total
        "date": date.group() if date else "Not found",
        "time": time.group() if time else "Not found",
        "payment_method": payment_method.group() if payment_method else "Not found"
    }

    return json.dumps(receipt_data, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    result = parse_receipt("raw.txt")
    print(result)