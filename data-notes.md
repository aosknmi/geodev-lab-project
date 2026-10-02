# Data Notes

## Oyo State Boundary

- **Source:** [Nigeria - Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-nga)
- **Publisher:** Humanitarian Data Exchange (HDX)
- **Downloaded:** 09/09/2026
- **Study area:** Oyo State
- **Geometry type:** Polygon
- **Coverage:** Oyo State administrative boundary

## OSM Roads

- **Source:** [Humanitarian OpenStreetMap Team (HOTOSM) – Nigeria Roads](https://data.humdata.org/dataset/hotosm_nga_roads)
- **Dataset:** HOTOSM Nigeria Roads (OpenStreetMap Export)
- **Downloaded:** 09/09/2026
- **Features:** 111,355
- **Geometry type:** Line
- **Coverage:** Looks complete for the study area, although there are a few small spaces/gaps
- **Columns:** `name`, `name_en`, `highway`, `surface`, `smoothness`, `width`, `lanes`, `oneway`, `bridge`, `layer`, `source`, `osm_id`, `osm_type`
- **Processing:** The Nigeria road dataset was clipped to the Oyo State boundary to retain only road features within the study area.
- **Road selection:** Major roads were identified from the `highway` classification attribute and used for the buffer analysis.

## Data Preparation and Coordinate System

- **CRS:** Source layers were initially obtained in EPSG:4326 (WGS 84 geographic coordinates).
- **STUDY AREA:** Oyo State was extracted from the [Humanitarian Data Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-nga) Nigeria Subnational Administrative Boundaries dataset.
- **CLIPPING:** The road layer was clipped to the Oyo State boundary to remove features outside the study area and maintain a consistent analysis extent.
- **REPROJECTION:** The clipped layers were reprojected to EPSG:32631 (WGS 84 / UTM Zone 31N), a projected coordinate reference system with units in metres.
- **PURPOSE OF REPROJECTION:** The projected CRS was used because the analysis involved distance-based operations such as buffering, where measurements in metres are more appropriate than geographic degrees.