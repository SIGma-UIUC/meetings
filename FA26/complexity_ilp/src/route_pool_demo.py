"""Run the slide example with NumPy and SciPy installed."""
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

cover = np.array([[1, 0, 1], [1, 0, 1],
                  [0, 1, 1], [0, 1, 1]])
length = np.array([6, 6, 10])  # A, B, D
C, m = 2, len(length)
n = C * m + 1                # flattened x, then L
objective = np.r_[np.zeros(C * m), 1]
upper = np.r_[np.ones(C * m), np.inf]
rows, lower, higher = [], [], []

for i in range(C):
    block = slice(i * m, (i + 1) * m)
    row = np.zeros(n)
    row[block] = 1
    rows.append(row)
    lower.append(1)
    higher.append(1)

    row = np.zeros(n)
    row[block], row[-1] = length, -1
    rows.append(row)
    lower.append(-np.inf)
    higher.append(0)

for cell in cover:
    rows.append(np.r_[np.tile(cell, C), 0])
    lower.append(1)
    higher.append(np.inf)

result = milp(
    c=objective, integrality=np.ones(n),
    bounds=Bounds(np.zeros(n), upper),
    constraints=LinearConstraint(rows, lower, higher),
    options={"time_limit": 30, "mip_rel_gap": 0.0})

if result.x is None:
    raise RuntimeError(result.message)
chosen = result.x[:-1].reshape(C, m) > 0.5
routes = [np.flatnonzero(row).item() for row in chosen]
print("Routes:", routes)  # [0, 1] or [1, 0]
print("Longest:", max(length[p] for p in routes))  # 6
print("Pool optimum proved:", result.status == 0)

assert np.all(chosen.sum(axis=1) == 1)
assert np.all(cover @ chosen.sum(axis=0) >= 1)
assert result.status == 0 and abs(result.fun - 6) < 1e-6
