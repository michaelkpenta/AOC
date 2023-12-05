
maps = ["seed-to-soil map:", "soil-to-fertilizer map:",
            "fertilizer-to-water map:", "water-to-light map:",
            "light-to-temperature map:",
            "temperature-to-humidity map:", "humidity-to-location map:"]


def get_data():
    global maps
    data = {"seeds": []}
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

def check_in_range(translator_in, translator_name, data_dict):
    translator: list = data_dict[translator_name]
    for (des_start, src_start, distance) in translator:
        if src_start <= translator_in < src_start + distance:
            dist_to_src_start = translator_in - src_start
            dest_result = des_start + dist_to_src_start
            return dest_result
    return translator_in #not found - returns its own value

if __name__ == '__main__':
    d = get_data()
    print(check_in_range(1, 'seed-to-soil map:', d))


