"""Independently certify the four-by-four holed example using integer walks.

Run with the CG:SHOP environment. No optimizer is used in this proof check.
"""

import json
from pathlib import Path
import sys

DECK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DECK.parents[2] / "CG-SHOP-27" / "src" / "utils"))
from cgshop2027_pyutils.io import read_instance, read_solution
from cgshop2027_pyutils.verify import SolutionValidator


def prove():
    instance = read_instance(DECK / "images" / "exact_demo.instance.json")
    solution = read_solution(DECK / "images" / "exact_demo.solution.json")
    validator = SolutionValidator(instance)
    errors = validator.check_for_errors(solution)
    if errors:
        raise ValueError(errors)
    cells = list(validator.region.cells())
    offsets = list(validator.cutter.cells())
    useful = [(qx - dx, qy - dy) for qx, qy in cells for dx, dy in offsets]
    # Compute the complete projection rectangle independently of the ILP code.
    x0, x1 = min(x for x, _ in useful), max(x for x, _ in useful)
    y0, y1 = min(y for _, y in useful), max(y for _, y in useful)
    points = [(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)]
    coverage = {
        p: sum(1 << j for j, q in enumerate(cells)
               if (q[0] - p[0], q[1] - p[1]) in offsets)
        for p in points
    }
    upper = solution.max_tour_length
    if upper != 8:
        raise ValueError("This certificate expects a validated length-8 solution")
    cutoff = upper - 2  # Every closed unit-grid walk has even length.
    maximum = 0
    states_checked = 0
    for root in points:
        states = {(root, coverage[root])}
        for length in range(cutoff + 1):
            states_checked += len(states)
            for position, mask in states:
                if position == root:
                    maximum = max(maximum, mask.bit_count())
            if length == cutoff:
                break
            following = set()
            for (x, y), mask in states:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (x + dx, y + dy)
                    if neighbor in coverage:
                        following.add((neighbor, mask | coverage[neighbor]))
            states = following
    if instance.number_of_cutters * maximum >= len(cells):
        raise ValueError("The per-route coverage bound does not prove optimality")
    proof = {
        "instance_uid": instance.instance_uid,
        "method": "exhaustive integer closed-walk coverage bound",
        "grid_bounds": [x0, y0, x1, y1],
        "field_cells": len(cells),
        "cutters": instance.number_of_cutters,
        "maximum_tested_length": cutoff,
        "max_cells_per_closed_walk": maximum,
        "states_checked": states_checked,
        "global_lower_bound": upper,
        "validated_upper_bound": upper,
        "global_optimum": upper,
    }
    (DECK / "images" / "exact_demo.proof.json").write_text(
        json.dumps(proof, indent=2), encoding="utf-8")
    print(json.dumps(proof, indent=2))
    return proof


if __name__ == "__main__":
    prove()
