import random
import yaml as y


def pre_game():
    with open('input.yaml', 'r') as f:
        data = y.safe_load(f)

    result = [(k, v) for k, v in data.items()]
    # print(result)
    return result


def start_game(g_board):
    dragons_killed, gold_counter = 0, 0
    marry_the_princess = False
    dragons_list = []
    for step in g_board:
        if 'd' in step[0]:
            choice = int(random.uniform(1, 100)) % 2
            if choice == 1:
                dragons_killed = dragons_killed + 1
                gold_counter = gold_counter + int(step[1])
                dragons_list.append(g_board.index(step) + 1)

        elif 'p' in step[0]:
            if dragons_killed >= int(step[1]):
                marry_the_princess = True
                break

    dragons_list.sort()
    return marry_the_princess, gold_counter, dragons_killed, dragons_list


def print_result(marry_the_princess, gold_counter, dragons_killed, dragons_list):
    if marry_the_princess:
        print(gold_counter)
        print(dragons_killed)
        print(*dragons_list)

    else:
        print(-1)


def main():
    game = pre_game()
    marry, count, dragons, d_list = start_game(game)
    print_result(marry, count, dragons, d_list)


if __name__ == '__main__':
    main()
