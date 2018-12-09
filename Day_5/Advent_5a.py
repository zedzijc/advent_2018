import sys


def reactive(unit, other_unit):
    return (not unit == other_unit and
            (unit.upper() == other_unit or unit.lower() == other_unit))


def get_polymer_length(instructions):
    index = 0
    units = list(instructions)
    while index < len(units) - 1:
        if reactive(units[index], units[index + 1]):
            del units[index:index + 2]
            index -= 1
            continue
        index += 1
    return len(units)


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().replace('\n', '')
    print("Polymer result: {0}".format(get_polymer_length(instructions)))
