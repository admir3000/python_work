pizza = ['peperoni','veggie','meats','canadian']

friends_pizza=pizza[:]

pizza.append('pinapple')
friends_pizza.append('jallapeno')

print("My favorit pizzas is:")
print(pizza)


print("\n My friends favorite pizzas is:")
print(friends_pizza) 


for pizzas in pizza:
    print(pizzas.title())
