current_movies = {'The Grinch':'11:00am',
                    'Rudolph':'1:00pm',
                    'Frosty the Snowman':'3:00pm',
                    'Christmas Vacation':'5:00pm'}

# this lady said something about making sure vscode is open
# my dictionary does not look like hers

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)

# ---------------------------------------------


breakfast = ['Egg Sandwich', 'Bagel', 'Coffee']
lunch = ['Egg Sandwich', 'Bagel', 'Coffee']
dinner = ['Soup', 'Salad', 'Spaghetti', 'Taco']

menus = [ ['Egg Sandwich', 'Bagel', 'Coffee'],
['Egg Sandwich', 'Bagel', 'Coffee'],
['Soup', 'Salad', 'Spaghetti', 'Taco'] ]

menus = { 'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
'Lunch' : ['Egg Sandwich', 'Bagel', 'Coffee'],
'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Taco'] }

for name, menu in menus.items():
    print(name, ':', menu)