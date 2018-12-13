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


def get_closest_coordinate(coordinates, x, y, max_distance):
        shortest_distance = max_distance
        shared = False
        closest = None

        for coordinate in coordinates:
            distance = coordinate.get_distance(x, y)
            if distance == shortest_distance:
                shared = True
            elif distance < shortest_distance:
                shared = False
                shortest_distance = distance
                closest = coordinate
        return closest if not shared else None


def get_infinite_area_coordinates(coordinates):
    """
    Any coordinate that is the closest coordinate for a point outside
    of manhattan will have an infinite area.
    Checks every position just outside the border that
    the eastern-southern-western-northern-most coordinates form.
    """
    western, northern, eastern, southern = get_edge_coordinates(coordinates)
    infinite_area_coordinates = set()

    x_indexes = [western.get_x() - 1, eastern.get_x() + 1]
    for x in x_indexes:
        for y in range(southern.get_y() - 1, northern.get_y() + 1):
            closest_coordinate = get_closest_coordinate(coordinates, x, y,
                                                        eastern.get_x() +
                                                        northern.get_y())
            if closest_coordinate is not None:
                infinite_area_coordinates.add(closest_coordinate)

    y_indexes = [southern.get_y() - 1, northern.get_y() + 1]
    for y in y_indexes:
        for x in range(western.get_x() - 1, eastern.get_x() + 1):
            closest_coordinate = get_closest_coordinate(coordinates, x, y,
                                                        eastern.get_x() +
                                                        northern.get_y())
            if closest_coordinate is not None:
                infinite_area_coordinates.add(closest_coordinate)

    return infinite_area_coordinates


def get_areas(coordinates):

    western, northern, eastern, southern = get_edge_coordinates(coordinates)
    areas = {}
    for x in range(eastern.get_x()):
        for y in range(northern.get_y()):
            closest_coordinate = get_closest_coordinate(coordinates, x, y,
                                                        eastern.get_x() +
                                                        northern.get_y())
            if closest_coordinate not in areas:
                areas[closest_coordinate] = 1
            else:
                areas[closest_coordinate] += 1
    return areas


def find_largest_area(instructions):
    coordinates = get_coordinates(instructions)
    areas = get_areas(coordinates)
    for infinite_area_coordinate in get_infinite_area_coordinates(coordinates):
        areas.pop(infinite_area_coordinate)
    return max(areas.values())


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Largest area: {0}".format(find_largest_area(instructions)))
