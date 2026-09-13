"""Run with the CG:SHOP Python environment."""

from pathlib import Path
import sys

DECK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DECK.parents[2] / "CG-SHOP-27" / "src" / "utils"))
from cgshop2027_pyutils.io import read_instance
from exact_ilp import solve_exact

instance = read_instance(DECK / "images" / "exact_demo.instance.json")
solution = solve_exact(instance)
print("Longest route:", solution.max_tour_length)
print("Global optimum:", solution.meta["global_optimal"])
assert solution.meta["global_optimal"] and solution.max_tour_length == 8
