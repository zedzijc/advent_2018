import sys
import re


class Point(object):

    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def move(self, steps=1):
        self.x_position += self.x_velocity * steps
        self.y_position += self.y_velocity * steps

    def get_x(self):
        return self.x_position

    def get_x_velocity(self):
        return self.x_velocity

    def get_y_velocity(self):
        return self.y_velocity

    def get_y(self):
        return self.y_position


def get_points(instructions):
    """
    Parses the input into Point objects
    """
    points = []
    for line in instructions:
        match = re.match(r'position=<\s?(-?\d*),\s*(-?\d*)>'
                         r' velocity=<\s?(-?\d*),\s*(-?\d*)>', line)
        points.append(Point(int(match[1]), int(match[2]),
                            int(match[3]), int(match[4])))
    return points


def get_empty_canvas(width, height):
    return [["." for x in range(width)] for x in range(height)]


def gather_points(points):
    """
    Iterates over a range of steps to find the lowest distance in y
    among all points. This is where our result will be found.
    """
    y_data = [100000, 0]  # [lowest difference, iteration where it was found]

    for steps in range(9000, 11000):  # The eye-test suggests ~ 10,000
        y_max = 0
        y_min = 1000000
        for point in points:
            y = point.get_y() + point.get_y_velocity() * steps
            if y < y_min:
                y_min = y
            elif y > y_max:
                y_max = y
        if y_max - y_min < y_data[0]:
            y_data[0] = y_max - y_min
            y_data[1] = steps
    for point in points:
        point.move(steps=y_data[1])


def find_message(instructions):
    points = get_points(instructions)
    gather_points(points)
    width = 80
    height = 20
    text_offset = 160  # Our result is based just outside the 160,160 region.
    canvas = get_empty_canvas(width, height)
    for point in points:
        canvas[point.get_y() - text_offset][point.get_x() - text_offset] = "#"
    for line in canvas:
        print("".join(line))


if __name__ == "__main__":
    find_message(open(sys.argv[1]).read().splitlines())
