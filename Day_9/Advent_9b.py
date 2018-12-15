
class Marble(object):

    def __init__(self, value, previous_marble, next_marble):
        self.marble_value = value
        self.previous_marble = previous_marble
        self.next_marble = next_marble

    def set_next(self, next_marble):
        self.next_marble = next_marble

    def next(self):
        return self.next_marble

    def set_previous(self, previous_marble):
        self.previous_marble = previous_marble

    def previous(self):
        return self.previous_marble

    def value(self):
        return self.marble_value


def get_score(players, final_marble_value):
    players = [0 for player in range(players)]
    marble_value = 1
    current_marble = Marble(0, None, None)
    current_marble.set_next(current_marble)
    current_marble.set_previous(current_marble)

    while True:
        player_index = 0
        while player_index < len(players):
            if marble_value % 23 == 0:
                bonus_marble = current_marble
                bonus_marble_distance = 7

                while bonus_marble_distance > 0:
                    bonus_marble = bonus_marble.previous()
                    bonus_marble_distance -= 1
                bonus_marble.previous().set_next(bonus_marble.next())
                bonus_marble.next().set_previous(bonus_marble.previous())

                players[player_index] += marble_value
                players[player_index] += bonus_marble.value()
                current_marble = bonus_marble.next()

            else:
                new_marble = Marble(marble_value,
                                    current_marble.next(),
                                    current_marble.next().next())
                current_marble.next().next().set_previous(new_marble)
                current_marble.next().set_next(new_marble)
                current_marble = new_marble

            if marble_value == final_marble_value:
                return max([score for score in players])
            marble_value += 1
            player_index += 1


if __name__ == "__main__":
    print("Winning score: {0}".format(get_score(439, 7130700)))
