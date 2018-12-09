import sys


class Guard(object):

    def __init__(self, guard_id):
        self.guard_id = guard_id
        self.time_slept = 0
        self.sleeping_since = None
        self.sleep_pattern = [0 for minute in range(0, 60)]

    def _log_sleep_pattern(self, minutes):
        for minute in minutes:
            self.sleep_pattern[minute] += 1

    def sleep(self, minute):
        self.sleeping_since = minute

    def wake_up(self, minute):
        self.time_slept += minute - self.sleeping_since
        self._log_sleep_pattern(range(self.sleeping_since, minute))

    def get_time_slept(self):
        return self.time_slept

    def get_guard_id(self):
        return self.guard_id

    def get_most_frequently_slept_minute(self):
        return self.sleep_pattern.index(max(self.sleep_pattern))


class GuardHandler(object):

    def __init__(self):
        self.guards = {}
        self.guard_on_duty = None

    def issue_command(self, guard_id, minute, action):
        if guard_id not in self.guards:
            self.guards[guard_id] = Guard(guard_id)

        if action == "falls asleep":
            self.guard_on_duty.sleep(minute)
        elif action == "wakes up":
            self.guard_on_duty.wake_up(minute)
        else:
            self.guard_on_duty = self.guards[guard_id]

    def get_most_sleepy_guard(self):
        most_sleepy_guard = self.guard_on_duty
        for guard in self.guards.values():
            if guard.get_time_slept() > most_sleepy_guard.get_time_slept():
                most_sleepy_guard = guard
        return most_sleepy_guard


def parse_instruction(instruction):
    guard_id = None
    words = instruction.split()
    for word in words:
        if ":" in word:
            minute = int(word.split(":")[1].replace("]", ""))
        elif "#" in word:
            guard_id = int(word.replace("#", ""))
    action = " ".join(words[-2:])
    return guard_id, minute, action


def get_overlap(instructions):
    guard_handler = GuardHandler()
    for instruction in sorted(instructions):
        guard_id, minute, action = parse_instruction(instruction)
        guard_handler.issue_command(guard_id, minute, action)

    guard = guard_handler.get_most_sleepy_guard()
    return guard.get_guard_id() * guard.get_most_frequently_slept_minute()


if __name__ == "__main__":
    instructions = open(sys.argv[1]).read().splitlines()
    print("Result: {0}".format(get_overlap(instructions)))
