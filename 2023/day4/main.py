def make_tuple(x):
    x = x.strip().split(":")
    left, right = x[1].split("|")
    left = left.strip().split()
    right = right.strip().split()
    return left, right


def get_data():
    data_list = []
    with open("2023/day4/input", "r") as file:
        file_list = file.readlines()
        m = list(map(make_tuple, file_list))
        data_list.extend(m)
    return data_list


def make_intersections(data :list):
    sets = []
    for s1, s2 in data:
        s = set(s1).intersection(set(s2))
        sets.append(list(s))
    return sets

def sum_up(l):
    dist = l[0]
    if dist == 0:
        return 0
    return dist + sum_up(l[:dist])

if __name__ == '__main__':
    d = get_data()
    winning_numbers = make_intersections(d)
    total = 0
    print(winning_numbers)
    for game in winning_numbers:
        score = 2**(len(game)-1)
        total += int(score)
    print(total)
    num_cards_per_game = list(map(len, winning_numbers))
    print(num_cards_per_game)
