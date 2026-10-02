# Data Notes

## Oyo State Boundary

- **Source:** [Nigeria - Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-nga)
- **Publisher:** Humanitarian Data Exchange (HDX)
- **Downloaded/Extracted:** 09/09/2026
- **Study area:** Oyo State
- **Geometry type:** Polygon
- **Coverage:** Oyo State administrative boundary

## OSM Roads

- **Source:** [Humanitarian OpenStreetMap Team (HOTOSM) – Nigeria Roads](https://data.humdata.org/dataset/hotosm_nga_roads)
- **Dataset:** HOTOSM Nigeria Roads (OpenStreetMap Export)
- **Downloaded/Extracted:** 09/09/2026
- **Features:** 111,355
- **Geometry type:** Line
- **Coverage:** Looks complete for the study area, although there are a few small spaces/gaps
- **Columns:** `name`, `name_en`, `highway`, `surface`, `smoothness`, `width`, `lanes`, `oneway`, `bridge`, `layer`, `source`, `osm_id`, `osm_type`
- **Processing:** The Nigeria road dataset was clipped to the Oyo State boundary to retain only road features within the study area.
- **Road selection:** Major roads were identified from the `highway` classification attribute and used for the buffer analysis.

## Data Preparation and Coordinate System

- **CRS:** Source layers were initially obtained in EPSG:4326 (WGS 84 geographic coordinates).
- **STUDY AREA:** Oyo State was extracted from the [Humanitarian Data Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-nga) Nigeria Subnational Administrative Boundaries dataset.
- **CLIPPING:** The road and health facility layer was clipped to the Oyo State boundary to remove features outside the study area and maintain a consistent analysis extent.
- **REPROJECTION:** The clipped layers were reprojected to EPSG:32631 (WGS 84 / UTM Zone 31N), a projected coordinate reference system with units in metres.
- **PURPOSE OF REPROJECTION:** The projected CRS was used because the analysis involved distance-based operations such as buffering, where measurements in metres are more appropriate than geographic degrees.

- ## Data Quality Notes

### Oyo State Boundary — HDX Nigeria Subnational Administrative Boundaries
- **SOURCE:** Humanitarian Data Exchange (HDX) — [Nigeria Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-nga)
- **DATASET DATE:** 16 April 2026
- **COMPLETENESS:** Expected to cover the Oyo State administrative boundary. Check that the Oyo State polygon is present and complete.
- **CURRENCY:** Dataset dated 16 April 2026, making it sufficiently recent for defining the 2026 study area.
- **POSITIONAL ACCURACY:** Compare the boundary with a reliable reference dataset or satellite imagery to identify any spatial mismatch.
- **ATTRIBUTE ACCURACY:** Check that the state name and administrative codes correctly identify Oyo State.
- **FITNESS:** Suitable for defining the study area and clipping the health facility and road datasets to Oyo State. Not sufficient by itself for measuring healthcare accessibility.

### Health Facility Locations — GRID3 Nigeria
- **SOURCE:** GRID3 Nigeria — [Geospatial Data](https://grid3.org/geospatial-data-nigeria)
- **DATASET DATE:** August 2026
- **COMPLETENESS:** Check whether all relevant health facilities in Oyo State are included. Missing or recently established facilities could affect the nearest-facility analysis.
- **CURRENCY:** Dataset dated August 2026, providing relatively recent information on the health facility network.
- **POSITIONAL ACCURACY:** Check facility coordinates for obvious spatial errors, including facilities appearing outside their actual locations or outside Oyo State.
- **ATTRIBUTE ACCURACY:** Check facility names, types, ownership/status and other available attributes for missing, duplicated or incorrectly classified records.
- **FITNESS:** Suitable as the primary health facility point dataset for identifying the nearest facility to each community. Results depend on the completeness and accuracy of the facility locations.

### Road Network — HOTOSM Nigeria Roads
- **SOURCE:** Humanitarian OpenStreetMap Team (HOTOSM) — [Nigeria Roads](https://data.humdata.org/dataset/hotosm_nga_roads)
- **DATASET DATE:** April 2026
- **COMPLETENESS:** Check road coverage for missing roads, particularly smaller community and access roads that may affect accessibility analysis.
- **CURRENCY:** Dataset dated April 2026, providing a recent representation of the road network at the time of the analysis.
- **POSITIONAL ACCURACY:** Compare road alignment with recent satellite imagery or another reliable reference to identify significant spatial offsets.
- **ATTRIBUTE ACCURACY:** Check road classifications and other available attributes for missing or incorrect values, especially if the network will be used for travel-distance or travel-time analysis.
- **FITNESS:** Suitable for displaying road context and potentially supporting network-based accessibility analysis. For a simple straight-line 5 km analysis, roads are contextual rather than essential to the distance calculation.
