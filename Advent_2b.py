import sys


def get_matching_instruction(instruction, other_instruction):
    mismatching_index = None
    index = 0
    other_instruction_as_list = list(other_instruction)
    for letter in instruction:
        if letter != other_instruction_as_list[index]:
            if mismatching_index is not None:
                return None
            mismatching_index = index
        index += 1
    if mismatching_index is not None:
        del other_instruction_as_list[mismatching_index]
        return "".join(other_instruction_as_list)
    return None


def find_instruction(instructions):
    index = len(instructions)
    for instruction in instructions:
        for other_instruction in instructions[-index:]:
            match = get_matching_instruction(instruction, other_instruction)
            if match is not None:
                return match
        index -= 1


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Checksum found: {0}".format(find_instruction(instructions)))
