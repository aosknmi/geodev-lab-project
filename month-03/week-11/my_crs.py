
import geopandas as gpd

# Read the datasets
oyo = gpd.read_file("data/processed/Oyo_State_Shp.gpkg")
facilities = gpd.read_file("data/processed/Health_Facilities_Oyo_State.gpkg")

# Print original CRS
print("Oyo State CRS:", oyo.crs)
print("Health Facilities CRS:", facilities.crs)

# Estimate the appropriate UTM CRS
utm_crs = oyo.estimate_utm_crs()
print("Suggested UTM CRS:", utm_crs)

# Reproject both datasets
oyo_utm = oyo.to_crs(utm_crs)
facilities_utm = facilities.to_crs(utm_crs)

# Calculate area in square kilometres
oyo_utm["area_km2"] = oyo_utm.area / 1_000_000

print("\nOyo State Area:")
print(oyo_utm[["area_km2"]])

print(
    "Total Oyo State Area:",
    round(oyo_utm["area_km2"].sum(), 2),
    "km2"
)