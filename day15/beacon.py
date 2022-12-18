import re

class Diamond:
    def __init__(self, centre, size):
        self.centre = centre
        self.size = size

    def __repr__(self):
        return f"Diamond({self.centre}, {self.size})"

    def cover(self, y):
        distance = abs(y - self.centre[1])
        reach = self.size - distance
        if reach < 0:
            return None
        return (self.centre[0] - reach, self.centre[0] + reach)

def parse(data):
    diamonds = []
    beacons = []
    for line in data.split("\n"):
        if line:
            coords = numbers(line)
            diamonds.append(
                Diamond(
                    (coords[0], coords[1]),
                    distance(
                        (coords[0], coords[1]),
                        (coords[2], coords[3]))))
            beacons.append((coords[2], coords[3]))
    return diamonds, beacons

def numbers(text):
    return list(map(int, re.findall(r'[+-]?\d+', text)))

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def combine(covers):
    combined = [covers[0]]
    i = 0
    for cover in covers[1:]:
        if intersects(combined[i], cover):
            combined[i] = (min(combined[i][0], cover[0]), max(combined[i][1], cover[1]))
        else:
            i += 1
    return combined

def intersects(cover1, cover2):
    return cover1[1] >= cover2[0] - 1

def measure(covers):
    total = 0
    for cover in covers:
        total += cover[1] - cover[0] + 1
    return total

def beacons_at_y(beacons, y):
    return len(set([beacon for beacon in beacons if beacon[1] == y]))

def part1(data):
    diamonds, beacons = parse(data)
    covers = [cover for cover in [diamond.cover(2000000) for diamond in diamonds] if cover]
    covers.sort()
    covers = combine(covers)
    print(measure(covers) - beacons_at_y(beacons, 2000000))

part1("""
Sensor at x=2662540, y=1992627: closest beacon is at x=1562171, y=2000000
Sensor at x=3577947, y=3994226: closest beacon is at x=3468220, y=3832344
Sensor at x=34015, y=3658022: closest beacon is at x=-48386, y=3887238
Sensor at x=3951270, y=2868430: closest beacon is at x=3499312, y=2620002
Sensor at x=3136779, y=3094333: closest beacon is at x=2731027, y=3076619
Sensor at x=3415109, y=2591103: closest beacon is at x=3499312, y=2620002
Sensor at x=277465, y=3971183: closest beacon is at x=-48386, y=3887238
Sensor at x=3697201, y=1834735: closest beacon is at x=3499312, y=2620002
Sensor at x=874397, y=1535447: closest beacon is at x=1562171, y=2000000
Sensor at x=2996230, y=3508199: closest beacon is at x=3251079, y=3709457
Sensor at x=2754388, y=3147571: closest beacon is at x=2731027, y=3076619
Sensor at x=524580, y=2640616: closest beacon is at x=-73189, y=1870650
Sensor at x=2718599, y=3106610: closest beacon is at x=2731027, y=3076619
Sensor at x=2708759, y=3688992: closest beacon is at x=3251079, y=3709457
Sensor at x=2413450, y=3994713: closest beacon is at x=3251079, y=3709457
Sensor at x=1881113, y=495129: closest beacon is at x=1562171, y=2000000
Sensor at x=3792459, y=3827590: closest beacon is at x=3468220, y=3832344
Sensor at x=3658528, y=641189: closest beacon is at x=4097969, y=-110334
Sensor at x=1379548, y=3381581: closest beacon is at x=1562171, y=2000000
Sensor at x=3480959, y=3069234: closest beacon is at x=3499312, y=2620002
Sensor at x=3871880, y=3531918: closest beacon is at x=3468220, y=3832344
Sensor at x=2825206, y=2606984: closest beacon is at x=2731027, y=3076619
Sensor at x=3645217, y=2312011: closest beacon is at x=3499312, y=2620002
Sensor at x=3485320, y=3509352: closest beacon is at x=3468220, y=3832344
Sensor at x=56145, y=3879324: closest beacon is at x=-48386, y=3887238
Sensor at x=148776, y=433043: closest beacon is at x=-73189, y=1870650
Sensor at x=3368682, y=3929248: closest beacon is at x=3468220, y=3832344
Sensor at x=3330787, y=2481990: closest beacon is at x=3499312, y=2620002
Sensor at x=2802875, y=3209067: closest beacon is at x=2731027, y=3076619
Sensor at x=2679788, y=3102108: closest beacon is at x=2731027, y=3076619
Sensor at x=3326846, y=3767097: closest beacon is at x=3251079, y=3709457
Sensor at x=3111518, y=1310720: closest beacon is at x=3499312, y=2620002
""")
