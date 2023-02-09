fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]

print("a. First letter of each fish name on a new line:")
for item in fish:
    print(item[0])

print("b. First 3 letters of each fish name: ")
for item in fish:
    print(item[:3])

print("c. print the longest fish name: ")
largest = ""
for item in fish:
    if len(item) > len(largest):
        largest = item
print(largest)

print("d. print out any fish with more than one word: ")
for item in fish:
    if " " in item:
        print(item)

print("e. If fish contains cod print: ")
for item in fish:
    if "cod" in item:
        print(item)
