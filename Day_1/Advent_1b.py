import sys


def find_repeated_frequency(instructions):
    frequency = 0
    previous_frequencies = set()
    while True:
        for instruction in instructions:
            frequency += int(instruction)
            if frequency in previous_frequencies:
                return frequency
            previous_frequencies.add(frequency)


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Frequency is: {0}".format(find_repeated_frequency(instructions)))
