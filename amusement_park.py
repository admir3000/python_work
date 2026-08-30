

age=49
if age < 4:
#    print("Your admition cost is $0.")
    price = 0 
elif age < 18:
#    print("Your admition cost $25.")
    price = 25
elif age >= 65:
    price = 20
else:
#    print("Your admition cost $40.")
    price = 40 

print(f"Your admition cost is ${price}.")
