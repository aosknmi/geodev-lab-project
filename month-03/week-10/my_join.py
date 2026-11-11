
import pandas as pd
import geopandas as gpd

# Read the health facilities GeoPackage
facilities = gpd.read_file(
    "data/processed/Health_Facilities_Oyo_State_UTM31.gpkg"
)

# Read the health facilities CSV
table = pd.read_csv("data/processed/oyo_state_health_facilities.csv")

# Check the first few records
print(facilities.head())
print(table.head())

# First attempt: Merge using unique_id
first_try = facilities.merge(
    table,
    on="unique_id",
    how="left",
    suffixes=("_gpkg", "_csv")
)

matched = first_try["unique_id"].notna().sum()
print("Matched on first try:", matched, "of", len(facilities))


# Function to clean names
def clean_name(name):
    return str(name).strip().upper().replace(".", " ")


# Clean facility names in both datasets
facilities["join_key"] = facilities["facility_n"].apply(clean_name)
table["join_key"] = table["facility_n"].apply(clean_name)

# Merge using the cleaned facility names
joined = facilities.merge(
    table,
    on="join_key",
    how="left",
    suffixes=("_gpkg", "_csv")
)

# Count matched records
matched = joined["facility_n_gpkg"].notna().sum()

print("Matched after cleaning:", matched, "of", len(facilities))

# Display matched facility names
print(joined[["facility_n_gpkg", "join_key"]])