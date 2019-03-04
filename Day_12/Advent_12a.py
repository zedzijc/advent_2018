

class PotUtils(object):
    growth_patterns = [".##..", "#####", "####.", ".##.#",
                       "...##", ".#.##", "#..#.", "#.#..",
                       ".###.", "##.##", ".#...", "###..",
                       ".#..#", "##...", "..#..", "#.#.#", ".#.#."]

    @classmethod
    def get_pot_contents_next_generation(cls, sequence):
        return "#" if sequence in cls.growth_patterns else "."


class Pot(object):

    def __init__(self, content, pot_points):
        self.content = content
        self.points = pot_points
        self.next_generation_content = "."

    def get_content(self):
        return self.content

    def get_points(self):
        return self.points

    def set_next_generation_content(self, next_generation_content):
        self.next_generation_content = next_generation_content

    def age_one_generation(self):
        self.content = self.next_generation_content

    def __repr__(self):
        return self.content


def add_margin_pots(pots, points, negative):
    """
    Adds empty pots on the edge of the list, either left or right end.
    """
    if negative:
        index = 0
        extra_points = -5
        while index < 5:
            pots.insert(index, Pot(".", points + extra_points))
            index += 1
            extra_points += 1
    else:
        extra_points = 1
        while extra_points < 6:
            pots.append(Pot(".", points + extra_points))
            extra_points += 1


def get_plant_sum(initial_state, generations):
    pots = []
    points = 0
    add_margin_pots(pots, points, True)

    for plant in list(initial_state):
        pots.append(Pot(plant, points))
        points += 1

    # points - 1 because we add a point on the last for loop iteration above
    add_margin_pots(pots, points - 1, False)
    generation = 1
    neighbour_width = 2
    while generation <= generations:
        index = neighbour_width

        # Check what next generation will be for each pot
        while index < len(pots) - neighbour_width:
            pot_sequence = (pots[index - 2].get_content() +
                            pots[index - 1].get_content() +
                            pots[index].get_content() +
                            pots[index + 1].get_content() +
                            pots[index + 2].get_content())
            pots[index].set_next_generation_content(
                PotUtils.get_pot_contents_next_generation(pot_sequence))
            index += 1

        # Grow all pots to the next generation.
        for pot in pots:
            pot.age_one_generation()
        add_margin_pots(pots, pots[0].get_points(), True)
        add_margin_pots(pots, pots[-1].get_points(), False)
        generation += 1

    total_points = 0
    for pot in pots:
        if pot.get_content() == "#":
            total_points += pot.get_points()
    return total_points


if __name__ == "__main__":
    print("Plant sum: {0}".format(
        get_plant_sum(("#...#...##..####..##.####.#...#...#" +
                       ".#.#.#......##....#....######.####." +
                       "##..#..#..##.##..##....#######"), 20)))
# This was not a problem that I enjoyed :-)
