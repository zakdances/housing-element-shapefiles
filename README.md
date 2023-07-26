# Bounty Project for CA Yimby bounty
### A project to create shapefiles for all cities belonging to ABAG and SACOG. SCAG coming soon.

#### shapefile path: counties/{county name}/cities/{city name}/output/{document name}/misc


1. Generating a list of incorporated cities along with associated planning agency (SACOG, ABAG, etc), county, and download links to housing element PDFs.
2. Geojson parcel data from each county website along with cleanup, normalization, and transfer to my database.
3. Download each PDF, use machine learning to extract the data. Then do a second pass to clean up the (very messy) data. Generate metadata (page count, thumbnail, etc). Transfer all data to my database.
4. Created endpoints to query database from the UI.
5. Extra: Created web UI viewer using nextjs and react.

