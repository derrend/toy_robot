place_error_msg = 'Set robot location'

class LocationError(ValueError):
    pass

class Robot:
    def __init__(self):
        """Sets default values during object initialization.

        Args:
            No Args

        Returns:
            No Output
        """
        self.d = dict(north=('y', 1), east=('x', 1), south=('y', -1), west=('x', -1))
        self.l = list(self.d.keys())
        self.x, self.y, self.f, self.placed = 0, 0, 'NORTH', False

    def place(self, X=0, Y=0, F='north'):
        """Will put theValueError toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.

        Args:
            X   (int, required):    Default 0
            Y   (int, required):    Default 0
            F   (str, required):    Default 'north'

        Returns:
            No Output
        """
        if type(X) is not int or type(Y) is not int:
            raise TypeError('X and Y values must be type int')

        if X not in range(6) or Y not in range(6):
            raise ValueError('X and Y values must be within range 0-5')

        if type(F) is not str:
            raise TypeError('F must be type str')

        if F.lower() not in self.l:
            raise ValueError('F value must be in [north, east, south, west]')

        self.x, self.y, self.f = X, Y, F.lower()
        self.placed = True

    def move(self):
        """Will move the toy robot one unit forward in the direction it is currently facing.

        Args:
            No Args

        Returns:
            No Output
        """
        if not self.placed:
            raise LocationError(place_error_msg)

        if self.d[self.f][0] is 'y':
            if self.y + self.d[self.f][1] not in range(6):
                raise ValueError('Y values must be within range 0-5')

            self.y += self.d[self.f][1]

        if self.d[self.f][0] is 'x':
            if self.x + self.d[self.f][1] not in range(6):
                raise ValueError('X values must be within range 0-5')

            self.x += self.d[self.f][1]

    def left(self):
        """Will rotate the robot 90 degrees to the left without changing the position of the robot.

        Args:
            No Args

        Returns:
            No Output
        """
        if not self.placed:
            raise LocationError(place_error_msg)

        self.f = self.l[self.l.index(self.f) - 1]

    def right(self):
        """Will rotate the robot 90 degrees to the right without changing the position of the robot.

        Args:
            No Args

        Returns:
            No Output
        """
        if not self.placed:
            raise LocationError(place_error_msg)

        try:
            self.f = self.l[self.l.index(self.f) + 1]
        except IndexError:
            self.f = self.l[0]

    def report(self):
        """Will announce the X,Y and F of the robot.

        Args:
            No Args

        Returns:
            dict:   Key value dictionary
        """
        if not self.placed:
            raise LocationError(place_error_msg)

        return dict(X=self.x, Y=self.y, F=self.f.upper())
