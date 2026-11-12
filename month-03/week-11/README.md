# Week 11: CRS and Spatial Operations

## What this folder contains

This folder contains my Week 11 GeoPandas exercises and independent challenge using Oyo State administrative boundaries and health facilities data.

## Guided exercises

area_wrong_and_right.py: Compares area calculations in geographic and projected coordinate reference systems.

set_vs_to.py: Explores the difference between setting a CRS and reprojecting a spatial layer.

one_point.py: Works with individual point geometries and coordinate reference systems.

spatial_ops.py: Explores spatial operations using GeoPandas.

coverage_gap.py: Analyses health facility coverage using buffer and overlay operations.

nearest.py: Explores nearest-distance analysis between spatial features.

clip_dissolve.py: Performs clipping and dissolving operations on spatial datasets.

fix_geometry.py: Checks and repairs invalid geometries.

## Guided outputs

Processed spatial layers and analysis results generated from the guided exercises.

## Independent challenge

my_crs.py: Loads the Oyo State boundary and health facilities GeoPackages, checks their CRS, estimates the appropriate UTM zone, reprojects the datasets to EPSG:32631, and calculates the area of Oyo State in square kilometres.

my_count.py: Uses spatial joins and groupby operations to count health facilities within the Oyo State boundary, merges the counts back to the polygon layer, and prints the total-counted check.

my_reach.py: Creates 5 km buffers around health facilities, dissolves the buffers, and identifies uncovered areas using the overlay difference operation.

my_validity.py: Checks invalid geometries in the Oyo State polygon layer, repairs them using make_valid(), and prints the invalid geometry count before and after correction.

## Independent challenge outputs

uncovered_areas.gpkg: GeoPackage containing the identified areas outside the 5 km health facility coverage zones.

health_facility_coverage.png: Map showing the Oyo State boundary, health facility locations, and uncovered areas.

## How to run it

From the repository root, run the guided scripts using:

```bash
uv run month-03/week-11/area_wrong_and_right.py
uv run month-03/week-11/set_vs_to.py
uv run month-03/week-11/one_point.py
uv run month-03/week-11/spatial_ops.py
uv run month-03/week-11/coverage_gap.py
uv run month-03/week-11/nearest.py
uv run month-03/week-11/clip_dissolve.py
uv run month-03/week-11/fix_geometry.py
```

Run the independent challenge scripts:

```bash
uv run month-03/week-11/my_crs.py
uv run month-03/week-11/my_count.py
uv run month-03/week-11/my_reach.py
uv run month-03/week-11/my_validity.py
```

## What I found

I explored Coordinate Reference Systems and spatial operations using GeoPandas. I learned how to distinguish between setting and reprojecting a CRS, calculate areas using projected coordinates, perform spatial joins, create buffers, dissolve geometries, calculate coverage gaps, and validate geometries.

Using my own Oyo State health facilities data, I reprojected both datasets from EPSG:4326 to EPSG:32631 (WGS 84 / UTM Zone 31N), calculated the state's area, counted health facilities, and identified areas outside a 5 km facility coverage radius.

I also created a map to visualize the distribution of health facilities and the identified coverage gaps.

This exercise improved my understanding of how coordinate reference systems and spatial operations can be applied to real-world geospatial problems using Python.

## What went wrong and how I fixed it

One important challenge was working with geographic coordinates (EPSG:4326) for area and distance calculations. Since geographic coordinates are measured in degrees, I reprojected the datasets to EPSG:32631 before performing metric calculations.

I also considered geometry validity before carrying out spatial operations and used make_valid() to repair invalid polygon geometries where necessary.

Another consideration was choosing an appropriate buffer distance. I used 5 km as an assumed proximity threshold to identify areas outside the health facility coverage zones.

## Methodological limitation

The 5 km buffer analysis measures straight-line distance rather than actual road travel distance. It also assumes that all mapped health facilities are operational and equally accessible. Population distribution, road conditions, facility capacity, and service availability were not considered.

## What I learned

- How to understand and work with Coordinate Reference Systems.
- The difference between setting a CRS and reprojecting a layer.
- How to select an appropriate UTM zone for spatial analysis.
- How to calculate polygon areas in square kilometres.
- How to perform spatial joins and count spatial features.
- How to create and dissolve buffers using GeoPandas.
- How to identify uncovered areas using overlay difference.
- How to check and repair invalid geometries using make_valid().
- How to visualize and save geospatial analysis results.
- How to document and organize geospatial Python projects.