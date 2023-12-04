def line_to_list(line: str):
    index = 0
    result_list = []
    while index < len(line):
        if line[index].isnumeric():
            result_list.append(int(line[index]))

        else: #it is a character - could be a number word
            word_to_num = {
              "one": 1, "two": 2, "three": 3,
              "four": 4, "five": 5, "six": 6,
              "seven": 7, "eight": 8, "nine": 9}
            for word in word_to_num:
                if line[index:].startswith(word):
                    result_list.append(int(word_to_num[word]))
        index += 1
    return result_list


def find_total():
    total = 0
    with open("input", "r") as file:
        for line in file:
            num_list = line_to_list(line)
            number = num_list[0] * 10 + num_list[-1]
            total += number
    return total


if __name__ == "__main__":
   print(line_to_list("ggdone3nbmsthreefourninefiveoneightpr"))
   print(find_total())
