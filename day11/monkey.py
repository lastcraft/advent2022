import re

class Monkey:
    def __init__(self, items, operation, test, modulus = None):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0
        self.modulus = modulus

    def __repr__(self):
        return f"Monkey {repr(self.items)} {self.inspections}"

    def catch(self, item):
        self.items.append(item)

    def inspect_all(self, monkeys):
        while len(self.items) > 0:
            self.inspect(self.items.pop(0), monkeys)

    def inspect(self, item, monkeys):
        worry = self.operation(item)
        if self.modulus:
            worry %= self.modulus
        monkeys[self.test(worry)].catch(worry)
        self.inspections += 1

def parse_monkey(monkey_code, modulus = None):
    items = parse_numbers(extract(r"Starting items: (.*?)\n", monkey_code))
    operation = parse_operation(extract(r"Operation: new = (.*?)\n", monkey_code))
    test = make_test(
        int(extract(r"Test: divisible by (.*?)\n", monkey_code)),
        int(extract(r"If true: throw to monkey (.*?)\n", monkey_code)),
        int(extract(r"If false: throw to monkey (.*?)$", monkey_code)))
    return Monkey(items, operation, test, modulus)

def parse_numbers(token):
    return list(map(int, token.split(", ")))

def parse_operation(token):
    elements = token.split(" ")
    ops = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}
    def operation(old):
        return ops[elements[1]](old, old if elements[2] == 'old' else int(elements[2]))
    return operation

def make_test(divisor, true_monkey, false_monkey):
    def test(worry):
        return true_monkey if worry % divisor == 0 else false_monkey
    return test

def extract(regex, line):
    return re.search(regex, line).group(1)

def monkey_business(monkeys):
    most_active = sorted(monkeys, key=lambda monkey: monkey.inspections, reverse=True)
    for monkey in most_active:
        print(monkey.inspections)
    return most_active[0].inspections * most_active[1].inspections

def part1(data):
    monkeys = [parse_monkey(monkey_code.strip()) for monkey_code in data.split("\n\n")]
    for _ in range(0, 20):
        for monkey in monkeys:
            monkey.inspect_all(monkeys)
    print(monkeys)
    print(monkey_business(monkeys))

def parse_divisor_multiple(data):
    modulus = 1
    for monkey_code in data.split("\n\n"):
        modulus *= int(extract(r"Test: divisible by (.*?)\n", monkey_code))
    return modulus

def part2(data):
    modulus = parse_divisor_multiple(data)
    monkeys = [parse_monkey(monkey_code.strip(), modulus) for monkey_code in data.split("\n\n")]
    for _ in range(0, 10000):
        for monkey in monkeys:
            monkey.inspect_all(monkeys)
    print(monkey_business(monkeys))

part2("""
Monkey 0:
  Starting items: 65, 78
  Operation: new = old * 3
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 78, 86, 79, 73, 64, 85, 88
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 2:
  Starting items: 69, 97, 77, 88, 87
  Operation: new = old + 2
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 3:
  Starting items: 99
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 5

Monkey 4:
  Starting items: 60, 57, 52
  Operation: new = old * 19
  Test: divisible by 7
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 5:
  Starting items: 91, 82, 85, 73, 84, 53
  Operation: new = old + 5
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 6:
  Starting items: 88, 74, 68, 56
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 7:
  Starting items: 54, 82, 72, 71, 53, 99, 67
  Operation: new = old + 1
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0
""")
