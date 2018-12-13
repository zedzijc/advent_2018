import sys


class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_distance(self, x, y):
        return (abs(self.x - x) +
                abs(self.y - y))


def get_coordinates(instructions):
    coordinates = []
    for line in instructions:
        x, y = line.replace(" ", "").split(",")
        coordinates.append(Coordinate(int(x), int(y)))
    return coordinates


def get_edge_coordinates(coordinates):
    western = northern = eastern = southern = coordinates[0]

    for coordinate in coordinates[-len(coordinates) - 1:]:
        if coordinate.get_x() < western.get_x():
            western = coordinate
        elif coordinate.get_x() > eastern.get_x():
            eastern = coordinate
        if coordinate.get_y() > northern.get_y():
            northern = coordinate
        elif coordinate.get_y() < southern.get_y():
            southern = coordinate
    return western, northern, eastern, southern


def get_region_size(instructions):

    def get_accumulated_distance(x, y):
        total_distance = 0
        for coordinate in coordinates:
            total_distance += coordinate.get_distance(x_index, y_index)
        return total_distance
    coordinates = get_coordinates(instructions)
    western, northern, eastern, southern = get_edge_coordinates(coordinates)
    region_size = 0
    for x_index in range(eastern.get_x()):
        for y_index in range(northern.get_y()):
            if get_accumulated_distance(x_index, y_index) < 10000:
                region_size += 1

    return region_size


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Region size: {0}".format(get_region_size(instructions)))
