def width(chart):
    return len(chart[0])

def height(chart):
    return len(chart)

def find(data, width, ch):
    return (data.strip().find(ch) % (width + 1), data.strip().find(ch) // (width + 1))

def parse_heights(data):
    data = data.strip().replace('S', 'a').replace('E', 'z')
    return [[ord(ch) - ord('a') for ch in line.strip()] for line in data.split("\n") if line]

def make_grid(grid, value):
    return list(map(
        lambda row: list(map(lambda visible: value, row)),
        grid))

def mark(grid, point, value):
    if point[0] < 0 or point[0] >= width(grid):
        raise ValueError()
    if point[1] < 0 or point[1] >= height(grid):
        raise ValueError()
    grid[point[1]][point[0]] = value

def peek(grid, point):
    if point[0] < 0 or point[0] >= width(grid):
        raise ValueError()
    if point[1] < 0 or point[1] >= height(grid):
        raise ValueError()
    return grid[point[1]][point[0]]

def east(point):
    return (point[0] + 1, point[1])

def west(point):
    return (point[0] - 1, point[1])

def north(point):
    return (point[0], point[1] - 1)

def south(point):
    return (point[0], point[1] + 1)

def measurement_sweep(chart, distances):
    work_done = False
    for y in range(0, height(chart)):
        for x in range(0, width(chart)):
            distance = peek(distances, (x, y))
            if distance < 9999:
                elevation = peek(chart, (x, y))
                for direction in [east, west, north, south]:
                    destination = direction((x, y))
                    try:
                        if elevation - peek(chart, destination) <= 1:
                            if peek(distances, destination) > distance + 1:
                                mark(distances, destination, distance + 1)
                                work_done = True
                    except:
                        pass
    return work_done

def part1(data):
    chart = parse_heights(data)
    end = find(data, width(chart), 'E')
    start = find(data, width(chart), 'S')
    distances = make_grid(chart, 9999)
    mark(distances, end, 0)
    while measurement_sweep(chart, distances):
        pass
    print(peek(distances, start))

def show(chart, distances):
    for y in range(0, height(chart)):
        for x in range(0, width(chart)):
            distance = peek(distances, (x, y))
            if distance != 9999:
                print(chr(distance % 10 + ord('0')), end='')
            else:
                print(' ', end='')
        print()

part1("""
abcccccccccccaaaaacccccccaaaaaaccccccccccccccccccccccccccccccccaaaaaaaaaaaaaacccccccccccccccccccaaaaaacccccccacccccccccaaccaaccccccccccccccccccccccccccccccaaaaaa
abcccccccccccaaaaaaacccccaaaaaaccccccccaaccccccccccaaaaccccccccaaaaaaaaaaaaaccccccccccccccccccccaaaaaaccccaaaacccccccccaaaaaaccccccccccccccccccccccccccccccccaaaa
abccccccccccaaaaaaaacccccaaaaaccccccccaaaacccccccccaaaacccccccccccaaaaaaacccccccccccccccccccccccaaaaacccccaaaaaaccccccccaaaaacccccccccccaaaccccccccccccccccccaaaa
abccccccccccaaaaaaaaccccccaaaaacccccccaaaacccccccccaaaacccccaaaccccaaaaaaccccccccccccccccccccccccaaaaacccccaaaaacccccccaaaaaacccccccccccaaaacccccccccccccccccaaaa
abccccccccccaaaaaaccccccccaaaaacccccccaaaaccccccccccaaacccccaaaaccaaaaaaaacccccccccccccccccccccccaaaaaccccaaaaacccccccaaaaaaaaccccccccccaaaaccaaccccccccccccaaaaa
abcccccccccccccaaaccccccccccccccccccccccccccccccccccccccccccaaaaccaaaaaaaaccccccccccccccccccccccccccccccccaccaaccccaaaaaaaaaaacccccccccccaaaaaaccccccccccccccaccc
abcacccccccccccccaaaccccccccccccccaaacccccccccccccccccccccccaaaccaaaacccaaacccccccccccccccccccccccaacccccccccccccccaaacccaaccccccccccccccaaaalllllccccccccccccccc
abaacccccccccccccaaaaaacccccccccccaaaccccccccccccccccccccccccccccaaaccccaaaccccccccccccccccccccccaaccccccccccccccccaaaaaaaaccccccccccccccckklllllllccccaaaccccccc
abaaaaacccccccccaaaaaaacccccccccaaaaaaaacccccaacccccccccccccccccccccccccaaaccccccccaacccccccccaaaaacaacaacaacccccaaaaaaaaccccccccccccaaakkkkllllllllcccaaaccccccc
abaaaaaccccccccaaaaaaaacccccccccaaaaaaaacccccaaaaaacccccccccccccccccccccaaaccccccaaaacacccccccaaaaaaaacaaaaaccccaaaaaaaaaccccccccckkkkkkkkkklsssslllcccaaaaaacccc
abaaaccccccccccaaaaaaacccccccccccaaaaacccccccaaaaaaccccccccccccccccccaaaaaaaaccccaaaaaacccccccccaaaaacaaaaacccccaaaaaaaacccaaaccjjkkkkkkkkkssssssslllcccaaaaacccc
abaaaccccccccccccaaaaaacccccaacccaaaaaaccccaaaaaaaccaaaccccccccccccccaaaaaaaacccccaaaacccccccccaaaaaccaaaaaacccccccaaaaaaccaaaajjjjkkkkkkssssssssslllcddaaaaccccc
abcaaacccccccccccaaaaaacaaacaacccaaaaaaccccaaaaaaaaaaaaaaccccccccccccccaaaaaccccccaaaaccccaaaaaaacaaacccaaaaaaacccaaaaaaaccaaajjjjrrrrrrssssuuuussqmmddddaaaccccc
abccaacccccccccccaaccccccaaaaacccaaaccaccccaaaaaaaaaaaaaacccccccccccccaaaaaacccccaacaaccccaaaaacccaaccccacccaaaaaaaaaccaaccaaajjjrrrrrrrrssuuuuuvqqmmmdddaaaccccc
abccccccccaaccccccccccccccaaaaaacccccccccccccaaaaaaaaaaaccccccccccccccaaaaaacccccccccccccaaaaaaccccccccccccaaaaaaaaaacccccccccjjjrrruuuuuuuuuuuvvqqmmmmddddaccccc
abaacccccaaaaccccccccccccaaaaaaacccccccccccccaacccccaaaaacccccccccccccaccaaacccccccccccccaaaaaacccccccccccaaaaaaaaccccccccccccjjjrrruuuuuuuuxyyvvqqqmmmddddcccccc
abaacccccaaaacccccccccccaaaaaaccccccccaaccccccccacccaaaaacccccccccccccccccccccccccccccccccaaaaacccccccccccaaaaaaacccccccccccccjjjrrttuxxxxuxxyyvvqqqqmmmmddddcccc
abaacccccaaaacccccccccccaacaaacccccaaaaacccaaaaaaaccccccccccccccccccccccccccccccccccccccccaaacccccccccccccccaaaaaaccccccccccccjjjrrtttxxxxxxyyyvvqqqqqmmmmdddcccc
abacccccccccccccccccccccccccaaccccccaaaaaccaaaaaaaccccccccaaccccccccccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccccccjjjqrrttxxxxxxyyyvvvvqqqqmmmdddcccc
abccccccccccccccccccccccccccccccccccaaaaaccaaaaaaacccccccaaaccccccccccaaaccccccccccccccccccaaaccccccccccccccaaccccccccccaaccccjjjqqqtttxxxxxyyyyyvvvqqqqmmmeeeccc
SbaaccccccaccaaacccccccccccccccccccaaaaacccaaaaaaaaccccaaaaaaaacccccccaaacaaccccccccccccccaaaaaaccccccccccccccccccccccaaaaaaccciiiqqqttxxxxEzyyyyyvvvqqqnnneeeccc
abaaccccccaaaaaaccccccccccccccccccccccaaccaaaaaaaaaacccaaaaaaaacccccaaaaaaaaccccccccccccccaaaaaaccccccccccccccccccccccaaaaaaccciiiqqtttxxxyyyyyyyvvvvqqqnnneeeccc
abaaaaacccaaaaaaccccccccccccccccccccccccccaaaaaaaaaaccccaaaaaaccccccaaaaaaaaccccccccccccccaaaaaacccccccccccccccccccccccaaaaacciiiqqqttxxyyyyyyywvvvvrrrqnnneeeccc
abaaaaacccaaaaaaaccccccccaaaccccccccccccccaacaaaccccccccaaaaaaccccccaaaaaaaccccccccccccccccaaaaaccccccccccccccccccccccaaaaaccciiiqqtttxxxyyyyywwwvrrrrrnnneeecccc
abaaaccccaaaaaaaaccccccccaaaacccccccccccccccccaaccccccccaaaaaaccccccccaaaaaccccccccccccccccaacaaccccccccccccccccccccccaaaaaccciiqqqttxxxwwwwyyywwrrrrnnnnneeecccc
abaaaccccaaaaaaaaccccccccaaaacccccaaaaacccccccaaccccccccaaccaacccccccaaacaaacccccccccccccccccccccccccccccccccccccccccccccccccciiqqqtttwwwwwwywwwrrrrnnnnneeeccccc
abcaaaccccccaaaccccccccccaaaccccccaaaaacccccccccccccaaaaccccccccccccccaacccccccccccccccccccccccccccccccaaaacccccccccccccccccciiiqqqtttssssswwwwwrrrnnnneeeecccccc
abccaaccccccaaaccccccccccccccccccaaaaaacccccccccccccaaaaccccccccccccccccccccccccccccccccccccccccccccccaaaaacccccccccccccccccciiiqqqqtssssssswwwwrronnnfeeeacccccc
abcccccccccccccccccccccccccccccccaaaaaacccccccccccccaaaaccccccccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccccccccccciiiiqqppssssssswwwwrroonfffeaacccccc
abcccccccccccccccccccccccccccccccaaaaaacaaaccccccccccaacccccccccccccccccccccccccccccccccaaacccccccccccaaaaaaccccccccccccccccccihhpppppppppsssssrrroonfffaaaaacccc
abcccccccccccccccccccccccccccccccccaacccaaaaacccccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccaaaaaccccccccccccccccccchhhhppppppppppssssrooofffaaaaaacccc
abccccccccaaaccccccccccccccccccccccccccaaaaacccccccccccccccccccccccccccccccccccccaccccaaaaaaaaccccccccccaaacccccccccccccccccccchhhhhhhhhpppposssoooofffaaaaaccccc
abccccccccaaaacccccaaccccccccccccccccccaaaaaccccccccccccccccccccccccaaccccccccccaaccccaaaaaaaacccccccccccccccccccccccccccccccccchhhhhhhhhgppooooooofffaaaaacccccc
abaaccccccaaaacccccaacaaccccccccccccccccaaaaacccccccccccccccaacaaccaaaaaaccccaaaaacaacaaaaaaacccccccccccccccccccccccccccccccccccccchhhhhhgggooooooffffaaaaaaccccc
abaaacccccaaaacccccaaaaaccccccccccccccccaaccccccccccccccccccaaaaaccaaaaaaccccaaaaaaaacccaaaaaccccccccccccccccccccccccaaacaacccccccccccccgggggooooffffccccaacccccc
abaaaccccccccccccaaaaaaccccaaccccccccccccccccccaaacccccccccccaaaaaaaaaaaacaacccaaaaaccccaacaaacccccccccccccccccccccccaaaaaaccccccccccccccaggggggggfffcccccccccccc
abaaaccccccccccccaaaaaaaacaaaaccccccccaaaccccccaaaacccccccccaaaaaaaaaaaaaaaaccaaaaacccccaaaaaccccccccccccccaaccccccccaaaaaaccccccccccccccaagggggggfccccccccccccca
abaacccccccccccccaccaaaaacaaaaccccccccaaaccccccaaaacccccccccaaaaccaaaaaaaaaaccaacaaaccccccaaaccccccccccccaaaaaacccccaaaaaaacccccccccccccaaaaccggggcccccccccccccaa
abaacccccccccccccccaaacaccaaaacccccaaaaaaaaccccaaaccccccccccccaaccaaaaaaaacccccccaacccccaacaaaaacccccccccaaaaaacccccaaaaaaaaccccccccccccaaaccccccccccccccccaaacaa
abcccccccccccccccccaaccccccccccccccaaaaaaaaccccccccccccccccccccaaaaaaaaaaaccccccccccccccaaaaaaaacccccccccaaaaaacccccaaaaaaaaccccccccccccacaccccccccccccccccaaaaaa
abccccccccccccccccccccccccccccccccccaaaaaacccccccccccccccccccccaaaaaaaaaaaaccccccccccccccaaaaaaccccccccccaaaaaccccccccaaacccccccccccccccccccccccccccccccccccaaaaa
""")
