
avalable_topings = ['mushroom', 'olives', 'green pepers', 'peperoni', 'pineapple', 'extra cheese']

requested_topings = ['mushroom', 'french fries', 'extra cheese']


for requested_toping in requested_topings:
    if requested_toping in avalable_topings:
        print(f"Adding {requested_toping}")

    else:
        print(f"Sorry we dont have,{requested_toping}!")


print("\n Finished making your pizza") 
