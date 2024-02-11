fish = ["Flounder", "Sole", "Blue Cod", "Snapper", "Terakihi", "John Dory", "Red Cod"]
print("A. First letter of each fish name: ")
for string in fish:
    print(string[0])
print()
print("B. First three letters of each fish name: ")
for string in fish:
    print(string[0], string[1], string[2])
print()

print(f"C. The longest name fish name is: ")
print(max(fish, key=len))
print()

print("D. Fish names with more than one word: ")
for string in fish:
    if ' ' in string:
        print(string)
print()

print("E. Fish names that contain the word cod:")
for g in fish:
    if 'cod' in g:
        print(g)


