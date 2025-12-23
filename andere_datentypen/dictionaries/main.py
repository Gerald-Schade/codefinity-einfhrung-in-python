#Definition eines Dictionaries
grocery_inventory = {"Milk": (113, "Dairy"), "Eggs": (116, "Dairy"), "Bread": (117, "Bakery"), "Apples": (141, "Produce")}

#Abrufen der Details des Artikkels "Bread"
bread_details = grocery_inventory.get("Bread")
print(bread_details)

#Hinzufügen eines neuen Artikels "Cookies"
grocery_inventory.update({"Cookies": (143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)

#Entfernen des Artikels "Eggs"
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)

#Ausgabe der Details von "Bread"
print("Details of Bread:", grocery_inventory["Bread"])




