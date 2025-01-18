# Iterating through a range of numbers
for i in range(10):  # 0 to 4
    if i == 5:
        break
    print(i)

for i in range(10): 
    if i == 5:
        continue
    print(i)

# Iterating through a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1
