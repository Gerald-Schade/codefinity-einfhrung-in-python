#Dictionary erstellen
grocery_inventory = {"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}
print(grocery_inventory["Eggs"] [1])

#Preis prüfen und aktualisieren
if (grocery_inventory["Eggs"] [1]) > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = ("Dairy", 4.50, 30)
else:
    print("The price of Eggs is reasonable.")

#Neuen Artikel hinzufügen
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

#Bestand verwalten
if grocery_inventory["Milk"] [2] < 10:
    grocery_inventory["Milk"] = ("Dairy", 3.50, 28)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

#Artikel nach Preis entfernen
if grocery_inventory["Apples"] [1] > 2:
    grocery_inventory.pop("Appeles")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:", grocery_inventory)




