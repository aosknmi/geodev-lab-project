
import geopandas as gpd

# Read datasets
oyo = gpd.read_file("data/processed/Oyo_State_Shp.gpkg")
facilities = gpd.read_file("data/processed/Health_Facilities_Oyo_State.gpkg")

# Reproject to UTM Zone 31N
oyo_utm = oyo.to_crs(epsg=32631)
facilities_utm = facilities.to_crs(epsg=32631)

# Spatial join: assign facilities to polygons
joined = gpd.sjoin(
    facilities_utm,
    oyo_utm[["geometry"]],
    how="left",
    predicate="within"
)

# Count facilities in each polygon
counts = joined.groupby("index_right").size()

# Merge counts back to Oyo State polygons
oyo_utm["facility_count"] = counts.reindex(
    oyo_utm.index,
    fill_value=0
)

# Print results
print(oyo_utm[["facility_count"]])

print(
    "Total counted facilities:",
    oyo_utm["facility_count"].sum()
)

print(
    "Original facility records:",
    len(facilities_utm)
)