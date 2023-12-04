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
    return data_list


if __name__ == '__main__':
    get_data()
