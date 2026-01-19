PY=python3

install:
	$(PY) -m pip install -U pip
	$(PY) -m pip install -U flake8 mypy

run:
	$(PY) a_maze_ing.py config.default.txt

debug:
	$(PY) -m pdb a_maze_ing.py config.default.txt

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache dist build *.egg-info

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
