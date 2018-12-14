import sys


def prepare_input(input_string):
    return [int(digit) for digit in input_string.split()]


def sum_metadata(instructions, start_index=0):
    metadata_sum = 0
    children = instructions[start_index]
    meta_data_length = instructions[start_index + 1]
    end_offset = start_index + 2

    while children > 0:
        child_results = sum_metadata(instructions, end_offset)
        metadata_sum += child_results[0]
        end_offset = child_results[1]
        children -= 1

    metadata_index = end_offset
    metadata_end_index = end_offset + meta_data_length
    while metadata_index < metadata_end_index:
        metadata_sum += instructions[metadata_index]
        metadata_index += 1

    return (metadata_sum, metadata_end_index)


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().replace('\n', '')
    print("Metadata: {0}".format(sum_metadata(prepare_input(instructions))[0]))
