# Complexity and Integer Linear Programming

Build with `latexmk -pdf main.tex` from this folder. Bullet points and paragraphs
reveal incrementally. Add `handout` to the document class for one page per frame.

The CG:SHOP section presents the complete grid-edge ILP, including its
finite-domain proof, parity, connectivity flow, and Euler extraction.
The saved slide figures and example solutions are included in `images/`.
The solver-dependent demo scripts have been removed. The code in the slides
illustrates the formulation and does not require changes to the CG:SHOP solver.

The four-by-four demonstration has optimum 8, proved by both the complete ILP
and an independent integer closed-walk enumeration. Run `python src/prove_demo.py`
to check the saved solution and regenerate `images/exact_demo.proof.json`.
Every closed walk has even length. No closed walk of length at most 6 covers
more than 4 required cells, so two such walks cannot cover all 12 cells.
The validated length-8 solution attains this lower bound.
