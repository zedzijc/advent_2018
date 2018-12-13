import sys


class Instruction(object):

    def __init__(self, name):
        self.name = name
        self.executed = False
        self.prerequisites = set()

    def execute(self):
        self.executed = True

    def has_executed(self):
        return self.executed

    def ready_to_execute(self):
        for prerequisite in self.prerequisites:
            if not prerequisite.has_executed():
                return False
        return True

    def add_prerequisite(self, instruction):
        self.prerequisites.add(instruction)

    def get_name(self):
        return self.name

    def __lt__(self, instruction):
        return self.name < instruction.get_name()


def get_instructions(raw_instructions):
    instructions = {}
    for raw_instruction in raw_instructions:
        split_instr = raw_instruction.upper().replace(" ", "").split("STEP")
        prereq_name, instr_name = split_instr[1][0], split_instr[2][0]

        for name in [prereq_name, instr_name]:
            if name not in instructions:
                instructions[name] = Instruction(name)

        instructions[instr_name].add_prerequisite(instructions[prereq_name])
    return instructions.values()


def get_instruction_order(raw_instructions):
    instructions = sorted(get_instructions(raw_instructions))
    instruction_order = []
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction.ready_to_execute():
            instruction.execute()
            instruction_order.append(instruction.get_name())
            instructions.remove(instruction)
            i = 0
        else:
            i += 1
    return "".join(instruction_order)


if __name__ == "__main__":
    raw_instructions = open(sys.argv[1]).read().splitlines()
    print("Instructions: {0}".format(get_instruction_order(raw_instructions)))
