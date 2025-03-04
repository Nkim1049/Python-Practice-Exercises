menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

# learning about dictionaries
# creating a dictionary
menu = {
    "Pizza": "1.99",
    "Soda": "0.69",
    "Double Chunk Chocolate Chip Cookie": "2.49",
}

# updating and adding new key/value pairs to our dictionary
menu["Pizza"] = "1.99"
menu["Soda"] = "0.69'"

# deleting item from our dictionary
del menu["Double Chunk Chocolate Chip Cookie"]

# looping through a dictionary to find the number of menu
# who find a c in the class
numC = 0
for key in menu:
    if menu[key] == "C":
        numC+=1
print(numC)
 