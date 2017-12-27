#!/usr/bin/python


def ball_score(rolls):
    """
    Helper function to return score of one or two balls
    :param rolls: one or two rolls score
    :return: score of the one or two rolls
    """
    if '/' in rolls:
        return 10
    else:
        return sum(map(int, ' '.join(rolls).replace('X', '10').replace('-', '0').split()))


def frame_score(roll_sequence):
    """
    see: http://codingdojo.org/kata/Bowling/
    Given a valid sequence of rolls for one line of American Ten-Pin Bowling, produce the total score for the game
    :param roll_sequence: valid sequence of rolls .e.g. "5/ 5- X 5/ 5/2 5/ 5- 5/ -3 5/5"
    :return: total score for the game
    """
    # TODO validate roll_sequence (for now assume ten-frame valid)
    roll_sequence = roll_sequence.replace(" ", "")
    score = 0
    frame = 1
    i = 0
    while i < len(roll_sequence) and frame <= 10:
        if roll_sequence[i] == 'X':
            # a strike
            score += 10 + ball_score(roll_sequence[i + 1:i + 3])
            i += 1
        elif roll_sequence[i + 1] == '/':
            # a spare
            score += 10 + ball_score(roll_sequence[i + 2])
            i += 2
        else:
            score += ball_score(roll_sequence[i:i + 2])
            i += 2
        frame += 1
    return score


def main():
    import sys
    if len(sys.argv) > 1:
        print(frame_score(sys.argv[1].strip()))
    else:
        print('Requires a valid sequence of rolls (e.g. python bowling.py "5/ 5/ X 5/ 5/2 5/ 5/ 5/ 5/ 5/5"')


if __name__ == '__main__':
    main()
