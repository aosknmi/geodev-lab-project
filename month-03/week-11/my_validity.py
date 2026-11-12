
import geopandas as gpd

# Read Oyo State polygon
oyo = gpd.read_file("data/processed/Oyo_State_Shp.gpkg")

# Count invalid geometries before correction
invalid_before = (~oyo.geometry.is_valid).sum()

print("Invalid geometries before:", invalid_before)

# Fix invalid geometries
oyo["geometry"] = oyo.geometry.make_valid()

# Count invalid geometries after correction
invalid_after = (~oyo.geometry.is_valid).sum()

print("Invalid geometries after:", invalid_after)

# Print validation summary
if invalid_before == 0:
    print("All geometries were already valid.")
else:
    print("Geometry correction completed.")

print("Remaining invalid geometries:", invalid_after)