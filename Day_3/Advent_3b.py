import sys
import re


class Claim(object):

    def __init__(self, claim_id, x_range, y_range):
        self.claim_id = claim_id
        self.x_range = x_range
        self.y_range = y_range

    def get_x_range(self):
        return self.x_range

    def get_y_range(self):
        return self.y_range

    def get_claim_id(self):
        return self.claim_id

    def overlaps(self, claim):
        x_overlap = (
            self.x_range[0] <=
            claim.get_x_range()[0] <=
            self.x_range[1] or
            claim.get_x_range()[0] <=
            self.x_range[0] <=
            claim.get_x_range()[1])

        y_overlap = (
            self.y_range[0] <=
            claim.get_y_range()[0] <=
            self.y_range[1] or
            claim.get_y_range()[0] <=
            self.y_range[0] <=
            claim.get_y_range()[1])

        return x_overlap and y_overlap


class SectorHandler(object):

    def __init__(self):
        self.unique_claims = []
        self.overlapped_claims = []

    def add_sector(self, claim_id, x_margin, width, y_margin, height):
        pending_removal = []
        new_unique_claim = Claim(claim_id,
                                 (x_margin, x_margin + width),
                                 (y_margin, y_margin + height))
        for unique_claim in self.unique_claims:
            if unique_claim.overlaps(new_unique_claim):
                pending_removal.append(unique_claim)

        if not pending_removal:
            unique = True
            for overlapped_claim in self.overlapped_claims:
                if overlapped_claim.overlaps(new_unique_claim):
                    self.overlapped_claims.append(new_unique_claim)
                    unique = False
                    break
            if unique:
                self.unique_claims.append(new_unique_claim)
        else:
            for overlapped_claim in pending_removal:
                self.overlapped_claims.append(overlapped_claim)
                self.unique_claims.remove(overlapped_claim)
            self.overlapped_claims.append(new_unique_claim)

    def get_unique_claim_ID(self):
        return self.unique_claims[0].get_claim_id()


def parse_instruction(instruction):
    claim_id = int(re.findall(r"^\#(.*)\s\@", instruction)[0])
    x = int(re.findall(r"\@\s(.*)\,", instruction)[0])
    y = int(re.findall(r"\,(.*)\:", instruction)[0])
    width = int(re.findall(r"\:\s(.*)x", instruction)[0])
    height = int(re.findall(r"x(.*)$", instruction)[0])

    return claim_id, x, width, y, height


def get_overlap(instructions):
    sector_handler = SectorHandler()
    for instruction in instructions:
        claim_id, x, width, y, height = parse_instruction(instruction)
        sector_handler.add_sector(claim_id, x, width, y, height)

    return sector_handler.get_unique_claim_ID()


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Unique claim has ID: {0}".format(get_overlap(instructions)))
