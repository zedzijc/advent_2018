import sys
import re


class SectorHandler(object):

    def __init__(self):
        self.row_list = []

    def _register_row(self, row_number, margin, width):
        while len(self.row_list[row_number]) < margin:
            self.row_list[row_number].append(0)

        if len(self.row_list[row_number]) < margin + width:
            added_columns = margin + width - len(self.row_list[row_number])
            while len(self.row_list[row_number]) < margin + width:
                self.row_list[row_number].append(1)
            width = width - added_columns

        for column_number in range(margin, margin + width):
            self.row_list[row_number][column_number] += 1

    def _add_new_rows_if_needed(self, margin, height):
        while len(self.row_list) < margin + height:
            self.row_list.append([])

    def add_sector(self, x_margin, width, y_margin, height):
        self._add_new_rows_if_needed(y_margin, height)

        for row_number in range(y_margin, y_margin + height):
            self._register_row(row_number, x_margin, width)

    def get_total_overlapping_area(self):
        overlap = 0
        for row in self.row_list:
            for column in row:
                if column > 1:
                    overlap += 1
        return overlap


def parse_instruction(instruction):
    x = int(re.findall(r"\@\s(.*)\,", instruction)[0])
    y = int(re.findall(r"\,(.*)\:", instruction)[0])
    width = int(re.findall(r"\:\s(.*)x", instruction)[0])
    height = int(re.findall(r"x(.*)$", instruction)[0])
    return x, width, y, height


def get_overlap(instructions):
    sector_handler = SectorHandler()
    for instruction in instructions:
        x, width, y, height = parse_instruction(instruction)
        sector_handler.add_sector(x, width, y, height)

    return sector_handler.get_total_overlapping_area()


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Overlapped square inches: {0}".format(get_overlap(instructions)))
