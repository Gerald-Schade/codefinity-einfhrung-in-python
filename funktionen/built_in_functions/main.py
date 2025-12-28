# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

#Umwandlung der [Liste ] in items!
for product, daten in products.items():
    daten_price = float(daten[0])
    daten_value = int(daten[1])
    total_sales = daten_price * daten_value
    total_sales_list.append(total_sales)
    total_sum = sum(total_sales_list)
    min_sales = min(total_sales_list)
    max_sales = max(total_sales_list)
#print(total_sum)
    #print(products, daten, daten_price, daten_value, product_total)
#print(total_sales_list)
    
#print(min(total_sales_list))
#print(max(total_sales_list))

    print(f"Total sales for {product}: ${total_sales}")
print("Total sum of all sales: $",(total_sum))
print("Minimum sales: $",(min_sales))
print("Maximum sales: $",(max_sales))