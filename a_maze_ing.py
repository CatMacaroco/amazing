#!/usr/bin/env python3
from __future__ import annotations

import sys

from config_parser import load_config


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 a_maze_ing.py <config.txt>")
        return 2

    config_path = argv[1]
    try:
        cfg = load_config(config_path)
    except (OSError, ValueError) as e:
        print(f"Error: {e}")
        return 1

    print("Config loaded successfully:")
    print(f"  size: {cfg.width}x{cfg.height}")
    print(f"  entry: {cfg.entry}")
    print(f"  exit: {cfg.exit}")
    print(f"  perfect: {cfg.perfect}")
    print(f"  seed: {cfg.seed}")
    print(f"  output: {cfg.output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
