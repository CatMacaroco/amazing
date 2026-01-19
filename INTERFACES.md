# Maze Interface Contract

## Important: Names below for the datas will never be changed and used accross us as same names always.


## Maze Object
- main object (container) = `maze`
Nte: it is not yet created yet so it is unknown for now if its a dict, class or any other thing but the following fields of it MUST BE as they are stated in below


### Field Names of the Maze

#### 01. Dimensions Naming
    - width = maze.witdh (int value)
        - number of columns in the maze. (x-axis)

    - height = maze.height (int value)
        - number of rows in the maze. (y-axis)


#### 02. Grid
- coordination naming = maze.grid[y][x] (int 0-15)
- the maze grid is a 2D structure indexed by row first, column second.
    - `y` is the row index (0 at top)
    - `x` is the column index (0 at left)
    - each cell value is an integer bitmask representing `CLOSED` walls. (note: later on path will be carved by removing walls from the maze.)
    - their values are integer bitmask
    - value range is always `0 <= value <= 15`


### 03. Wall bit encoding
    - bit 0 (value 1) → North wall
    - bit 1 (value 2) → East wall
    - bit 2 (value 4) → South wall
    - bit 3 (value 8) → West wall
Bit meaning:
- `1` = wall is `CLOSED`
- `0` = wall is `OPEN`

Valid cell values are always in range `0` to `15`.


## 04. Coordinates vs Grid Indexing

this section explains the relationship between **coordinates** and **grid indexing**.
Both are used together and must not be confused.


### 05. Coordinates (Semantic / Geometric)

all positions in the maze (entry, exit, movement, path steps) are represented
as **(x, y)** tuples.

    - `x` → horizontal position (column index)
    - `y` → vertical position (row index)

coordinate system:
- `(0, 0)` is the **top-left** cell
- `x` increases to the **right**
- `y` increases **downward**

examples:
- `(0, 0)` → top-left corner
- `(1, 0)` → one cell to the right
- `(0, 1)` → one cell below


### 06. Grid Indexing (Storage / Data Structure)

the maze grid is stored as a 2D structure accessed as:

    - `maze.grid[y][x]`

reason:
- `maze.grid` is a list of rows
- each row is a list of columns

so:
- first index = row (`y`)
- second index = column (`x`)


### 07. Relationship Between the Two Terms

given a coordinate `(x, y)`:
- the corresponding cell value is always accessed as:
    > `maze.grid[y][x]`

this rule is used consistently throughout:
- maze generation
- pathfinding
- validation
- visualization

**Rule to remember:**
> coordinates are `(x, y)`, but grid access is always `grid[y][x]`.


## 08. Entry and Exit

- `maze.entry` : `(x, y)`
- `maze.exit`  : `(x, y)`

rules:
- both coordinates are within bounds
- entry and exit are distinct


## 09. Path (Solver Output)

- `maze.path` : str

the path is a string of directions:
- characters are one of: `N`, `E`, `S`, `W`
- example: `"NNEEESNNWSWSNEEEESW"`

the path may be an empty string (`""`) if:
    - the solver has not been run yet
    - or solution output is hidden


## 10. Responsibilities

- person B (parser / visualization) may `READ` all fields above.
- person A (generation / solving) is responsible for POPULATING:
  - `maze.grid`
  - `maze.path`