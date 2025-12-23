# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Zählen wie oft appel im <tupel vorkommt
apple_count = shelf.count("apples")
banana_index = shelf.index("bananas")
print("Number of Apples:", apple_count)
print("First Banana Index:", banana_index)

#Anzahl überprüfen
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
    
shelf_count_grapes = shelf.count("grapes")
if shelf_count_grapes <= 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")


oranges_index = shelf.index("oranges")
if "oranges" in shelf:
    print("Oranges are at index:", oranges_index)
else:
    print("Oranges are out of stock.")




