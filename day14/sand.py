class BoundingBox:
    def __init__(self, x0, x1, y0, y1):
        self.x0, self. x1, self.y0, self.y1 = x0, x1, y0, y1

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def add(self, point):
        return Point(point.x + self.x, point.y + self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

def parse(data):
    surfaces = []
    for line in data.split("\n"):
        if line:
            surfaces.append([Point(*list(map(int, points.split(",")))) for points in line.split(" -> ")])
    return surfaces

def bounding_box(walls):
    x0, x1, y0, y1 = 9999, 0, 9999, 0
    for wall in walls:
        for point in wall:
            x0 = min(x0, point.x)
            x1 = max(x1, point.x)
            y0 = min(y0, point.y,  0)
            y1 = max(y1, point.y)
    return BoundingBox(x0, x1 + 1, y0, y1 + 1)

class Cave:
    def __init__(self, bbox):
        self.bbox = bbox
        line = list(map(lambda _: ".", list(range(bbox.x0, bbox.x1))))
        self.lines = list(map(lambda _: line[:], list(range(bbox.y0, bbox.y1))))

    def plot(self, point, sprite):
        if point.y < self.bbox.y0 or point.y >= self.bbox.y1:
            raise ValueError()
        if point.x < self.bbox.x0 or point.x >= self.bbox.x1:
            raise ValueError()
        self.lines[point.y - self.bbox.y0][point.x - self.bbox.x0] = sprite

    def peek(self, point):
        if point.y < self.bbox.y0 or point.y >= self.bbox.y1:
            raise ValueError()
        if point.x < self.bbox.x0 or point.x >= self.bbox.x1:
            raise ValueError()
        return self.lines[point.y - self.bbox.y0][point.x - self.bbox.x0]

    def paint(self):
        for line in self.lines:
            print("".join(line))

def paint(cave, wall):
    for i in range(0, len(wall) - 1):
        direction = Point(
            one(wall[i + 1].x - wall[i].x),
            one(wall[i + 1].y - wall[i].y))
        point = wall[i]
        for _ in range(0, abs(wall[i + 1].x - wall[i].x) + abs(wall[i + 1].y - wall[i].y) + 1):
            cave.plot(point, "#")
            point = point.add(direction)

def one(n):
    return min(1, max(-1, n))

def drop_sand(cave, point):
    cave.peek(point.add(Point(0, 1)))
    if cave.peek(point.add(Point(0, 1))) == ".":
        drop_sand(cave, point.add(Point(0, 1)))
    else:
        if cave.peek(point.add(Point(-1, 1))) == ".":
            drop_sand(cave, point.add(Point(-1, 1)))
        elif cave.peek(point.add(Point(1, 1))) == ".":
            drop_sand(cave, point.add(Point(1, 1)))
        else:
            cave.plot(point, "o")
    pass

def part1(data):
    walls = parse(data)
    cave = Cave(bounding_box(walls))
    for wall in walls:
        paint(cave, wall)
    n = 0
    while(True):
        try:
            drop_sand(cave, Point(500, 0))
            n += 1
        except ValueError:
            break
    print(n)
    # cave.paint()

part1("""
498,13 -> 498,16 -> 496,16 -> 496,20 -> 509,20 -> 509,16 -> 502,16 -> 502,13
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
481,79 -> 485,79
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
493,85 -> 497,85
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
499,85 -> 503,85
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
482,107 -> 487,107
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
505,129 -> 505,131 -> 504,131 -> 504,135 -> 517,135 -> 517,131 -> 509,131 -> 509,129
496,82 -> 500,82
505,129 -> 505,131 -> 504,131 -> 504,135 -> 517,135 -> 517,131 -> 509,131 -> 509,129
489,148 -> 489,149 -> 501,149 -> 501,148
482,49 -> 487,49
488,24 -> 488,25 -> 499,25 -> 499,24
494,61 -> 494,63 -> 490,63 -> 490,70 -> 499,70 -> 499,63 -> 498,63 -> 498,61
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
500,138 -> 500,142 -> 498,142 -> 498,146 -> 513,146 -> 513,142 -> 506,142 -> 506,138
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
489,148 -> 489,149 -> 501,149 -> 501,148
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
498,13 -> 498,16 -> 496,16 -> 496,20 -> 509,20 -> 509,16 -> 502,16 -> 502,13
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
478,82 -> 482,82
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
493,79 -> 497,79
471,52 -> 476,52
469,58 -> 474,58
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
469,103 -> 469,104 -> 484,104 -> 484,103
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
494,61 -> 494,63 -> 490,63 -> 490,70 -> 499,70 -> 499,63 -> 498,63 -> 498,61
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
479,29 -> 489,29 -> 489,28
475,85 -> 479,85
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
490,76 -> 494,76
486,109 -> 491,109
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
489,49 -> 494,49
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
505,129 -> 505,131 -> 504,131 -> 504,135 -> 517,135 -> 517,131 -> 509,131 -> 509,129
488,24 -> 488,25 -> 499,25 -> 499,24
476,58 -> 481,58
476,111 -> 481,111
490,82 -> 494,82
483,111 -> 488,111
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
488,24 -> 488,25 -> 499,25 -> 499,24
479,56 -> 484,56
500,138 -> 500,142 -> 498,142 -> 498,146 -> 513,146 -> 513,142 -> 506,142 -> 506,138
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
473,113 -> 478,113
480,113 -> 485,113
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
481,85 -> 485,85
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
498,13 -> 498,16 -> 496,16 -> 496,20 -> 509,20 -> 509,16 -> 502,16 -> 502,13
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
490,111 -> 495,111
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
468,54 -> 473,54
484,76 -> 488,76
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
505,129 -> 505,131 -> 504,131 -> 504,135 -> 517,135 -> 517,131 -> 509,131 -> 509,129
483,58 -> 488,58
498,13 -> 498,16 -> 496,16 -> 496,20 -> 509,20 -> 509,16 -> 502,16 -> 502,13
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
465,56 -> 470,56
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
481,45 -> 486,45
494,61 -> 494,63 -> 490,63 -> 490,70 -> 499,70 -> 499,63 -> 498,63 -> 498,61
494,113 -> 499,113
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
489,148 -> 489,149 -> 501,149 -> 501,148
472,56 -> 477,56
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
500,138 -> 500,142 -> 498,142 -> 498,146 -> 513,146 -> 513,142 -> 506,142 -> 506,138
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
475,54 -> 480,54
485,47 -> 490,47
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
498,13 -> 498,16 -> 496,16 -> 496,20 -> 509,20 -> 509,16 -> 502,16 -> 502,13
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
500,138 -> 500,142 -> 498,142 -> 498,146 -> 513,146 -> 513,142 -> 506,142 -> 506,138
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
505,129 -> 505,131 -> 504,131 -> 504,135 -> 517,135 -> 517,131 -> 509,131 -> 509,129
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
505,129 -> 505,131 -> 504,131 -> 504,135 -> 517,135 -> 517,131 -> 509,131 -> 509,129
484,82 -> 488,82
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
494,61 -> 494,63 -> 490,63 -> 490,70 -> 499,70 -> 499,63 -> 498,63 -> 498,61
500,138 -> 500,142 -> 498,142 -> 498,146 -> 513,146 -> 513,142 -> 506,142 -> 506,138
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
462,58 -> 467,58
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
498,13 -> 498,16 -> 496,16 -> 496,20 -> 509,20 -> 509,16 -> 502,16 -> 502,13
487,113 -> 492,113
487,73 -> 491,73
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
505,129 -> 505,131 -> 504,131 -> 504,135 -> 517,135 -> 517,131 -> 509,131 -> 509,129
469,103 -> 469,104 -> 484,104 -> 484,103
487,79 -> 491,79
479,29 -> 489,29 -> 489,28
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
500,138 -> 500,142 -> 498,142 -> 498,146 -> 513,146 -> 513,142 -> 506,142 -> 506,138
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
487,85 -> 491,85
475,49 -> 480,49
479,109 -> 484,109
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
469,103 -> 469,104 -> 484,104 -> 484,103
494,61 -> 494,63 -> 490,63 -> 490,70 -> 499,70 -> 499,63 -> 498,63 -> 498,61
494,61 -> 494,63 -> 490,63 -> 490,70 -> 499,70 -> 499,63 -> 498,63 -> 498,61
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
485,42 -> 485,41 -> 485,42 -> 487,42 -> 487,38 -> 487,42 -> 489,42 -> 489,32 -> 489,42 -> 491,42 -> 491,33 -> 491,42 -> 493,42 -> 493,34 -> 493,42
498,13 -> 498,16 -> 496,16 -> 496,20 -> 509,20 -> 509,16 -> 502,16 -> 502,13
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
468,98 -> 468,96 -> 468,98 -> 470,98 -> 470,90 -> 470,98 -> 472,98 -> 472,90 -> 472,98 -> 474,98 -> 474,92 -> 474,98 -> 476,98 -> 476,97 -> 476,98 -> 478,98 -> 478,97 -> 478,98
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
494,61 -> 494,63 -> 490,63 -> 490,70 -> 499,70 -> 499,63 -> 498,63 -> 498,61
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
478,47 -> 483,47
500,138 -> 500,142 -> 498,142 -> 498,146 -> 513,146 -> 513,142 -> 506,142 -> 506,138
493,126 -> 493,123 -> 493,126 -> 495,126 -> 495,117 -> 495,126 -> 497,126 -> 497,123 -> 497,126 -> 499,126 -> 499,122 -> 499,126 -> 501,126 -> 501,119 -> 501,126 -> 503,126 -> 503,125 -> 503,126 -> 505,126 -> 505,122 -> 505,126
478,162 -> 478,154 -> 478,162 -> 480,162 -> 480,159 -> 480,162 -> 482,162 -> 482,156 -> 482,162 -> 484,162 -> 484,161 -> 484,162 -> 486,162 -> 486,155 -> 486,162 -> 488,162 -> 488,159 -> 488,162 -> 490,162 -> 490,158 -> 490,162 -> 492,162 -> 492,159 -> 492,162 -> 494,162 -> 494,158 -> 494,162 -> 496,162 -> 496,153 -> 496,162
""")
