from collections import namedtuple
from itertools import combinations
from math import sqrt

from more_itertools import flatten

Point = namedtuple("Point", ["x", "y"])


def upper_hull(points: set[Point]) -> list[Point]:
    """
    @param      `points` an unordered collection of Points in 2D space
    @returns    sequence of points defining the upper hull of `points`,
                    given in counter-clockwise order.
    """
    ...


def sin_angle(p1: Point, p2: Point) -> float:
    """Sin of the angle of the ray p1->p2"""
    return (p2.y - p1.y) / sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def cross(o: Point, a: Point, b: Point) -> float:
    """Signed area of o->a, o->b"""
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def point_below_line(line: tuple[Point, Point], point: Point) -> bool:
    return cross(line[0], line[1], point) >= 0


def upper_hull_1(points: set[Point]) -> list[Point]:
    hull_segments = []
    for p1, p2 in combinations(points, 2):
        p1, p2 = max(p1, p2), min(p1, p2)  # orient to the 'left'
        if all(point_below_line((p1, p2), q) for q in points):
            hull_segments.append((p1, p2))
    return sorted(set(flatten(hull_segments)), reverse=True)


def upper_hull_2(points: set[Point]) -> list[Point]:
    hull_segments = []
    for p1 in points - {min(points)}:
        p2 = max((q for q in points if q < p1), key=lambda q: sin_angle(p1, q))
        if all(point_below_line((p1, p2), q) for q in points):
            hull_segments.append((p1, p2))
    return sorted(set(flatten(hull_segments)), reverse=True)


def upper_hull_3(points: set[Point]) -> list[Point]:
    hull = []
    for point in sorted(points, reverse=True):
        while len(hull) >= 2 and not point_below_line((hull[-2], hull[-1]), point):
            hull.pop()
        hull.append(point)
    return hull


def main():
    pass


if __name__ == "__main__":
    main()
