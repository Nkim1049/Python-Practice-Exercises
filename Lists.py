groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

# print first item in list at index 0
print(groceries[0])

# looping through our list
num = 1
for groceries in groceries:
    print(str(num) + ". " + groceries)
    num = num + 1

# list methods

# sort our groceries alphabetically
groceries.sort()
print(groceries)

# adds item to end of list
groceries.append("")
groceries(groceries)

# removes item from end of list
groceries.pop()
print(groceries)

# removes specific item
groceries.remove("cheez its")
print(groceries)

# adds item at a specific index
groceries.insert(1, "doritos")
print(groceries)

# repacing specific items in our list
groceries[0:2] = ["cocoa puffs"]
print(groceries)


# looping through a string
name = "norah kim"
for letter in name: 
    print(letter) 