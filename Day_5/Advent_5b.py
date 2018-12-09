import sys


def reactive(unit, other_unit):
    return (not unit == other_unit and
            (unit.upper() == other_unit or unit.lower() == other_unit))


def get_unique_units(instructions):
    return set([a.lower() for a in set(instructions)])


def get_shortest_polymer(instructions):
    shortest_polymer_length = len(instructions)
    for unique_unit in get_unique_units(instructions):
        reduced_instructions = instructions.replace(
            unique_unit, "").replace(unique_unit.upper(), "")
        units = list(reduced_instructions)
        index = 0
        while index < len(units) - 1:
            if reactive(units[index], units[index + 1]):
                del units[index:index + 2]
                index -= 1
                continue
            index += 1
        if len(units) < shortest_polymer_length:
            shortest_polymer_length = len(units)
    return shortest_polymer_length


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().replace('\n', '')
    print("Polymer result: {0}".format(get_shortest_polymer(instructions)))
