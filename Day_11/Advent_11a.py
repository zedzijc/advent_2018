GRID_SIZE = 300


def get_hundredth_digit(number):
    if number > 99:
        return int(list(str(number))[-3])
    return 0


def get_coordinate(grid_serial_number):
    grid = []
    max_power = 0
    max_power_coords = None
    y = GRID_SIZE
    while y > 0:
        x = GRID_SIZE
        row = []
        next_x_power = next_next_x_power = 0
        while x > 0:
            rack_id = x + 10
            power = get_hundredth_digit(
                ((rack_id * y) + grid_serial_number) * rack_id) - 5
            x_power = power + next_x_power + next_next_x_power
            row.append(x_power)
            next_next_x_power = next_x_power
            next_x_power = power
            if len(grid) > 1:
                total_power = (x_power +
                               grid[GRID_SIZE - y - 1][x - 1] +
                               grid[GRID_SIZE - y - 2][x - 1])
                if total_power > max_power:
                    max_power = total_power
                    max_power_coords = (x, y)
            x -= 1
        grid.append(row[::-1])
        y -= 1
    return max_power_coords


if __name__ == "__main__":
    print("Coordinates: {0}".format(get_coordinate(1308)))
