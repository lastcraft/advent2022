import re

def extract_row(line):
    row = ""
    for i in range(1, len(line), 4):
        row += line[i]
    return row

def stack_row(pallet, row):
    for i in range(0,len(row)):
        if i + 1 > len(pallet):
            pallet.append("")
        if row[i] != " ":
            pallet[i] += row[i]


def parse_stacks(raw):
    pallet = []
    lines = raw.split("\n")
    lines.reverse()
    index_line = False
    for line in lines:
        if not line:
            continue
        if not index_line:
            index_line = True
            continue
        stack_row(pallet, extract_row(line))
    return pallet

def parse_moves(raw):
    return raw

def numbers(text):
    return list(map(int, re.findall(r'\d+', text)))

def index(label):
    return int(label) - 1

def parse_moves(raw):
    moves = []
    for line in raw.split("\n"):
        if line:
            move = numbers(line)
            moves.append({"times": int(move[0]), "from": index(move[1]), "to": index(move[2])})
    return moves

def parse(data):
    parts = data.split("\n\n")
    return (parse_stacks(parts[0]), parse_moves(parts[1]))

def last(l, n=1):
    return l[(-n):]

def except_last(l, n=1):
    return l[0:(-n)]

def apply_move(pallet, move):
    for _ in range(0, move["times"]):
        crate = last(pallet[move["from"]])
        pallet[move["from"]] = except_last(pallet[move["from"]])
        pallet[move["to"]] += crate

def part1(data):
    pallet, moves = parse(data)
    for move in moves:
        apply_move(pallet, move)
    top = ""
    for stack in pallet:
        top += last(stack)
    print(top)

def apply_move2(pallet, move):
    crates = last(pallet[move["from"]], move["times"])
    pallet[move["from"]] = except_last(pallet[move["from"]], move["times"])
    pallet[move["to"]] += crates

def part2(data):
    pallet, moves = parse(data)
    for move in moves:
        apply_move2(pallet, move)
    top = ""
    for stack in pallet:
        top += last(stack)
    print(top)

part2("""
            [Q]     [G]     [M]    
            [B] [S] [V]     [P] [R]
    [T]     [C] [F] [L]     [V] [N]
[Q] [P]     [H] [N] [S]     [W] [C]
[F] [G] [B] [J] [B] [N]     [Z] [L]
[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
[R] [N] [S] [T] [P] [P] [W] [Q] [G]
 1   2   3   4   5   6   7   8   9 

move 1 from 2 to 6
move 3 from 7 to 9
move 7 from 9 to 4
move 2 from 5 to 3
move 3 from 2 to 8
move 14 from 4 to 5
move 1 from 2 to 1
move 1 from 2 to 3
move 3 from 6 to 8
move 3 from 6 to 9
move 1 from 4 to 6
move 5 from 9 to 8
move 9 from 8 to 9
move 3 from 3 to 8
move 8 from 9 to 4
move 2 from 1 to 7
move 4 from 1 to 5
move 2 from 7 to 1
move 1 from 9 to 6
move 7 from 4 to 7
move 1 from 8 to 4
move 1 from 9 to 8
move 2 from 6 to 7
move 7 from 7 to 3
move 10 from 3 to 1
move 1 from 3 to 2
move 1 from 2 to 9
move 1 from 9 to 8
move 15 from 5 to 8
move 1 from 6 to 9
move 2 from 7 to 3
move 11 from 1 to 8
move 1 from 9 to 8
move 1 from 1 to 5
move 3 from 5 to 2
move 2 from 6 to 9
move 1 from 2 to 4
move 2 from 4 to 5
move 1 from 3 to 6
move 5 from 8 to 3
move 12 from 8 to 4
move 2 from 2 to 5
move 12 from 8 to 1
move 1 from 6 to 9
move 10 from 5 to 7
move 3 from 3 to 9
move 6 from 8 to 9
move 2 from 3 to 5
move 8 from 4 to 7
move 1 from 3 to 2
move 6 from 8 to 6
move 8 from 9 to 3
move 2 from 5 to 4
move 1 from 2 to 3
move 2 from 9 to 2
move 1 from 9 to 2
move 1 from 2 to 1
move 2 from 2 to 4
move 5 from 4 to 2
move 3 from 2 to 3
move 2 from 4 to 2
move 18 from 7 to 3
move 3 from 6 to 9
move 1 from 6 to 3
move 1 from 4 to 1
move 1 from 6 to 3
move 6 from 3 to 9
move 2 from 2 to 6
move 26 from 3 to 7
move 2 from 2 to 3
move 2 from 6 to 8
move 3 from 1 to 5
move 8 from 9 to 1
move 1 from 8 to 5
move 1 from 3 to 1
move 2 from 9 to 3
move 1 from 1 to 2
move 12 from 1 to 7
move 1 from 8 to 5
move 2 from 3 to 5
move 1 from 3 to 6
move 2 from 6 to 2
move 7 from 5 to 7
move 1 from 4 to 2
move 15 from 7 to 4
move 1 from 4 to 9
move 1 from 7 to 6
move 14 from 4 to 2
move 1 from 1 to 2
move 5 from 1 to 5
move 4 from 5 to 4
move 1 from 6 to 3
move 4 from 4 to 7
move 1 from 9 to 2
move 1 from 3 to 5
move 2 from 5 to 1
move 1 from 1 to 6
move 2 from 1 to 5
move 9 from 2 to 9
move 1 from 6 to 1
move 1 from 1 to 9
move 1 from 5 to 4
move 1 from 5 to 6
move 4 from 7 to 2
move 1 from 4 to 1
move 18 from 7 to 1
move 17 from 1 to 7
move 4 from 9 to 5
move 1 from 5 to 8
move 1 from 1 to 4
move 2 from 9 to 6
move 3 from 9 to 7
move 1 from 1 to 5
move 1 from 7 to 5
move 16 from 7 to 2
move 1 from 4 to 2
move 1 from 8 to 7
move 1 from 9 to 8
move 1 from 8 to 4
move 3 from 5 to 3
move 15 from 7 to 6
move 7 from 6 to 4
move 9 from 6 to 2
move 2 from 5 to 7
move 2 from 6 to 8
move 4 from 4 to 7
move 2 from 8 to 1
move 11 from 2 to 7
move 1 from 4 to 2
move 2 from 3 to 6
move 3 from 4 to 5
move 12 from 7 to 1
move 1 from 7 to 3
move 31 from 2 to 4
move 3 from 7 to 2
move 1 from 6 to 3
move 1 from 5 to 1
move 1 from 5 to 2
move 2 from 3 to 4
move 1 from 6 to 1
move 1 from 3 to 6
move 1 from 5 to 6
move 1 from 2 to 4
move 11 from 1 to 4
move 5 from 1 to 5
move 1 from 7 to 3
move 3 from 5 to 8
move 1 from 8 to 7
move 1 from 5 to 3
move 2 from 8 to 5
move 2 from 6 to 2
move 2 from 5 to 1
move 1 from 7 to 9
move 1 from 3 to 9
move 2 from 9 to 5
move 1 from 1 to 6
move 1 from 6 to 5
move 1 from 3 to 5
move 13 from 4 to 8
move 5 from 2 to 3
move 3 from 3 to 4
move 1 from 8 to 6
move 4 from 5 to 2
move 1 from 1 to 5
move 1 from 3 to 7
move 2 from 5 to 4
move 11 from 4 to 5
move 1 from 3 to 7
move 15 from 4 to 2
move 1 from 6 to 4
move 19 from 2 to 8
move 8 from 8 to 3
move 2 from 3 to 8
move 7 from 5 to 4
move 6 from 3 to 4
move 8 from 4 to 5
move 7 from 4 to 6
move 2 from 7 to 5
move 9 from 5 to 6
move 13 from 8 to 3
move 3 from 4 to 3
move 6 from 3 to 4
move 6 from 8 to 2
move 4 from 5 to 9
move 5 from 8 to 7
move 4 from 6 to 2
move 5 from 3 to 5
move 1 from 6 to 9
move 8 from 2 to 6
move 1 from 8 to 7
move 1 from 2 to 5
move 1 from 4 to 1
move 3 from 3 to 1
move 1 from 7 to 3
move 4 from 9 to 8
move 6 from 6 to 2
move 2 from 8 to 4
move 1 from 7 to 6
move 3 from 5 to 1
move 4 from 5 to 3
move 6 from 2 to 9
move 4 from 7 to 4
move 2 from 8 to 5
move 2 from 9 to 5
move 4 from 5 to 6
move 1 from 2 to 5
move 8 from 6 to 7
move 18 from 4 to 2
move 2 from 3 to 6
move 6 from 1 to 8
move 8 from 7 to 9
move 9 from 6 to 4
move 1 from 5 to 4
move 5 from 8 to 4
move 1 from 4 to 5
move 1 from 8 to 1
move 8 from 9 to 8
move 3 from 3 to 9
move 5 from 2 to 7
move 1 from 5 to 2
move 2 from 4 to 8
move 11 from 2 to 8
move 1 from 7 to 2
move 2 from 6 to 5
move 1 from 6 to 2
move 4 from 2 to 3
move 2 from 1 to 3
move 5 from 9 to 7
move 1 from 5 to 8
move 6 from 7 to 8
move 7 from 3 to 7
move 1 from 5 to 9
move 3 from 9 to 7
move 1 from 4 to 1
move 1 from 9 to 8
move 8 from 7 to 3
move 1 from 2 to 4
move 1 from 1 to 7
move 9 from 3 to 7
move 7 from 4 to 7
move 8 from 7 to 3
move 1 from 7 to 9
move 13 from 7 to 4
move 1 from 4 to 6
move 11 from 8 to 2
move 5 from 3 to 7
move 1 from 9 to 6
move 7 from 2 to 9
move 2 from 2 to 4
move 4 from 9 to 2
move 17 from 8 to 3
move 3 from 3 to 4
move 1 from 7 to 6
move 5 from 2 to 3
move 8 from 4 to 1
move 2 from 6 to 4
move 1 from 2 to 7
move 1 from 1 to 4
move 1 from 8 to 2
move 2 from 7 to 4
move 7 from 1 to 9
move 16 from 4 to 2
move 1 from 6 to 1
move 2 from 2 to 9
move 6 from 2 to 7
move 1 from 1 to 6
move 3 from 2 to 6
move 10 from 3 to 6
move 6 from 9 to 8
move 3 from 4 to 3
move 6 from 9 to 2
move 4 from 3 to 7
move 10 from 2 to 5
move 2 from 2 to 6
move 3 from 6 to 3
move 1 from 8 to 2
move 1 from 2 to 6
move 5 from 6 to 1
move 3 from 6 to 7
move 5 from 8 to 4
move 3 from 7 to 1
move 2 from 6 to 1
move 2 from 4 to 1
move 2 from 5 to 8
move 1 from 8 to 7
move 1 from 8 to 9
move 8 from 3 to 4
move 11 from 1 to 7
move 1 from 9 to 8
move 1 from 8 to 3
move 3 from 6 to 3
move 1 from 6 to 8
move 3 from 5 to 2
move 1 from 8 to 6
move 2 from 5 to 8
move 3 from 5 to 6
move 3 from 2 to 4
move 2 from 8 to 4
move 22 from 7 to 3
move 12 from 3 to 2
move 9 from 3 to 9
move 1 from 1 to 2
move 2 from 6 to 8
move 2 from 8 to 4
move 2 from 6 to 5
move 11 from 3 to 1
move 18 from 4 to 3
move 3 from 7 to 3
move 1 from 5 to 7
move 3 from 2 to 4
move 2 from 4 to 9
move 6 from 1 to 4
move 1 from 5 to 1
move 10 from 9 to 3
move 27 from 3 to 9
move 6 from 2 to 8
move 5 from 4 to 2
move 3 from 3 to 8
move 1 from 7 to 8
move 10 from 8 to 2
move 5 from 1 to 5
move 1 from 3 to 5
move 1 from 1 to 8
move 14 from 9 to 4
move 6 from 5 to 6
move 11 from 9 to 4
move 6 from 6 to 3
move 1 from 8 to 6
move 2 from 9 to 5
move 1 from 2 to 5
move 8 from 2 to 1
move 12 from 4 to 7
move 1 from 6 to 8
move 14 from 4 to 1
move 1 from 9 to 8
move 1 from 5 to 1
move 2 from 5 to 2
move 11 from 1 to 6
move 11 from 6 to 1
move 1 from 8 to 7
move 1 from 8 to 2
move 12 from 1 to 7
move 1 from 4 to 7
move 5 from 1 to 5
move 5 from 2 to 6
move 1 from 5 to 6
move 1 from 2 to 9
move 6 from 1 to 3
move 19 from 7 to 2
move 1 from 9 to 6
move 9 from 3 to 2
move 9 from 2 to 7
move 3 from 5 to 8
move 1 from 5 to 1
move 3 from 3 to 9
move 7 from 2 to 9
move 15 from 7 to 2
move 10 from 9 to 4
move 4 from 4 to 9
move 1 from 6 to 4
move 1 from 1 to 6
move 26 from 2 to 5
move 1 from 7 to 3
move 6 from 4 to 8
move 3 from 2 to 9
move 6 from 8 to 3
move 4 from 5 to 7
move 1 from 4 to 5
move 2 from 2 to 1
move 6 from 9 to 1
move 3 from 3 to 8
move 3 from 2 to 8
move 3 from 7 to 9
move 6 from 1 to 7
move 2 from 3 to 2
move 2 from 2 to 5
move 1 from 8 to 6
move 4 from 7 to 3
move 10 from 5 to 3
move 4 from 9 to 1
move 6 from 3 to 1
move 1 from 7 to 4
move 4 from 3 to 2
move 1 from 3 to 1
move 13 from 1 to 5
move 1 from 3 to 7
move 1 from 3 to 8
move 4 from 6 to 3
move 1 from 6 to 3
move 7 from 8 to 2
move 1 from 6 to 9
move 2 from 7 to 2
move 1 from 9 to 5
move 2 from 8 to 6
move 1 from 7 to 5
move 1 from 3 to 1
move 30 from 5 to 2
move 1 from 3 to 4
move 2 from 6 to 1
move 5 from 3 to 4
move 2 from 6 to 5
move 5 from 4 to 3
move 1 from 3 to 1
move 4 from 1 to 6
move 1 from 2 to 5
move 2 from 4 to 9
move 4 from 3 to 5
move 1 from 3 to 5
move 1 from 5 to 3
move 6 from 5 to 1
move 2 from 1 to 9
move 4 from 6 to 2
move 1 from 3 to 5
move 1 from 5 to 2
move 1 from 5 to 2
move 8 from 2 to 5
move 4 from 9 to 6
move 3 from 1 to 4
move 3 from 6 to 2
move 2 from 4 to 2
move 1 from 6 to 1
move 1 from 4 to 6
move 2 from 5 to 1
move 1 from 6 to 8
move 3 from 5 to 2
move 2 from 5 to 6
move 1 from 6 to 7
move 1 from 5 to 9
move 1 from 7 to 5
move 3 from 1 to 9
move 3 from 9 to 5
move 31 from 2 to 6
move 1 from 1 to 3
move 1 from 8 to 9
move 30 from 6 to 9
move 2 from 9 to 8
move 13 from 2 to 3
move 4 from 5 to 2
move 1 from 8 to 4
move 1 from 4 to 1
move 1 from 1 to 6
move 5 from 2 to 8
move 1 from 2 to 8
move 26 from 9 to 3
move 18 from 3 to 8
move 1 from 2 to 1
move 12 from 3 to 8
move 1 from 2 to 3
move 3 from 6 to 4
move 1 from 1 to 9
move 11 from 8 to 5
move 1 from 4 to 7
move 9 from 3 to 9
move 1 from 7 to 8
move 11 from 8 to 3
move 11 from 3 to 2
move 11 from 2 to 9
move 19 from 9 to 8
move 3 from 5 to 7
move 2 from 4 to 2
move 2 from 2 to 8
move 29 from 8 to 2
move 5 from 5 to 4
move 1 from 9 to 6
move 2 from 5 to 9
move 1 from 6 to 9
move 7 from 8 to 7
move 1 from 9 to 7
move 6 from 9 to 1
move 1 from 9 to 4
move 1 from 5 to 4
move 15 from 2 to 5
move 3 from 1 to 7
move 5 from 5 to 2
move 1 from 8 to 3
move 1 from 5 to 8
move 2 from 3 to 6
move 1 from 3 to 8
move 9 from 2 to 1
move 1 from 8 to 7
move 1 from 8 to 3
move 10 from 7 to 8
move 4 from 7 to 3
move 1 from 7 to 2
move 1 from 8 to 6
move 3 from 6 to 5
move 6 from 5 to 8
move 3 from 1 to 3
move 8 from 3 to 7
move 3 from 1 to 3
move 4 from 8 to 3
move 1 from 4 to 5
move 4 from 1 to 4
move 1 from 4 to 5
move 1 from 7 to 4
move 4 from 4 to 1
move 2 from 8 to 7
move 6 from 5 to 2
move 2 from 8 to 1
move 6 from 4 to 7
move 1 from 5 to 4
move 5 from 8 to 6
move 1 from 6 to 9
""")
