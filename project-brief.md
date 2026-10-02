# Health Access in Oyo State

## Question

**Which communities in Oyo State are located more than 5 km from the nearest health facility?**

## Why It Matters

Access to healthcare is influenced by the geographic distance between communities and health facilities. Identifying communities located more than 5 km from the nearest health facility can help reveal communities with potentially limited access to healthcare and provide useful information for healthcare planning and service improvement across Oyo State.

## Data Needed

- Oyo State boundary
- Health facility locations
- Road network data for map context

## Data Sources

- **State and administrative boundaries:** [Nigeria - Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-nga) — Humanitarian Data Exchange (HDX)
- **Health facility locations:** [GRID3 Nigeria – Geospatial Data](https://grid3.org/geospatial-data-nigeria)
- **Road network data:**
  - [HOTOSM – Nigeria Roads](https://data.humdata.org/dataset/hotosm_nga_roads)
  - [GRID3 – Geospatial Data Nigeria](https://grid3.org/geospatial-data-nigeria)
  - **Alternative:** [QuickOSM](https://plugins.qgis.org/plugins/QuickOSM/) plugin for QGIS, which allows OpenStreetMap road data to be downloaded directly into QGIS using the Overpass API.

## What I Would Build

I will build a **GIS-based healthcare accessibility and coverage system for Oyo State**. The system will map existing health facilities and determine the **nearest health facility to each community**. The distance from each community to its nearest health facility will then be calculated to identify communities located more than **5 km from their nearest health facility**.

However, the project will go beyond creating a static map or performing a one-time spatial analysis. I aim to develop an **automated and interactive geospatial system** that can process new or updated community and health facility data and refresh the accessibility analysis with minimal manual intervention.

Instead of manually updating facility locations, calculating distances, and rerunning the analysis whenever new data becomes available, the system will be designed to automatically process new or modified health facility and community data, determine the nearest health facility for each community, calculate the corresponding distance, identify communities beyond the 5 km threshold, and update the analysis results.

The system will ultimately function as a **GIS-based decision-support tool** that provides up-to-date information on healthcare accessibility across Oyo State. Health planners, local government authorities, and other relevant stakeholders could use the system to monitor healthcare accessibility, identify communities located far from health facilities, assess the distribution of existing facilities, and support decisions about where additional healthcare facilities may be needed.

The goal is to transform the project from simply **“a GIS map showing healthcare coverage”** into a **scalable, automated geospatial system for monitoring and supporting healthcare accessibility across Oyo State**.