import numpy as np
import random
import os
from typing import Union

def generate_path(env, start, goal, trail_length) -> Union[np.ndarray, None]:
    """
    Generates a path from the start position to the goal position.

    Args:
        env (np.ndarray): 2d array representing the environment in int form
        start (tuple): The starting position of the path.
        goal (tuple): The goal position of the path.
        trail_length (int): The length of the path.

    Returns:
        path (np.ndarray): 2d array representing the path in int form.
    """
    path = np.copy(env)
    trail = []
    current = start
    while current != goal:
        # get the next position in the path
        next = get_next_position(env, path, current, goal, trail)

        # if the next position is the goal, break
        if next == goal:
            break

        # if there is no next position, the path is invalid
        if next is None:
            return None

        # set the next position in the path
        path[next] = 1

        # update the trail but limit it to the trail length
        trail.append(current)
        if len(trail) > trail_length:
            trail.pop(0)

        # update the current position
        current = next

    return path

def get_next_position(env, path, current, goal, trail) -> Union[tuple, None]:
    """
    Gets the next position in the path.

    Args:
        env (np.ndarray): 2d array representing the environment in int form
        path (np.ndarray): 2d array representing the path in int form
        current (tuple): The current position in the path.
        goal (tuple): The goal position of the path.
        trail_length (int): The length of the path.

    Returns:
        next (tuple): The next position in the path.
    """
    # make empty list for possible next positions
    poss_next_positions = []
    # get the next positions
    for next_pos in next_positions(env, current):
        # if the next position is the goal add it to the list of possible next positions then break
        if next_pos == goal:
            poss_next_positions.append(next_pos)
            break
        # if the next position is not in the path or is in the trail, add it to the list of possible next positions
        # also check that the next position is not a start or goal position for another time rider
        next_pos_val = path[next_pos]
        if next_pos_val == 0 or (next_pos not in trail and next_pos_val == 1):
            poss_next_positions.append(next_pos)


    # if there are no possible next positions, return None
    if len(poss_next_positions) == 0:
        return None

    # if there is only one possible next position, return it
    if len(poss_next_positions) == 1:
        return poss_next_positions[0]

    # if goal is in the list of possible next positions, return it
    if goal in poss_next_positions:
        return goal

    # if there is more than one possible next position, return a random one
    return random.choice(poss_next_positions)


def next_positions(env: np.ndarray, current: tuple[int, int]):
    """
    A generator function that iterates over each direction and returns the next position from the current one.

    Args:
        env (np.ndarray): 2d array representing the environment in int form
        current (tuple): The current position in the path.

    Yields:
        next (tuple): The next position in the path.
    """
    x, y = current
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for (dx, dy) in possible_moves:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < env.shape[0] and 0 <= next_y < env.shape[1]:
            yield (next_x, next_y)

def generate_valid_env(width, height, num_riders, trail_length, seed=None) -> Union[np.ndarray, None]:
    """
    Generates a valid environments for time riders.

    Args:
        num_states (int): The number of valid environments to generate.
        width (int): The width of the environment.
        height (int): The height of the environment.
        num_riders (int): The number of time riders.
        trail_length (int): The length of each time rider's trail.

    Returns:
        list: A valid time riders environment.
    """
    # set the random seed
    random.seed(seed)
    
    # initialize the environment
    env = np.zeros((width, height), dtype=int)

    # generate the start and goal positions for each time rider
    coordinates = set()
    while len(coordinates) < num_riders * 2:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        coordinates.add((x, y))
    
    # add the coordinates to the environment, starting with the start positions (start from 65) and then the goal positions (start from 97)
    for i, (x, y) in enumerate(coordinates):
        env[x, y] = i + 65 if i < num_riders else i-num_riders + 97
        
    # generate the paths for each time rider
    for i in range(num_riders):
        # get the start and goal positions for the current time rider
        start = np.where(env == i + 65)
        goal = np.where(env == i + 97)
        # add the start and goal positions to the environment
        env[start] = i + 65
        env[goal] = i + 97
        # generate the path for the current time rider
        path = generate_path(env, start, goal, trail_length)

        # if the path is None, the configuration is unsolvable so return None
        if path is None:
            return None
        
        # add the path to the environment
        env = np.where(path > 0, path, env)
        

    return env

def convert_env_to_str(env) -> str:
    """ 
    Converts the passed environment to a string representation.

    Args:
        env (np.ndarray): 2d array representing the environment in int form

    Returns:
        env_str (str): A string representation of the environment.
    """
    # copy the env into a 2d array of strings so we can replace the ints with their string representations
    env_str = ""
    for row in env:
        for cell in row:
            if cell == 0 or cell == 1:
                env_str += str(cell)
            else: 
                env_str += chr(cell)
        env_str += '\n'
    return env_str

def write_env_to_file(env, path, filename='env.txt'):
    """ 
    Writes the passed environment to a text file.

    Args:
        env (str): A text representation of the environment. 
        path (str): The path to the directory where the file will be written.
        filename (str): The name of the file to write to. Defaults to 'env.txt'.
    """
    # create the full file path
    full_path =  path + '/' + filename

    # create the directory if it doesn't exist
    os.makedirs(path, exist_ok=True)

    # write the environment to the file
    with open(full_path, 'w') as f:
        f.write(env)


def main():
    env = generate_valid_env(10, 10, 3, 4)
    if env is None:
        print('No valid environment could be generated.')
        return
    print(env)
    env_str = convert_env_to_str(env)
    print(env_str)
    write_env_to_file(env_str, 'test')

# run generate valid env function 100 times and record the number of valid environments generated
def test_generate_valid_env(rep=10000):
    num_valid_envs = 0
    for i in range(1000):
        env = generate_valid_env(10, 10, 3, 4)
        if env is not None:
            num_valid_envs += 1
    # get the percentage of valid environments generated
    num_valid_envs = num_valid_envs / rep * 100
    print(f"percentage of environments generated that are valid: {num_valid_envs}%")

if __name__ == '__main__':
    test_generate_valid_env(1000)
