import sys


def get_repeated_letter_value(instruction, occurences):
    for letter in set(instruction):
        if instruction.count(letter) == occurences:
            return 1
    return 0


def compute_checksum(instructions):
    doubles = 0
    triples = 0
    for instruction in instructions:
        doubles += get_repeated_letter_value(instruction, 2)
        triples += get_repeated_letter_value(instruction, 3)
    return doubles * triples


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Checksum found: {0}".format(compute_checksum(instructions)))
