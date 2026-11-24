import geopandas as gpd
import rasterio
from rasterio.mask import mask
import pandas as pd

# Open boundary layer
boundaries = gpd.read_file("data/processed/wards.gpkg")

# Calculate mean NDVI per polygon
mean_ndvi = []

with rasterio.open("data/processed/ndvi.tif") as src:
    boundaries = boundaries.to_crs(src.crs)

    for geometry in boundaries.geometry:
        out_image, out_transform = mask(
            src,
            [geometry],
            crop=True,
            nodata=-9999
        )

        # Extract mean NDVI values
        data = out_image[0]
        valid_pixels = data[data != -9999]

        mean = valid_pixels.mean() if len(valid_pixels) > 0 else None
        mean_ndvi.append(mean)

# Add results to boundary table
boundaries["mean_ndvi"] = mean_ndvi

# Save results as CSV
boundaries.drop(columns="geometry").to_csv(
    "month-03/week-12/my_zonal.csv",
    index=False
)

print("Zonal statistics completed!")
print("Mean NDVI per polygon saved to month-03/week-12/my_zonal.csv")