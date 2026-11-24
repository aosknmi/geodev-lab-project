import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

# Open Landsat Band 4 (Red)
with rasterio.open("data/raw/landsat/LC09_L2SP_191055_20260115_20260117_02_T1_SR_B4.tif") as red_src:
    red = red_src.read(1).astype("float32")
    profile = red_src.profile.copy()
    nodata = red_src.nodata

# Open Landsat Band 5 (NIR)
with rasterio.open("data/raw/landsat/LC09_L2SP_191055_20260115_20260117_02_T1_SR_B5.tif") as nir_src:
    nir = nir_src.read(1).astype("float32")
    nir_nodata = nir_src.nodata

# Calculate NDVI
denominator = nir + red

ndvi = np.full(red.shape, -9999, dtype="float32")

valid = np.isfinite(red) & np.isfinite(nir)

if nodata is not None:
    valid &= (red != nodata)

if nir_nodata is not None:
    valid &= (nir != nir_nodata)

valid &= denominator != 0

ndvi[valid] = (
    (nir[valid] - red[valid]) /
    denominator[valid]
)

# Print statistics
print("NDVI minimum:", np.min(ndvi[valid]))
print("NDVI maximum:", np.max(ndvi[valid]))
print("NDVI mean:", np.mean(ndvi[valid]))

# Plot NDVI map
plt.figure(figsize=(10, 8))
plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar(label="NDVI")
plt.title("NDVI Map")
plt.axis("off")

# Create output directory
os.makedirs("data/processed", exist_ok=True)

# Save map
plt.savefig("month-03/week-12/my_map.png", dpi=300, bbox_inches="tight")

plt.show()

print("NDVI calculation completed!")
print("Map saved as month-03/week-12/my_map.png")