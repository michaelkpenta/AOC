

def get_data():
    data = {}
    maps = ["seed-to-soil map:", "soil-to-fertilizer map:",
            "fertilizer-to-water map:", "water-to-light map:",
            "light-to-temperature map:",
            "temperature-to-humidity map:", "humidity-to-location map:"]

    data["seeds"] = []
    for i in range(len(maps)):
        data[maps[i]] = []
    current_map = maps[0]
    with open("input", "r") as file:
        for line in file:
            line = line.strip()
            if len(line) < 1:
                continue
            if line.startswith("seeds:"):
                data["seeds"] = list(map(int, line.split(":")[1].split()))
                continue
            if line[0].isdigit():
                data[current_map].append(tuple(map(int, line.split())))
            else:
                current_map = line

        return data


if __name__ == '__main__':
    print(get_data())

