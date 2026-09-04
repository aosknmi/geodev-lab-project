# Health Access in Ibadan North Local Government Area

## Question

**Which wards in Ibadan North Local Government Area are located more than 5 km from a health facility?**

## Why It Matters

Access to healthcare is influenced by the geographic distance between communities and health facilities. Identifying wards located more than 5 km from a health facility can help reveal areas with potentially limited access to healthcare and provide useful information for healthcare planning and service improvement in Ibadan North LGA.

## Data Needed

- Ibadan North LGA boundary
- Ward boundaries
- Health facility locations
- Road network data for map context

## Data Sources

- **LGA and administrative boundaries:** [Humanitarian Data Exchange (HDX) – Nigeria Subnational Administrative Boundaries](https://data.humdata.org/dataset/cod-ab-nga)
- **Ward boundaries:** [GRID3 Nigeria – Geospatial Data](https://grid3.org/geospatial-data-nigeria)
- **Health facility locations:** [GRID3 Nigeria – Geospatial Data](https://grid3.org/geospatial-data-nigeria)
- **Road network data:**
  - [Humanitarian Data Exchange (HDX) – Nigeria Roads](https://data.humdata.org/dataset/nigeria-roads)
  - [GRID3 – Geospatial Data Nigeria](https://grid3.org/geospatial-data-nigeria)
  - **Alternative:** [QuickOSM](https://plugins.qgis.org/plugins/QuickOSM/) plugin for QGIS, which allows OpenStreetMap road data to be downloaded directly into QGIS using the Overpass API.

## What I Would Build

I will build a **GIS-based healthcare accessibility and coverage system for Ibadan North LGA**. The system will map existing health facilities and generate **5 km coverage zones** around them to identify wards and locations that fall outside the defined coverage areas. This will provide a clear visual representation of areas that may have limited access to healthcare facilities.

However, the project will go beyond creating a static map or performing a one-time spatial analysis. I aim to develop an **automated and interactive geospatial system** that can process new or updated health facility data and refresh the coverage analysis with minimal manual intervention.

Instead of manually updating facility locations, recreating buffers, and rerunning the analysis whenever new data becomes available, the system will be designed to automatically process new or modified health facility data, regenerate the 5 km coverage areas, identify underserved areas, and update the analysis results.

The system will ultimately function as a **GIS-based decision-support tool** that provides up-to-date information on healthcare facility coverage within Ibadan North LGA. Health planners, local government authorities, and other relevant stakeholders could use the system to monitor healthcare accessibility, identify underserved areas, assess the distribution of existing facilities, and support decisions about where additional healthcare facilities may be needed.

The goal is to transform the project from simply **“a GIS map showing healthcare coverage”** into a **scalable, automated geospatial system for monitoring and supporting healthcare accessibility**.