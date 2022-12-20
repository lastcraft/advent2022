import re

class Tree:
    def __init__(self, here, unvisited, valves, distances, remaining, score):
        self.here = here
        self.remaining = remaining
        self.score = score + remaining * valves[self.here]["flow"]
        self.children = []
        for tag in unvisited:
            if remaining - distances[self.here][tag] - 1 > 0:
                self.children.append(
                    Tree(tag,
                         unvisited - {tag},
                         valves,
                         distances,
                         remaining - distances[self.here][tag] - 1,
                         self.score))

    def walk(self, visitor, path=[]):
        visitor(path[:] + [self.here], self.score)
        for child in self.children:
            child.walk(visitor, path[:] + [self.here])

def parse(data):
    valves = {}
    for line in data.split("\n"):
        if line:
            valve = {}
            valve["tag"] = extract(r"Valve (.+?) has", line)
            valve["flow"] = int(extract(r"rate=(\d+?);", line))
            valve["links"] = extract(r" to .+? (.*)", line).strip().split(", ")
            valves[valve["tag"]] = valve
    return valves

def extract(regex, line):
    return re.search(regex, line).group(1)

def calculate_distances(valves):
    distances = {key2: {key: None for key in valves.keys()} for key2 in valves.keys()}
    for valve in valves.values():
        for link in valve["links"]:
            distances[valve["tag"]][link] = 1
    while(True):
        work_done = False
        for from_here in distances.values():
            for via, hop in from_here.items():
                if hop:
                    for there, to_there in distances[via].items():
                        if to_there:
                            if not from_here[there] or hop + to_there < from_here[there]:
                                from_here[there] = hop + to_there
                                work_done = True
        if not work_done:
            break
    return distances

def show(path, score):
    print(path, score)

def part1(data):
    valves = parse(data)
    useful = set([tag for tag in valves if valves[tag]["flow"] > 0])
    distances = calculate_distances(valves)
    tree = Tree("AA", useful, valves, distances, 30, 0)
    best = {"score": 0, "path": []}
    def solve(path, score):
        if score > best["score"]:
            best["path"] = path
            best["score"] = score
    tree.walk(solve)
    print(best)

part1("""
Valve QE has flow rate=3; tunnels lead to valves OU, ME, UX, AX, TW
Valve TN has flow rate=16; tunnels lead to valves UW, CG, WB
Valve UX has flow rate=0; tunnels lead to valves AA, QE
Valve HK has flow rate=5; tunnels lead to valves HT, QU, TW, WV, OK
Valve SK has flow rate=14; tunnels lead to valves GH, GA, XM
Valve HY has flow rate=0; tunnels lead to valves LG, AA
Valve BK has flow rate=0; tunnels lead to valves SZ, AA
Valve BY has flow rate=11; tunnels lead to valves SP, HS, DN, KD, TK
Valve GR has flow rate=0; tunnels lead to valves FE, OK
Valve OH has flow rate=0; tunnels lead to valves BM, KE
Valve DC has flow rate=0; tunnels lead to valves AX, XH
Valve YS has flow rate=0; tunnels lead to valves XH, EU
Valve KP has flow rate=0; tunnels lead to valves KI, OF
Valve LG has flow rate=0; tunnels lead to valves FE, HY
Valve FE has flow rate=4; tunnels lead to valves RU, GR, YI, LG, ME
Valve NK has flow rate=0; tunnels lead to valves SD, BM
Valve EU has flow rate=0; tunnels lead to valves NS, YS
Valve OF has flow rate=0; tunnels lead to valves CJ, KP
Valve TW has flow rate=0; tunnels lead to valves HK, QE
Valve GL has flow rate=0; tunnels lead to valves AF, CQ
Valve OU has flow rate=0; tunnels lead to valves KN, QE
Valve BM has flow rate=24; tunnels lead to valves GH, NK, YH, OH
Valve GA has flow rate=0; tunnels lead to valves SK, SZ
Valve EI has flow rate=17; tunnels lead to valves ZX, AF
Valve QN has flow rate=25; tunnel leads to valve SD
Valve ZX has flow rate=0; tunnels lead to valves EI, WB
Valve ME has flow rate=0; tunnels lead to valves QE, FE
Valve CJ has flow rate=21; tunnels lead to valves OF, YI, KD
Valve AX has flow rate=0; tunnels lead to valves DC, QE
Valve LW has flow rate=0; tunnels lead to valves AA, HT
Valve CQ has flow rate=18; tunnels lead to valves GL, XM
Valve KN has flow rate=0; tunnels lead to valves SZ, OU
Valve HS has flow rate=0; tunnels lead to valves UZ, BY
Valve RU has flow rate=0; tunnels lead to valves TK, FE
Valve SZ has flow rate=6; tunnels lead to valves WV, GA, BK, KE, KN
Valve AF has flow rate=0; tunnels lead to valves GL, EI
Valve YI has flow rate=0; tunnels lead to valves FE, CJ
Valve HT has flow rate=0; tunnels lead to valves LW, HK
Valve WV has flow rate=0; tunnels lead to valves SZ, HK
Valve TK has flow rate=0; tunnels lead to valves BY, RU
Valve GH has flow rate=0; tunnels lead to valves BM, SK
Valve CG has flow rate=0; tunnels lead to valves TN, SP
Valve AA has flow rate=0; tunnels lead to valves HY, UX, VQ, LW, BK
Valve SP has flow rate=0; tunnels lead to valves BY, CG
Valve XM has flow rate=0; tunnels lead to valves SK, CQ
Valve DN has flow rate=0; tunnels lead to valves NS, BY
Valve XH has flow rate=22; tunnels lead to valves YS, QU, UZ, DC
Valve KI has flow rate=20; tunnels lead to valves UW, KP
Valve OK has flow rate=0; tunnels lead to valves HK, GR
Valve YH has flow rate=0; tunnels lead to valves VQ, BM
Valve UZ has flow rate=0; tunnels lead to valves XH, HS
Valve KE has flow rate=0; tunnels lead to valves OH, SZ
Valve VQ has flow rate=0; tunnels lead to valves AA, YH
Valve QU has flow rate=0; tunnels lead to valves HK, XH
Valve WB has flow rate=0; tunnels lead to valves TN, ZX
Valve UW has flow rate=0; tunnels lead to valves KI, TN
Valve SD has flow rate=0; tunnels lead to valves NK, QN
Valve NS has flow rate=23; tunnels lead to valves EU, DN
Valve KD has flow rate=0; tunnels lead to valves BY, CJ
""")
