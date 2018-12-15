def get_score(players, final_marble_value):
    players = [player for player in range(players)]
    scores = [0 for player in players]
    marble = 1
    current_marble_position = 0
    circle = [0]

    while True:
        player_index = 0
        while player_index < len(players):
            if marble % 23 == 0:
                scores[player_index] += marble
                if current_marble_position < 7:
                    current_marble_position += len(circle)
                scores[player_index] += circle.pop(current_marble_position - 7)
                current_marble_position = current_marble_position - 7
            else:
                current_marble_position += 2
                if current_marble_position > len(circle):
                    current_marble_position = (current_marble_position -
                                               len(circle))
                circle.insert(current_marble_position, marble)
            if marble == final_marble_value:
                return max(scores)
            marble += 1
            player_index += 1


if __name__ == "__main__":
    print("Winning score: {0}".format(get_score(439, 71307)))
