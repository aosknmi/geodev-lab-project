
import geopandas as gpd

# Read datasets
oyo = gpd.read_file("data/processed/Oyo_State_Shp.gpkg")
facilities = gpd.read_file("data/processed/Health_Facilities_Oyo_State.gpkg")

# Reproject to UTM Zone 31N
oyo_utm = oyo.to_crs(epsg=32631)
facilities_utm = facilities.to_crs(epsg=32631)

# Create 5 km buffers around health facilities
buffers = facilities_utm.geometry.buffer(5000)

# Dissolve all buffers into one coverage area
coverage_area = buffers.union_all()

# Combine Oyo State boundary geometries
oyo_boundary = oyo_utm.geometry.union_all()

# Find areas outside the health facility coverage
uncovered = oyo_boundary.difference(coverage_area)

# Create a GeoDataFrame for uncovered areas
uncovered_gdf = gpd.GeoDataFrame(
    {"area_km2": [uncovered.area / 1_000_000]},
    geometry=[uncovered],
    crs=oyo_utm.crs
)

# Print results
print("Coverage buffer: 5 km")
print(
    "Uncovered area:",
    round(uncovered_gdf["area_km2"].iloc[0], 2),
    "km2"
)

print("Uncovered geometry:")
print(uncovered_gdf)