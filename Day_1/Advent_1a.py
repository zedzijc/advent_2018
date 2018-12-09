import sys


def compute_frequency(instructions):
    frequency = 0
    for instruction in instructions:
        frequency += int(instruction)
    return frequency


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("The frequency is: {0}".format(compute_frequency(instructions)))
