class IntervalNode:
    def __init__(self, src_start, src_end, des_start, des_end):
        self.source_interval = (src_start, src_end)
        self.destination_interval = (des_start, des_end)
        self.max = src_end
        self.left = None
        self.right = None

    def insert(self, node):
        if node.source_interval[0] < self.source_interval[0]:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        self.max = max(self.max, node.max)

        def __str__(self) -> str:
            return f"({self.source_interval})->({self.destination_interval})"


def insert(root, interval_src, interval_des):
    if root is None:
        return IntervalNode(interval_src[0], interval_src[1],
                            interval_des[0], interval_des[1])
    root.insert(IntervalNode(interval_src[0], interval_src[1],
                             interval_des[0], interval_des[1]))
    return root


def overlaps(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    return end1 >= start2 and end2 >= start1


def search_overlapping(root, interval):
    if root is None:
        return None
    if overlaps(root.interval, interval):
        return root.interval
    if root.left is not None and root.left.max >= interval[0]:
        return search_overlapping(root.left, interval)
    return search_overlapping(root.right, interval)


maps = ["seed-to-soil map:", "soil-to-fertilizer map:",
            "fertilizer-to-water map:", "water-to-light map:",
            "light-to-temperature map:",
            "temperature-to-humidity map:", "humidity-to-location map:"]
def get_data():
    global maps
    data = {"seeds": []}
    for i in range(len(maps)):
        data[maps[i]] = None
    current_map = maps[0]
    with open("input", "r") as file:
        for line in file:
            line = line.strip()
            if len(line) < 1:
                continue
            if line.startswith("seeds:"):
                seeds = list(map(int, line.split(":")[1].split()))
                for j in range(0, len(seeds), 2):
                    data["seeds"].append((seeds[j], seeds[j] + seeds[j+1] - 1))
                continue
            if line[0].isdigit():
                des, src, dist = tuple(map(int, line.split()))
                data[current_map] = insert(data[current_map], (src, src+dist-1), (des, des+dist-1))
            else:
                current_map = line

        return data

if __name__ == '__main__':
   print(get_data())
