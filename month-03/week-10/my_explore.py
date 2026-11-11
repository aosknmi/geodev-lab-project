
import geopandas as gpd

# List available layers in the GeoPackage
print(gpd.list_layers("data/processed/Health_Facilities_Oyo_State_UTM31.gpkg"))

# Read the health facilities layer
health_facilities = gpd.read_file(
    "data/processed/Health_Facilities_Oyo_State_UTM31.gpkg"
)

# Display the first five rows
print(health_facilities.head())

# Display number of rows and columns
print("Rows and columns:", health_facilities.shape)

# Display geometry types
print(health_facilities.geom_type.value_counts())

# Display Coordinate Reference System
print("CRS:", health_facilities.crs)

# Display dataset bounds
print("Bounds:", health_facilities.total_bounds)