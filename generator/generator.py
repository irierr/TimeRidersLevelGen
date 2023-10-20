import numpy as np
import random
import os

def generate_valid_env(width, height, num_riders, trail_length, seed) -> np.ndarray:
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
    # TODO: Implement function logic

    # some notes about the game logic below:
    # - the game is played on a 2d grid
    # - the game is played by multiple time riders, each with their own starting position and goal position
    # - the goal of the game is for each time rider to reach their goal position without colliding with another time rider
    # - a time rider can move forward, left, or right, but not backwards or diagonally
    # - a time rider cannot move into a space occupied by another time rider
    # - a time rider cannot move into a space occupied by an obstacle
    # - a time rider cannot move into a space occupied by another time rider's goal position
    # - a time rider cannot move into a space occupied by another time rider's starting position
    # - a time rider cannot move into a space occupied by another time rider's trail
    # - an environment is a 2d array of 1's, 0's, and upper (in int form) and lower case (in int form) letters.
    #    - 1's represent spaces that are not accessible
    #    - 0's represent accessible spaces
    #    - a lower case letter (in its int form) represents the starting position of that time rider
    #    - an upper case letters (in its int form) represents the goal position of the same time rider
    # - an environment is valid if:
    #    - it has at least one starting position and one goal position
    #    - it has at least one accessible space for each time rider
    #    - each time rider's goal position is accessible without moving through another time rider's starting position, goal position, or trail and without moving through an obstacle
    #    - each time rider's starting position and goal position are not the same
    #    - each time rider's starting position and goal position are not the same as another time rider's starting position or goal position

    # so to generate a valid environment, we need to:
    # - randomly generate a 2d array of x's and 0's
    # - randomly generate a starting position for each time rider
    # - randomly generate a goal position for each time rider
    # - check that the environment is valid
    # - if the environment is valid, add it to the list of valid environments
    # - repeat until we have the desired number of valid environments

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
    env = generate_valid_env(10, 10, 2, 3, 10)
    print(env)
    env_str = convert_env_to_str(env)
    print(env_str)
    write_env_to_file(env_str, 'test')

if __name__ == '__main__':
    main()
