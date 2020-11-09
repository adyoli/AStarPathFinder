import random

# Global
walls = {}
obstacles = []
stack = []
visited = []
new_obstacles = []

def check_x_y_range(x, y):

    """
    Checks if -100 < x < 100 and -200 < y < 200
    * params x
    * params y
    * returns bool == False if x or y are outside the range
    * returns bool == False if (x, y) == (0, 0)
    * returns bool == True if (x, y) is inside the range
    """

    if x == 0 and y == 0:
        return False
    if -100 < x < 100 and -200 < y < 200:
        return True
    return False


def get_neighbour_nodes(x, y):

    """
    Finds all the neihbouring nodes of a node at (x, y)
    * param x, y coordinate inside a grid
    * returns a list of all the nodes within the grid range
    """

    valid_nodes = []
    neighbour_nodes = [(x - 10, y), (x, y + 10), (x + 10, y), (x, y - 10)]
    for node in neighbour_nodes:
        if check_x_y_range(node[0], node[1]):
            valid_nodes.append(node)
    
    return valid_nodes


def create_maze():
    global stack, visited, walls, obstacles

    x = random.randrange(-90, 93, 10)
    y = random.randrange(-190, 193, 10)
    stack.append((x, y))
    visited.append((x, y))

    while len(stack) > 0:
        neighbour_nodes = [node for node in get_neighbour_nodes(x, y) \
        if node not in visited]

        if len(neighbour_nodes) > 0:
            nx, ny = random.choice(neighbour_nodes)
            walls[(x, y)] = [(x, y), (nx, ny)]
            stack.append((nx, ny))
            visited.append((nx, ny))

        else:
            (x, y) = stack.pop()
    obstacles = [walls[node] for node in walls]

    return obstacles

'''
def create_maze_obstacles(x1, y1, x2, y2):
    
    global new_obstacles

    if x1 == x2:
        x = x1
        block_1 = [x] #[(x - 5, y1), (x + 5, y1 + 5)]
        block_2 = [(x - 5, y1 + 5), (x + 5, y2)]
        
    elif y1 == y2:
        y = y1
        block_1 = [(x1, y - 5), (x1 + 5, y + 5)]
        block_2 = [(x1 + 5, y - 5), (x2, y + 5)]

    new_obstacles.append(block_1)
    new_obstacles.append(block_2)


def obs():
    for _ in create_maze():
        #print(_[0][0], _[0][1], _[1][0], _[1][0])
        create_maze_obstacles(_[0][0], _[0][1], _[1][0], _[1][1])
'''

def is_position_blocked(x, y):

    """
    Iterates through the list of generated obstacles and checks:
    * If (x, y) lies inside an obstacle
    * param x
    * param y
    * returns bool == True if x or y inside obstacle
    * returns bool == False if x and y not inside obstacle 
    """
    global obstacles

    for i in obstacles:
        x1 = i[0][0]
        x2 = i[1][0]
        y1 = i[0][1]
        y2 = i[1][1]
        
        if y1 == y2:
            if x1 < x2:
                if y == y1 and x1 <= x <= x2:
                    return True
            elif x1 > x2:
                if y == y1 and x2 <= x <= x1:
                    return True
        elif x1 == x2:
            if y1 < y2:
                if x == x1 and y1 <= y <= y2:
                    return True
            elif y1 > y2:
                if x == x1 and y2 <= y <= y1:
                    return True
    return False


def value_in_range(num):

    """
    Takes a number and returns -1 if num < 0 or +1 if num > 0
    * param num
    * returns 1 if num > 0
    * returns -1 if num < 0
    * returns0 if num == 0 
    """
    if num != 0:
        return num/abs(num)
    else:
        return 0


def is_path_blocked(x1, y1, x2, y2):

    """
    Checks if there is an (x, y) value 
    that lies inside obstacle between (x1, y1) and (x2, y2)
    * param x1, y1, x2, y2
    * Checks the direction of move, i.e (x1 == x2) or (y1 == y2)
      Then iterates through the path between the coords
    * Each iteration is passed to is_position_blocked
    * returns bool == True if path is blocked
    * returns bool == False if path is not blocked
    """
    if x1 == x2:
        i = y1
        while i != y2 + value_in_range(y2):
            if is_position_blocked(x1, i):
                return True
            else:
                if y1 > y2:
                    i -= 1
                else:
                    i += 1

    elif y1 == y2:
        i = x1
        while i != x2 + value_in_range(x2):
            if is_position_blocked(i, y1):
                return True
            else:
                if x1 > x2:
                    i -= 1
                else:
                    i += 1
    return False


