from robot import Robot, LocationError
from random import randint

def random_walk():
    """Send the robot on a journey until it receives an invalid command.

    Args:
        No Args

    Returns:
        dict:   Iterated list of key value dictionaries
    """
    try:
        r = Robot()
        r.place()
        for i in range(100):
            rand = randint(1, 3)
            if rand is 1:
                r.move()
            elif rand is 2:
                r.left()
            elif rand is 3:
                r.right()
            print(i, r.report())

    except LocationError as e:
        print('LocationError: {}'.format(e))

    except ValueError as e:
        print('ValueError: {}'.format(e))

    except TypeError as e:
        print('TypeError: {}'.format(e))


if __name__ == '__main__':
    random_walk()
