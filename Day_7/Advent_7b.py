import sys


class Instruction(object):

    def __init__(self, name):
        self.name = name
        self.base_amount_of_work = 60
        self.executed = False
        self.prerequisites = set()

    def set_amount_of_work(self, amount_of_work):
        self.amount_of_work = self.base_amount_of_work + amount_of_work

    def get_amount_of_work(self):
        return self.amount_of_work

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


class Worker(object):

    def __init__(self):
        self.work_remaining = 0

    def is_available(self):
        return self.work_remaining == 0

    def assign(self, instruction):
        self.work_remaining = instruction.get_amount_of_work()
        self.assignment = instruction

    def work(self):
        self.work_remaining -= 1
        if self.assignment is not None and self.work_remaining == 0:
            self.assignment.execute()


def get_instructions(raw_instructions):
    instructions = {}
    for raw_instruction in raw_instructions:
        split_instr = raw_instruction.upper().replace(" ", "").split("STEP")
        prereq_name, instr_name = split_instr[1][0], split_instr[2][0]

        for name in [prereq_name, instr_name]:
            if name not in instructions:
                instructions[name] = Instruction(name)

        instructions[instr_name].add_prerequisite(instructions[prereq_name])

    work_required = sorted(instructions.keys())
    for name, instruction in instructions.items():
        instruction.set_amount_of_work(work_required.index(name) + 1)

    return instructions.values()


def get_time_taken(raw_instructions):
    instructions = sorted(get_instructions(raw_instructions))
    workforce_size = 5
    workforce = [Worker() for i in range(workforce_size)]
    time_taken = 0

    while len(instructions) > 0:
        available_workers = []
        for worker in workforce:
            if worker.is_available():
                available_workers.append(worker)

        if available_workers:
            claimed_instructions = []
            for instruction in instructions:
                if instruction.ready_to_execute():
                    available_workers[0].assign(instruction)
                    del available_workers[0]
                    claimed_instructions.append(instruction)
                if not available_workers:
                    break

            for claimed_instructions in claimed_instructions:
                instructions.remove(claimed_instructions)

        for worker in workforce:
            if not worker.is_available():
                worker.work()
        time_taken += 1

    remaining_worker = True
    overtime = 0
    while remaining_worker:
        remaining_worker = False
        for worker in workforce:
            if not worker.is_available():
                remaining_worker = True
                worker.work()
        if remaining_worker:
            overtime += 1

    return time_taken + overtime


if __name__ == "__main__":
    raw_instructions = open(sys.argv[1]).read().splitlines()
    print("Time taken: {0}".format(get_time_taken(raw_instructions)))
