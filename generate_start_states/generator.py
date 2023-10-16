

def generate_valid_envs(num_states, width, height, num_riders, trail_length):
    """
    Generates a list of valid environments for time riders.

    Args:
        num_states (int): The number of valid environments to generate.
        width (int): The width of the environment.
        height (int): The height of the environment.
        num_riders (int): The number of time riders.
        trail_length (int): The length of each time rider's trail.

    Returns:
        list: A list of valid environments.
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
    # - an environment is a 2d array of x's, 0's, and upper and lower case letters.
    #    - x's represent spaces that are not accessible
    #    - 0's represent accessible spaces
    #    - a lower case letter represents the starting position of that time rider
    #    - an upper case letters represents the goal position of the same time rider
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
    
    
    pass

def write_env_to_file(env):
    """ 
    Writes the passed environment to a text file.

    Args:
        env: 2d array representing the environment 
    """
    pass


def main():
    pass

if __name__ == '__main__':
    main()
