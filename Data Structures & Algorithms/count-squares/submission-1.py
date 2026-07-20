class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x = defaultdict(set)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

        self.x[point[0]].add(tuple(point))

    def count(self, point: List[int]) -> int:
        x1, y1 = point

        ctr = 0
        # print(self.x[point[0]])
        for pnt in self.x[x1]:

            x2, y2 = pnt

            if y1 == y2:
                continue

            a = abs(y1-y2)

            start = max(1, self.points[pnt])

            ctr += start * self.points.get((x1+a, y1), 0) * self.points.get((x2+a, y2), 0)

            ctr += start * self.points.get((x1-a, y1), 0) * self.points.get((x2-a, y2), 0)

        return ctr