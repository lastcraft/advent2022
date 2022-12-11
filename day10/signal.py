durations = {"addx": 2, "noop": 1}

def to_signal(command, value):
    if command == "addx":
        return [0, 0, value]
    else:
        return []

class Signal:
    def __init__(self):
        self.values = [1]

    def apply(self, cycle, sequence):
        self.lengthen(cycle + len(sequence))
        for i, value in enumerate(sequence):
            self.values[cycle + i] += value

    def lengthen(self, target):
        for i in range(len(self.values), target):
            self.values.append(self.values[i - 1])

    def at(self, cycle):
        return self.values[cycle]

def part1(data):
    x = Signal()
    clock = 1
    for line in data.split("\n"):
        if line:
            tokens = line.split(" ")
            command, value = tokens[0], int(tokens[1]) if len(tokens) > 1 else None
            x.apply(clock, to_signal(command, value))
            clock += durations[command]
            print(command, value)
    samples = [20, 60, 100, 140, 180, 220]
    total = 0
    for sample in samples:
        total += x.at(sample) * sample
    print(total)

part1("""
noop
noop
addx 5
addx 29
addx -28
addx 5
addx -1
noop
noop
addx 5
addx 12
addx -6
noop
addx 4
addx -1
addx 1
addx 5
addx -31
addx 32
addx 4
addx 1
noop
addx -38
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx -32
addx 33
addx -20
addx 27
addx -39
addx 1
noop
addx 5
addx 3
noop
addx 2
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -16
addx 21
addx -1
addx 1
noop
addx 3
addx 5
addx -22
addx 26
addx -39
noop
addx 5
addx -2
addx 2
addx 5
addx 2
addx 23
noop
addx -18
addx 1
noop
noop
addx 2
noop
noop
addx 7
addx 3
noop
addx 2
addx -27
addx 28
addx 5
addx -11
addx -27
noop
noop
addx 3
addx 2
addx 5
addx 2
addx 27
addx -26
addx 2
addx 5
addx 2
addx 4
addx -3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx -33
noop
noop
noop
noop
addx 31
addx -26
addx 6
noop
noop
addx -1
noop
addx 3
addx 5
addx 3
noop
addx -1
addx 5
addx 1
addx -12
addx 17
addx -1
addx 5
noop
noop
addx 1
noop
noop
""")
