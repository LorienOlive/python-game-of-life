live = 1
dead = 0


def dead_state(width, height):
    return [[dead for element in range(height)] for element in range(width)]

width = 4
height = 6
print(dead_state(width, height))