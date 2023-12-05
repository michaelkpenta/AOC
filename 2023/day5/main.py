

def get_data():
    data = {}
    maps = ["seeds", "seed_soil", "soil_fert", "fert_water",
            "water_light", "light_temp","temp_humid", "humid_location"]

    for i in range(len(maps)):
        data[maps[i]] = []
    current_map = 0
    with open("input", "r") as file:
        for line in file:
            if line.startswith("seeds:"):
                line = line.strip()
                data["seeds"] = list(map(int, line.split(":")[1].split()))
                continue
            if line.startswith("seed-to"):
                current_map = 1
                continue
            if line.startswith("soil-to"):
                current_map = 2
                continue
            if line.startswith("fertilizer-to"):
                current_map = 3
                continue
            if line.startswith("water-to"):
                current_map = 4
                continue
            if line.startswith("light-to"):
                current_map = 5
                continue
            if line.startswith("temperature-to"):
                current_map = 6
                continue
            if line.startswith("humidity-to"):
                current_map = 7
                continue
            if line.isspace():
                continue
            if line[0].isdigit():
                entry = tuple(map(int, line.split()))
                data[maps[current_map]].append(entry)

        return data

if __name__ == '__main__':
    print(get_data())
