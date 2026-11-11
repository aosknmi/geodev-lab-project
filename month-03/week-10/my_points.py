
import pandas as pd
import geopandas as gpd

# Read the CSV file
table = pd.read_csv("data/processed/oyo_state_health_facilities.csv")

# Display the first 3 rows
print(table.head(3))

# Convert the CSV into a GeoDataFrame
facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
)

# Display the first 3 rows of the GeoDataFrame
print(facilities.head(3))

# Display the CRS
print("CRS:", facilities.crs)

# Save as a GeoPackage
facilities.to_file(
    "data/processed/Health_Facilities_Oyo_State_UTM31.gpkg",
    layer="health_facilities",
    driver="GPKG"
)

print("Saved", len(facilities), "health facilities")