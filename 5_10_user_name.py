
current_users = ['Pookie', 'Kiko', 'Mujo', 'Ado', 'Alen']

new_users = ['Pookie', 'Mom', 'Adam', 'Julie','Ado', 'Sam']



for current_user in current_users:
    if current_user in new_users:
        print (f"User {current_user} hase been used!")
    else:
        print (f"User {current_user} is avalable")
