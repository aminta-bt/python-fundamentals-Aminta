"""SALES SUMMARY ANALYSIS
Reads a sales CSV file and calculates sales performance.
"""

import csv

def calculate_sales_stats(csv_file):
    total_sales = 0.0
    product_sales = {}
    count = 0

    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["amount"])
            product = row["product"]
            
            total_sales += amount
            product_sales[product] = product_sales.get(product, 0.0) + amount
            count += 1

    if count == 0:
        return None

    highest_product = None
    highest_amount = 0.0

    for product, amount in product_sales.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_product = product

    return {
        "total_sales": total_sales,
        "highest_product": highest_product,
        "average_sale": total_sales / count,
    }

if __name__ == "__main__":
    try:
        results = calculate_sales_stats("sales.csv")
        if results is None:
            print("Error! The file contains no sales records.")
        else:
            print(f"Total Sales Amount: {round(results["total_sales"], 2)}")
            print(f"Product with the Highest Total Sales: {results["highest_product"]}")
            print(f"Average Sale Amount: {round(results["average_sale"], 2)}")

    except FileNotFoundError:
        print("Error! The file 'sales.csv' was not found.")