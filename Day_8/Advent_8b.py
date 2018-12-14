import sys


def prepare_input(input_string):
    return [int(digit) for digit in input_string.split()]


def get_root_value(instructions, start_index=0):
    node_value = 0
    children = instructions[start_index]
    meta_data_length = instructions[start_index + 1]
    end_offset = start_index + 2
    child_values = []

    while children > 0:
        child_results = get_root_value(instructions, end_offset)
        child_values.append(child_results[0])
        end_offset = child_results[1]
        children -= 1

    metadata_index = end_offset
    metadata_end_index = end_offset + meta_data_length
    if child_values:
        while metadata_index < metadata_end_index:
            metadata_value = instructions[metadata_index]
            if metadata_value - 1 < len(child_values):
                node_value += child_values[metadata_value - 1]
            metadata_index += 1
    else:
        while metadata_index < metadata_end_index:
            node_value += instructions[metadata_index]
            metadata_index += 1

    return (node_value, metadata_end_index)


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().replace('\n', '')
    print("Root: {0}".format(get_root_value(prepare_input(instructions))[0]))
