# Bounty Project for CA Yimby bounty
### A project to create shapefiles for all cities belonging to ABAG, SACOG and SCAG.

#### (shapefile path: counties/{county name}/cities/{city name}/output/{document name}/misc)

## How this project was created:
1. I generated a list of incorporated cities along with associated planning agency (SACOG, ABAG, etc), county, and downloaded links to housing element PDFs.
2. Geojson parcel data from each county website along with cleanup, normalization, and transfer to my database.
3. Download each PDF, use machine learning to extract the data. Then do a second pass to clean up the (very messy) data. Generate metadata (page count, thumbnail, etc). Transfer all data to my database.
4. Created endpoints to query database from the UI.
5. Extra: Created web UI viewer using nextjs and react.

## Results

```
Columns
* city - name of city
* documents - number of documents city has publicly available for download
* tables - number of tables found in the documents
* apns - number of APNs (assessor parcel numbers) found in the tables
* parcels - parcel data found for APNs. Ideally, this number should be very close to the previous column.
* agency - regional planning organization this city is a member of
* county - county the city resides in
* link - link to relevant folder in this repo. There you can find shapefiles and other output.
```


# SACOG
|   |     city      |documents|tables|apns|parcels|agency|  county  |                       link                        |
|--:|---------------|--------:|-----:|----|------:|------|----------|---------------------------------------------------|
|  1|Auburn         |        3|     4|788 |    785|SACOG |Placer    |[link](<counties/Placer/cities/Auburn>)            |
|  2|Citrus Heights |        3|    11|162 |    118|SACOG |Sacramento|[link](<counties/Sacramento/cities/Citrus Heights>)|
|  3|Colfax         |        2|     3|58  |     62|SACOG |Placer    |[link](<counties/Placer/cities/Colfax>)            |
|  4|Davis          |        3|    17|267 |    252|SACOG |Yolo      |[link](<counties/Yolo/cities/Davis>)               |
|  5|Elk Grove      |        4|    30|775 |   1809|SACOG |Sacramento|[link](<counties/Sacramento/cities/Elk Grove>)     |
|  6|Folsom         |        3|    26|997 |    787|SACOG |Sacramento|[link](<counties/Sacramento/cities/Folsom>)        |
|  7|Galt           |        4|    18|844 |    306|SACOG |Sacramento|[link](<counties/Sacramento/cities/Galt>)          |
|  8|Isleton        |        3|     2|18  |     18|SACOG |Sacramento|[link](<counties/Sacramento/cities/Isleton>)       |
|  9|Lincoln        |        2|     3|51  |     51|SACOG |Placer    |[link](<counties/Placer/cities/Lincoln>)           |
| 10|Live Oak       |        2|     2|656 |    340|SACOG |Sutter    |[link](<counties/Sutter/cities/Live Oak>)          |
| 11|Loomis         |        2|     2|122 |    114|SACOG |Placer    |[link](<counties/Placer/cities/Loomis>)            |
| 12|Marysville     |        3|     9|522 |    522|SACOG |Yuba      |[link](<counties/Yuba/cities/Marysville>)          |
| 13|Placerville    |        4|    10|122 |      1|SACOG |El Dorado |[link](<counties/El Dorado/cities/Placerville>)    |
| 14|Rancho Cordova |        3|     6|157 |   1476|SACOG |Sacramento|[link](<counties/Sacramento/cities/Rancho Cordova>)|
| 15|Rocklin        |        3|     6|525 |    472|SACOG |Placer    |[link](<counties/Placer/cities/Rocklin>)           |
| 16|Roseville      |        3|     3|649 |    515|SACOG |Placer    |[link](<counties/Placer/cities/Roseville>)         |
| 17|Sacramento     |        3|     5|5836|   5887|SACOG |Sacramento|[link](<counties/Sacramento/cities/Sacramento>)    |
| 18|West Sacramento|        4|     7|642 |    303|SACOG |Yolo      |[link](<counties/Yolo/cities/West Sacramento>)     |
| 19|Wheatland      |        2|     2|108 |    109|SACOG |Yuba      |[link](<counties/Yuba/cities/Wheatland>)           |
| 20|Winters        |        3|     7|666 |    349|SACOG |Yolo      |[link](<counties/Yolo/cities/Winters>)             |
| 21|Woodland       |        5|    11|727 |    662|SACOG |Yolo      |[link](<counties/Yolo/cities/Woodland>)            |
| 22|Yuba City      |        2|    11|505 |    351|SACOG |Sutter    |[link](<counties/Sutter/cities/Yuba City>)         |

