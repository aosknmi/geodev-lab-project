# Week 10: GeoPandas, Layers as Tables

## What this folder contains

This folder contains my Week 10 GeoPandas exercises and independent
challenge using Oyo State health facilities data.

### Guided exercises

-   `explore_pandas.py`: Explores the ward population table.
-   `filter_sort.py`: Filters and sorts tabular data.
-   `explore_layers.py`: Explores spatial layers and their attributes.
-   `play_geom_props.py`: Explores GeoPandas geometry properties.
-   `csv_to_points.py`: Converts CSV coordinates into spatial point
    data.
-   `join_population.py`: Joins population data to ward polygons after
    cleaning names.
-   `make_map.py`: Creates a map of health facilities by ward.
-   `save_outputs.py`: Saves the processed outputs.

### Guided outputs

-   `facilities_map.png`: Map showing health facilities by ward.
-   `wards_table.csv`: Exported ward attribute table.

### Independent challenge

-   `my_explore.py`: Loads and explores the Oyo State health facilities
    GeoPackage, checking its layers, rows and columns, geometry types,
    CRS, and bounds.
-   `my_points.py`: Converts the Oyo State health facilities CSV
    coordinates into point geometries and saves them as a GeoPackage.
-   `my_join.py`: Joins the health facilities CSV table to the
    GeoPackage and checks matching records before and after cleaning
    facility names.
-   `my_map.png`: Map showing the spatial distribution of health
    facilities in Oyo State.

## How to run it

From the repository root, run the guided scripts using:

``` bash
uv run month-03/week-10/explore_pandas.py
uv run month-03/week-10/filter_sort.py
uv run month-03/week-10/explore_layers.py
uv run month-03/week-10/play_geom_props.py
uv run month-03/week-10/csv_to_points.py
uv run month-03/week-10/join_population.py
uv run month-03/week-10/make_map.py
uv run month-03/week-10/save_outputs.py
```

Run the independent challenge scripts:

``` bash
uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py
```

## What I found

I explored tabular and spatial data using Pandas and GeoPandas. I
learned how to inspect GeoPackage layers, examine geometry properties,
convert CSV coordinates into spatial points, and join tabular data to
spatial datasets.

Using my own Oyo State health facilities data, I explored the dataset,
converted facility coordinates into point geometries, performed
attribute joins, and created a map showing the distribution of health
facilities across the state.

This exercise improved my understanding of how Python can be used to
manage, process, join, and visualize geospatial data.

## What went wrong and how I fixed it

One challenge was matching records between the CSV and GeoPackage
datasets. I checked the available columns, used common identifiers, and
cleaned facility names to improve matching.

I also paid attention to coordinate reference systems when converting
geographic coordinates into spatial point data to ensure the locations
were correctly represented.

## What I learned

-   How to explore tabular data using Pandas.
-   How to inspect and work with GeoPackage layers using GeoPandas.
-   How to convert CSV coordinates into spatial point geometries.
-   How to clean names before joining datasets.
-   How to combine tabular and spatial data.
-   How to create and save maps using GeoPandas and Matplotlib.
-   How to organize geospatial Python projects.

## Outstanding optional task

-   `population_map.png`: Optional stretch task involving a choropleth
    map of ward population using the joined `population_2024` field. Not
    completed yet.
