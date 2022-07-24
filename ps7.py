import random

# I didn't like how the lesson didn't give the individual dice rolls
# so I made it display each

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dice_total = die1 + die2
    return [die1, die2, dice_total]


player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")

roll1 = roll_dice()
roll2 = roll_dice()

print(player1, 'rolled', roll1[0], 'and', roll1[1], 'for a total of', roll1[2])
print(player2, 'rolled', roll2[0], 'and', roll2[1], 'for a total of', roll2[2])

if roll1[2] > roll2[2]:
    print(player1, 'wins!')
elif roll2[2] > roll1[2]:
    print(player2, 'wins!')
else:
    print('You tie!')

# I like mine better, but it won't run in a function like hers did :/