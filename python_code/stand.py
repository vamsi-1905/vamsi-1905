menu = {"hotdog":30,"pizza":45,"burger":75,"soda":20}

cart = []
total = 0
print("------MENU-------")
for key,value in menu.items():
    print(f"{key}: ${value}")

while True:
    food = input("what item do you want to add?(q to quit)").lower()
    if food == "q" :
        break
    elif food not in menu.keys():
        print("enter valid item instead")
    else:
        cart.append(food)

for food in cart:
    total+= menu.get(food)
    print(food,end=" ")

print(f"total cart: {total}")

print(cart)