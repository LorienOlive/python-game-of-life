
#from numpy import random
#print(random.choice(2, (2, 4), p=[0.5, 0.5]))

import random

live = 1
dead = 0


def dead_state(width, height):
    return [[dead for element in range(height)] for element in range(width)]


def random_state(width, height):
    state = dead_state(width, height)
    for j in range(0, width):
        for k in range(0, height):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = live
            else:
                cell_state = dead
            state[j][k] = cell_state

    return state


print(random_state(3, 5))