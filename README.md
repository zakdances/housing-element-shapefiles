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

# SACOG
```
+------------------------------------------------------------------------+
|  |      city     |documents|tables|apns|server intersection apns|agency|
+--+---------------+---------+------+----+------------------------+------+
| 1|     Auburn    |    3    |   4  | 788|           772          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 2| Citrus Heights|    3    |  11  | 162|           128          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 3|     Colfax    |    2    |   3  | 58 |           56           | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 4|     Davis     |    3    |  17  | 267|           255          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 5|   Elk Grove   |    4    |  30  | 775|          1810          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 6|     Folsom    |    3    |  26  | 997|           778          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 7|      Galt     |    4    |  18  | 844|           320          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 8|    Isleton    |    3    |   2  | 18 |           18           | SACOG|
+--+---------------+---------+------+----+------------------------+------+
| 9|    Lincoln    |    2    |   3  | 51 |           51           | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|10|    Live Oak   |    2    |   2  | 656|           340          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|11|     Loomis    |    2    |   2  | 122|           114          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|12|   Marysville  |    3    |   9  | 522|           522          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|13|  Placerville  |    4    |  10  | 122|            1           | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|14| Rancho Cordova|    3    |   6  | 157|          1473          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|15|    Rocklin    |    3    |   6  | 525|           500          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|16|   Roseville   |    3    |   3  | 649|           502          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|17|   Sacramento  |    3    |   5  |5836|          5848          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|18|West Sacramento|    4    |   7  | 642|           324          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|19|   Wheatland   |    2    |   2  | 108|           106          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|20|    Winters    |    3    |   7  | 666|           360          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|21|    Woodland   |    5    |  11  | 727|           660          | SACOG|
+--+---------------+---------+------+----+------------------------+------+
|22|   Yuba City   |    2    |  11  | 505|           351          | SACOG|
+------------------------------------------------------------------------+```
