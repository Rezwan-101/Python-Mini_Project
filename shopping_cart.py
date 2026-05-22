foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quite): ")
    if food.lower() == "q":
        print("THANK YOU FOR SHOPPING WITH US!")
        break
    else:
        price = input(f"Enter the price of a {food}: $")
        foods.append(food)
        prices.append(float(price))

print("===== YOUR CART ====")

for x in foods:
    print(x)

for y in prices:
    total += y

print(f"Your total is: {total}$")

