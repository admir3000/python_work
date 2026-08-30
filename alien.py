#alien_0 = {'color': 'green', 'points': 5}
alien_0 = {}

#print(alien_0['color'])
#print(alien_0['points'])

#new_points = alien_0['points']
#print(f"You just earned {new_points} points!")


#print(alien_0)

alien_0['x_position'] =0
alien_0['y_position']=25
alien_0['speed'] = 'medium'

print(alien_0)

print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_incraments = 1 
elif alien_0['speed'] =='medium':
    x_incraments = 2 

else:
    # This must be fast alien 
    x_incraments = 3

# The new positiom is the old position plus the incrunents.
alien_0['x_position'] = alien_0['x_position'] + x_incraments

print (f"New postion : {alien_0['x_position']}")




