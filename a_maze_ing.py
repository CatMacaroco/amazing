#!/usr/bin/env python3
from __future__ import annotations

import sys

from config_parser import load_config
from output_writer import write_output
from visualizer import run_ui_loop


class DummyMaze:
    """Temporary maze for testing UI"""
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = [[15 for _ in range(width)] for _ in range(height)]


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

    # TEMPORARY state provider (replace with real generator/solver)
    def get_state() -> tuple[object, str]:
        maze = DummyMaze(cfg.width, cfg.height)
        path = ""
        write_output(cfg.output_file, maze, cfg.entry, cfg.exit, path)
        return maze, path
    try:
        run_ui_loop(get_state, cfg.entry, cfg.exit)
    except (OSError, ValueError) as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
