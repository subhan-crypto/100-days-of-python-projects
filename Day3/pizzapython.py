print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# todo: work out how much they need to pay on their choosen size
bill=0
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("you choose a wrong size.")


# todo: how much you pay if you add pepperoni
if pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

# todo: how much you pay if extra cheeze is add.
if extra_cheese == "Y":
    bill+=1
print(f"Your final bill is: ${bill}.")