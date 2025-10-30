import random

x =0
while x<3:
     y = input("rock paper scissor go").split()[-1]
     options = ("rock","paper","scissor")
     option = random.choice(options)
     print(option)
     if option == "rock" and y == "scissor":
         print("you lose")
         x+=1
     elif option == "paper" and y == "rock":
         print("you lose")
         x+=1
     elif option == "scissor" and y == "paper":
         print("you lose")
         x+=1
     elif option == y:
         print("you drew")
         x+=1
     else:
         print("you win")
         x+=1


