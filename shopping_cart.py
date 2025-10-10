foods = []
prices = []
total = 0

while True:
    food = input("Enter the food (q to quit): ")
    if food.lower()  == "q":
        break
    else:
        foods.append(food)
        price = float(input("Enter the prices: $"))
        prices.append(price)

for food in foods:
    print(food, end=" , ")

for price in prices:
    total += price

print()
print(F"Your total price is: ${total}")
