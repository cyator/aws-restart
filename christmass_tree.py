import random
import time
import os

# clear console (uses cls if os is windows else uses clear)
os.system('cls' if os.name == 'nt' else 'clear')
# Python program to draw a christmas tree

# Define tree size
tree_size = 12

# Define a list of colors for the tree
colors = ['\033[92m', '\033[91m', '\033[93m']

# start animation loop
while True:
    # Draw the star at top of the tree
    print(' '*(tree_size-1) + colors[2] + "*")
    print(' '*(tree_size-2) + colors[2] + "***")

    # Draw the tree
    for i in range(tree_size):
        stars = ''
        for j in range(2*i + 1):
            if j == 0:
                # set yellow for first ellement
                color = colors[2]
                # choose random colors for all other elements
            else:
                color = random.choice(colors)
            stars += color + '*'
        print(' '*(tree_size - i - 1) + stars)

    # Draw the tree stand
    stem = 3
    for i in range(stem):
        stem = color + '\033[92m'
        print(((' ' * 10) + stem) + (('#' * 3) + stem) + (('' * 4) + stem))

    # Display the message
    print('\033[91m\033[1m\nMerry Christmas!\n\033[0m')

    # Wait for a 4 seconds before reanimating
    time.sleep(4)

    # clear console (uses cls if os is windows else uses clear)
    os.system('cls' if os.name == 'nt' else 'clear')
