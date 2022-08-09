from random import choice


class RandomWalk:
    """A class to generate random walk"""

    def __init__(self, num_points=5000):
        """Initalize attributes for a walk"""
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculating all the points in the walk"""

        # keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # decide the direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction*x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction*y_distance

            # reject moves that nowhere
            if x_step == s0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1]+x_step
            y = self.y_values[-1]+y_step

            self.x_values.append(x)
            self.y_values.append(y)
