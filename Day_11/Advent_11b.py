TOTAL_GRID_SIZE = 300


def get_hundredth_digit(number):
    if number > 99:
        return int(list(str(number))[-3])
    return 0


def get_coordinate(grid_serial_number, grid_size):
    grid = []
    max_power = 0
    max_power_coords = None
    y = TOTAL_GRID_SIZE
    while y > 0:
        x = TOTAL_GRID_SIZE
        row = []
        neighbour_powers = [0 for x in range(grid_size - 1)]
        while x > 0:
            rack_id = x + 10
            power = get_hundredth_digit(
                ((rack_id * y) + grid_serial_number) * rack_id) - 5
            total_power = power
            for neighbour_power in neighbour_powers:
                total_power += neighbour_power
            row.append(total_power)
            neighbour_powers.insert(0, power)
            del neighbour_powers[-1]
            if len(grid) >= grid_size - 1:
                y_index = 1
                while y_index < grid_size:
                    total_power += grid[TOTAL_GRID_SIZE - y - y_index][x - 1]
                    y_index += 1
                if total_power > max_power:
                    max_power = total_power
                    max_power_coords = (x, y)
            x -= 1
        grid.append(row[::-1])
        y -= 1
    return max_power, max_power_coords


def get_coordinate_variable_size(grid_serial_number):
    max_power = 0
    max_power_coords = None
    max_power_size = None
    #  By plotting the grid it seems that large grids > 30 turn negative.
    #  Therefore, a limited set of grid-sizes is run and is sufficient
    #  in order to find our answer.
    #  Without this observation the logic would have had to be improved
    #  in order to allow for reasonable execution speeds for large grid-sizes.
    for i in range(1, 35):
        result = get_coordinate(grid_serial_number, i)
        if result[0] > max_power:
            max_power_coords = result[1]
            max_power = result[0]
            max_power_size = i
    return max_power_coords, max_power_size


if __name__ == "__main__":
    print("Coordinates: {0}".format(get_coordinate_variable_size(1308)))
