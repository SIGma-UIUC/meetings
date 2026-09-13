# Complexity and Integer Linear Programming

Build with `latexmk -pdf main.tex` from this folder. Bullet points and paragraphs
reveal incrementally. Add `handout` to the document class for one page per frame.

The CG:SHOP section now presents the complete grid-edge ILP, including its
finite-domain proof, parity, connectivity flow, and Euler extraction. It keeps
the existing title and author. The implementation and detailed proof are in
`CG-SHOP-27/src/utils/exact_ilp.py` and `CG-SHOP-27/src/utils/EXACT_ILP.md`.

Activate the CG:SHOP environment after `uv sync` in its `src/utils` folder.
From this presentation folder run:

```sh
python src/generate_figures.py --animate
```

This creates and solves a 4-by-4 field with a 2-by-2 hole and two unit cutters.
The exact optimum is 8. Files are named `images/exact_demo.*`. The default
search has no time limit. Supply `--time-limit SECONDS` to bound optimization
and inspect the solution's `global_optimal` flag before claiming optimality.
Use `--instance PATH` for a different instance or `--python PATH` to select the
CG:SHOP environment's interpreter. The larger instances can exceed the exact
model's explicit allocation limits. No route-pool fallback is used.

`python src/exact_demo.py` runs the complete solve-and-validate example.

The old `src/route_pool_demo.py`, `images/demo.*`, and `images/isoa_*` files are
historical restricted-pool examples. They do not establish global optimality
and are no longer used by the presentation. `images/exact_small.*` is a
separate globally solved 3-by-3 example with optimum 6.

The four-by-four demonstration has optimum 8, proved by both the complete ILP
and an independent integer closed-walk enumeration. Run `python src/prove_demo.py`
to check the saved solution and regenerate `images/exact_demo.proof.json`.
Every closed walk has even length. No closed walk of length at most 6 covers
more than 4 required cells, so two such walks cannot cover all 12 cells.
The validated length-8 solution attains this lower bound.
