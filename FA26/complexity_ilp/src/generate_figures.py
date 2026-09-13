"""Generate a real ILP solution and its slide plot, with an optional GIF."""

import argparse
import json
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--animate", action="store_true", help="Also render a GIF")
    parser.add_argument("--python", default=sys.executable, help="Python from the CG:SHOP environment")
    parser.add_argument("--instance", type=Path, help="Use an existing competition instance")
    parser.add_argument("--time-limit", type=float, default=None)
    args = parser.parse_args()
    deck = Path(__file__).resolve().parents[1]
    workspace = deck.parents[2]
    utils = workspace / "CG-SHOP-27" / "src" / "utils"
    images = deck / "images"
    images.mkdir(exist_ok=True)
    name = args.instance.name.removesuffix(".instance.json") if args.instance else "exact_demo"
    instance = args.instance.resolve() if args.instance else images / "exact_demo.instance.json"
    solution = images / f"{name}.solution.json"
    if args.instance is None:
        instance.write_text(json.dumps({
            "content_type": "CGSHOP2027_Instance",
            "instance_uid": "exact-donut-demo",
            "region_to_cover": {
                "outer_boundary": {"x": [0, 4, 4, 0], "y": [0, 0, 4, 4]},
                "inner_boundaries": [{"x": [1, 1, 3, 3], "y": [1, 3, 3, 1]}],
            },
            "cutter": {"x": [0, 1, 1, 0], "y": [0, 0, 1, 1]},
            "cutter_center": [0, 0],
            "number_of_cutters": 2,
        }), encoding="utf-8")
    command = [
        args.python, str(utils / "solve.py"), str(instance), str(solution),
        "--image", str(images / f"{name}.png"),
    ]
    if args.time_limit is not None:
        command.extend(["--time-limit", str(args.time_limit)])
    subprocess.run(command, check=True)
    if args.animate:
        subprocess.run([
            args.python, str(utils / "display.py"), str(instance), str(solution),
            "--animate", "--output", str(images / f"{name}.gif"),
        ], check=True)


if __name__ == "__main__":
    main()
