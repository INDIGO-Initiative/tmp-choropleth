# tmp-choropleth


## Updating GEOJSON

Install QGIS

Go to https://data.humdata.org/dataset/international-boundaries-intl-adm0

Download adm0_polygons.shp

Extract all files in zip to same dir

Open QGIS

Layer -> Add Layer -> Add Vector Layer. select .shp file

Vector menu -> Geometry tools -> Simplify.
Tolerance 1
Simplified - Save as a new file on disk
Open after - uncheck


Layer -> Add Layer -> Add Vector Layer. select NEW .shp file

Right click layer - save as GeoJSON

