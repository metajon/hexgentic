# How to Use Hexgen

## 1. Set up the project

Hexgen requires Python 3.10 or newer.

### With Anaconda or Miniconda

From the project root, create a conda environment and install the project dependencies:

```bash
conda create --name hexgen python=3.12
conda activate hexgen

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Activate the environment whenever you work on the project:

```bash
conda activate hexgen
```

To leave it when you are finished, run `conda deactivate`.

### With Python's built-in virtual environment

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 2. Generate a map

Create a script based on `bin/example.py`, then call `generate` with map options:

```python
from hexgen import generate
from hexgen.enums import MapType

options = {
    'map_type': MapType.terran,
    'size': 100,
    'avg_temp': 15,
    'sea_percent': 60,
    'hydrosphere': True,
    'num_rivers': 50,
    'num_territories': 0,
}

mapgen = generate(options, image=True)
```

The generated PNG maps are written to the `output` directory.

To run the included example directly, first activate the conda environment and then run:

```bash
python bin/example.py
```

You can also run it without activating the environment in the current shell:

```bash
conda run --name hexgen python bin/example.py
```

## 3. Export hex data to CSV

Add `csv=True` to create `output/map_hexes.csv` alongside the images:

```python
mapgen = generate(options, image=True, csv=True)
```

To use a different filename, provide `csv_filename`:

```python
mapgen = generate(options, image=False, csv=True,
                  csv_filename='my_map.csv')
```

Each CSV row represents a hex. The `x` and `y` columns identify its map coordinate.

## 4. Edit a generated map

Open the exported CSV in a spreadsheet editor or text editor. Preserve the column names and the `x` and `y` coordinates. The editable columns are:

- `altitude`
- `moisture`
- `features`: semicolon-separated feature names, such as `volcano;crater`
- `resource_type` and `resource_rating`: supply both fields together or leave both blank
- `territory`
- `river_sides`: semicolon-separated sides, such as `east;north_east`

Other columns are derived from the map data and are recalculated when the map is rendered.

## 5. Render the edited CSV

Pass the edited export through `csv_input` when generating the map. The CSV values are applied before the PNGs are drawn:

```python
mapgen = generate(options, image=True, csv_input='my_map.csv')
```

Use the same generation options as the original map, especially `size`, `num_territories`, and a fixed `random_seed` when you need repeatable base generation.

## 6. Run tests

Run the test suite from the project root:

```bash
python -m unittest discover -s hexgen/test
```
