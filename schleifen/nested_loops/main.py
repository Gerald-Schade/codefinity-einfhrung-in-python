produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]

#Verschachtelte Schleifen
for section in groceries:
    for item in section:
        print(item)



