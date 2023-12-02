with open("mydefaults.ini.txt", "r") as ini_file:
    data = ini_file.read()

characters = 0
numbers = 0

for char in data:
    if char.isalpha():
        characters += 1
    elif char.isdigit():
        numbers += 1

print(f"the number of characters is {characters}")
print(f"the number of digits is {numbers}")

with open("mydefaults.ini.txt", "x") as f:
    f.write(f"the number of characters is {characters}, and the number of digits is {numbers}")