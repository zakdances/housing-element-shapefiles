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
👇 Columns explained 
* city - name of city
* documents - number of documents city has publicly available for download
* tables - number of tables found in the documents
* apns - number of APNs (assessor parcel numbers) found in the tables
* parcels - parcel data found for APNs. Ideally, this number should be very close to the previous column.
* agency - regional planning organization this city is a member of
* county - county the city resides in
* link - link to relevant folder in this repo. There you can find shapefiles and other output.
```
# ABAG
|   |  city  |documents|tables|apns|parcels|agency|county|                  link                   |
|--:|--------|--------:|-----:|----|------:|------|------|-----------------------------------------|
|  1|Petaluma|        2|     6|130 |     84|ABAG  |Sonoma|[link](<counties/Sonoma/cities/Petaluma>)|

# ABAG
|   |       city        |documents|tables|apns|parcels|agency|   county    |                         link                          |
|--:|-------------------|--------:|-----:|----|------:|------|-------------|-------------------------------------------------------|
|  1|Alameda            |        2|     6|50  |     40|ABAG  |Alameda      |[link](<counties/Alameda/cities/Alameda>)              |
|  2|Albany             |        2|    27|1063|    855|ABAG  |Alameda      |[link](<counties/Alameda/cities/Albany>)               |
|  3|American Canyon    |        2|     0|   0|      0|ABAG  |Napa         |[link](<counties/Napa/cities/American Canyon>)         |
|  4|Antioch            |        2|    10|638 |    520|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Antioch>)         |
|  5|Atherton           |        2|     0|   0|      0|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Atherton>)           |
|  6|Belmont            |        2|     2|16  |     10|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Belmont>)            |
|  7|Belvedere          |        1|     3|83  |     37|ABAG  |Marin        |[link](<counties/Marin/cities/Belvedere>)              |
|  8|Benicia            |        2|    38|877 |    763|ABAG  |Solano       |[link](<counties/Solano/cities/Benicia>)               |
|  9|Berkeley           |        3|     2|576 |      7|ABAG  |Alameda      |[link](<counties/Alameda/cities/Berkeley>)             |
| 10|Brentwood          |        2|    11|295 |    220|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Brentwood>)       |
| 11|Brisbane           |        4|    12|1240|   1160|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Brisbane>)           |
| 12|Burlingame         |        1|     2|140 |     69|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Burlingame>)         |
| 13|Calistoga          |        2|     5|52  |     44|ABAG  |Napa         |[link](<counties/Napa/cities/Calistoga>)               |
| 14|Campbell           |        3|    11|997 |    939|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Campbell>)         |
| 15|Clayton            |        2|     4|102 |     90|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Clayton>)         |
| 16|Cloverdale         |        2|     5|40  |     40|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Cloverdale>)            |
| 17|Colma              |        2|     2|145 |     72|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Colma>)              |
| 18|Concord            |        2|     4|1037|    495|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Concord>)         |
| 19|Corte Madera       |        3|     0|   0|      0|ABAG  |Marin        |[link](<counties/Marin/cities/Corte Madera>)           |
| 20|Cotati             |        2|     5|69  |     38|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Cotati>)                |
| 21|Cupertino          |        1|     0|   0|      0|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Cupertino>)        |
| 22|Daly City          |        1|     2|171 |    162|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Daly City>)          |
| 23|Danville           |        2|    59|435 |    401|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Danville>)        |
| 24|Dixon              |        2|     3|33  |     15|ABAG  |Solano       |[link](<counties/Solano/cities/Dixon>)                 |
| 25|Dublin             |        2|     1|82  |      2|ABAG  |Alameda      |[link](<counties/Alameda/cities/Dublin>)               |
| 26|East Palo Alto     |        2|    16|118 |     86|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/East Palo Alto>)     |
| 27|El Cerrito         |        2|     6|160 |    149|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/El Cerrito>)      |
| 28|Emeryville         |        2|     4|230 |     14|ABAG  |Alameda      |[link](<counties/Alameda/cities/Emeryville>)           |
| 29|Fairfax            |        1|     9|432 |    284|ABAG  |Marin        |[link](<counties/Marin/cities/Fairfax>)                |
| 30|Fairfield          |        2|    11|215 |     99|ABAG  |Solano       |[link](<counties/Solano/cities/Fairfield>)             |
| 31|Foster City        |        2|    11|95  |     81|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Foster City>)        |
| 32|Fremont            |        2|     3|574 |    614|ABAG  |Alameda      |[link](<counties/Alameda/cities/Fremont>)              |
| 33|Gilroy             |        2|     8|124 |     28|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Gilroy>)           |
| 34|Hayward            |        3|     0|348 |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/Hayward>)              |
| 35|Healdsburg         |        2|     2|21  |      2|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Healdsburg>)            |
| 36|Hercules           |        3|     0|5   |      0|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Hercules>)        |
| 37|Hillsborough       |        2|     5|109 |     43|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Hillsborough>)       |
| 38|Lafayette          |        2|    22|708 |    416|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Lafayette>)       |
| 39|Larkspur           |        1|     3|80  |     37|ABAG  |Marin        |[link](<counties/Marin/cities/Larkspur>)               |
| 40|Livermore          |        3|     2|292 |      2|ABAG  |Alameda      |[link](<counties/Alameda/cities/Livermore>)            |
| 41|Los Altos          |        2|     7|589 |    532|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Altos>)        |
| 42|Los Altos Hills    |        3|     5|295 |     72|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Altos Hills>)  |
| 43|Los Gatos          |        3|    11|551 |    528|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Gatos>)        |
| 44|Menlo Park         |        2|   190|1088|    662|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Menlo Park>)         |
| 45|Mill Valley        |        1|     3|257 |    244|ABAG  |Marin        |[link](<counties/Marin/cities/Mill Valley>)            |
| 46|Millbrae           |        2|    14|318 |    224|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Millbrae>)           |
| 47|Milpitas           |        2|     0|   0|      0|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Milpitas>)         |
| 48|Monte Sereno       |        2|     2|280 |    116|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Monte Sereno>)     |
| 49|Moraga             |        3|     6|169 |     74|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Moraga>)          |
| 50|Morgan Hill        |        2|     1|118 |      8|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Morgan Hill>)      |
| 51|Mountain View      |        3|     8|688 |    625|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Mountain View>)    |
| 52|Napa               |        1|     0|   0|      0|ABAG  |Napa         |[link](<counties/Napa/cities/Napa>)                    |
| 53|Newark             |        1|     2|12  |      5|ABAG  |Alameda      |[link](<counties/Alameda/cities/Newark>)               |
| 54|Novato             |        1|     4|44  |     25|ABAG  |Marin        |[link](<counties/Marin/cities/Novato>)                 |
| 55|Oakland            |        2|     5|4185|     41|ABAG  |Alameda      |[link](<counties/Alameda/cities/Oakland>)              |
| 56|Oakley             |        4|    29|596 |    474|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Oakley>)          |
| 57|Orinda             |        3|    20|1784|   1745|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Orinda>)          |
| 58|Pacifica           |        1|     2|49  |     45|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Pacifica>)           |
| 59|Palo Alto          |        1|    13|447 |    420|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Palo Alto>)        |
| 60|Petaluma           |        2|     6|130 |     84|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Petaluma>)              |
| 61|Piedmont           |        2|     1|289 |      2|ABAG  |Alameda      |[link](<counties/Alameda/cities/Piedmont>)             |
| 62|Pinole             |        2|    15|144 |    138|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pinole>)          |
| 63|Pittsburg          |        1|     2|124 |    120|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pittsburg>)       |
| 64|Pleasant Hill      |        1|     1|154 |     31|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pleasant Hill>)   |
| 65|Pleasanton         |        2|     2|839 |      4|ABAG  |Alameda      |[link](<counties/Alameda/cities/Pleasanton>)           |
| 66|Portola Valley     |        1|     2|27  |      2|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Portola Valley>)     |
| 67|Redwood City       |        2|     3|176 |     87|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Redwood City>)       |
| 68|Richmond           |        2|     5|383 |    321|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Richmond>)        |
| 69|Rio Vista          |        2|     6|160 |    154|ABAG  |Solano       |[link](<counties/Solano/cities/Rio Vista>)             |
| 70|Rohnert Park       |        2|     5|93  |     71|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Rohnert Park>)          |
| 71|Ross               |        1|     3|40  |     38|ABAG  |Marin        |[link](<counties/Marin/cities/Ross>)                   |
| 81|San Anselmo        |        1|     1|418 |    217|ABAG  |Marin        |[link](<counties/Marin/cities/San Anselmo>)            |
| 72|San Bruno          |        2|     4|116 |    105|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Bruno>)          |
| 73|San Carlos         |        2|     4|995 |    905|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Carlos>)         |
| 74|San Francisco      |        4|     1|174 |    143|ABAG  |San Francisco|[link](<counties/San Francisco/cities/San Francisco>)  |
| 75|San Jose           |        1|     3|231 |    123|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/San Jose>)         |
| 76|San Leandro        |        2|     0|99  |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/San Leandro>)          |
| 77|San Mateo          |        2|     7|577 |    359|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Mateo>)          |
| 78|San Pablo          |        1|     4|195 |    191|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/San Pablo>)       |
| 79|San Rafael         |        2|     3|392 |    125|ABAG  |Marin        |[link](<counties/Marin/cities/San Rafael>)             |
| 80|San Ramon          |        3|     2|195 |     12|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/San Ramon>)       |
| 82|Santa Clara        |        2|     6|157 |    146|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Santa Clara>)      |
| 83|Santa Rosa         |        2|    10|2748|   2714|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Santa Rosa>)            |
| 84|Saratoga           |        2|    24|896 |    655|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Saratoga>)         |
| 85|Sausalito          |        2|     9|2477|   2407|ABAG  |Marin        |[link](<counties/Marin/cities/Sausalito>)              |
| 86|Sebastopol         |        2|     7|154 |    148|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Sebastopol>)            |
| 87|Sonoma             |        2|     1|20  |      1|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Sonoma>)                |
| 88|South San Francisco|        2|     9|363 |    334|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/South San Francisco>)|
| 89|Suisun City        |        2|     3|73  |     65|ABAG  |Solano       |[link](<counties/Solano/cities/Suisun City>)           |
| 90|Sunnyvale          |        1|     6|232 |    188|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Sunnyvale>)        |
| 91|Tiburon            |        2|     4|127 |    126|ABAG  |Marin        |[link](<counties/Marin/cities/Tiburon>)                |
| 92|Union City         |        2|     7|166 |    190|ABAG  |Alameda      |[link](<counties/Alameda/cities/Union City>)           |
| 93|Vacaville          |        2|     6|804 |    424|ABAG  |Solano       |[link](<counties/Solano/cities/Vacaville>)             |
| 94|Walnut Creek       |        4|    14|2810|   2061|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Walnut Creek>)    |
| 95|Windsor            |        2|     8|159 |    136|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Windsor>)               |
| 96|Woodside           |        2|     0|724 |      0|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Woodside>)           |
| 97|Yountville         |        2|     3|21  |     18|ABAG  |Napa         |[link](<counties/Napa/cities/Yountville>)              |

# SACOG
|   |     city      |documents|tables|apns|parcels|agency|  county  |                       link                        |
|--:|---------------|--------:|-----:|----|------:|------|----------|---------------------------------------------------|
|  1|Auburn         |        3|     4|788 |    772|SACOG |Placer    |[link](<counties/Placer/cities/Auburn>)            |
|  2|Citrus Heights |        3|     8|162 |    128|SACOG |Sacramento|[link](<counties/Sacramento/cities/Citrus Heights>)|
|  3|Colfax         |        2|     3|58  |     56|SACOG |Placer    |[link](<counties/Placer/cities/Colfax>)            |
|  4|Davis          |        3|    16|267 |    255|SACOG |Yolo      |[link](<counties/Yolo/cities/Davis>)               |
|  5|Elk Grove      |        4|    30|775 |    459|SACOG |Sacramento|[link](<counties/Sacramento/cities/Elk Grove>)     |
|  6|Folsom         |        3|    22|997 |    764|SACOG |Sacramento|[link](<counties/Sacramento/cities/Folsom>)        |
|  7|Galt           |        4|    18|844 |    260|SACOG |Sacramento|[link](<counties/Sacramento/cities/Galt>)          |
|  8|Isleton        |        3|     2|18  |     18|SACOG |Sacramento|[link](<counties/Sacramento/cities/Isleton>)       |
|  9|Lincoln        |        2|     3|51  |     51|SACOG |Placer    |[link](<counties/Placer/cities/Lincoln>)           |
| 10|Live Oak       |        2|     2|656 |    340|SACOG |Sutter    |[link](<counties/Sutter/cities/Live Oak>)          |
| 11|Loomis         |        2|     2|122 |    114|SACOG |Placer    |[link](<counties/Placer/cities/Loomis>)            |
| 12|Marysville     |        3|     9|522 |    522|SACOG |Yuba      |[link](<counties/Yuba/cities/Marysville>)          |
| 13|Placerville    |        4|     5|122 |      5|SACOG |El Dorado |[link](<counties/El Dorado/cities/Placerville>)    |
| 14|Rancho Cordova |        3|     6|157 |    145|SACOG |Sacramento|[link](<counties/Sacramento/cities/Rancho Cordova>)|
| 15|Rocklin        |        3|     6|525 |    500|SACOG |Placer    |[link](<counties/Placer/cities/Rocklin>)           |
| 16|Roseville      |        3|     3|649 |    502|SACOG |Placer    |[link](<counties/Placer/cities/Roseville>)         |
| 17|Sacramento     |        3|     5|5836|   5660|SACOG |Sacramento|[link](<counties/Sacramento/cities/Sacramento>)    |
| 18|West Sacramento|        4|     7|642 |    324|SACOG |Yolo      |[link](<counties/Yolo/cities/West Sacramento>)     |
| 19|Wheatland      |        2|     1|108 |      1|SACOG |Yuba      |[link](<counties/Yuba/cities/Wheatland>)           |
| 20|Winters        |        3|     7|666 |    342|SACOG |Yolo      |[link](<counties/Yolo/cities/Winters>)             |
| 21|Woodland       |        5|     8|727 |    660|SACOG |Yolo      |[link](<counties/Yolo/cities/Woodland>)            |
| 22|Yuba City      |        2|    10|505 |    351|SACOG |Sutter    |[link](<counties/Sutter/cities/Yuba City>)         |

# ABAG
|   |  city  |documents|tables|apns|parcels|agency|county|                  link                   |
|--:|--------|--------:|-----:|----|------:|------|------|-----------------------------------------|
|  1|Petaluma|        2|     6|130 |     84|ABAG  |Sonoma|[link](<counties/Sonoma/cities/Petaluma>)|

# SCAG (Orange County)
|   |       city        |documents|tables|apns |parcels|agency|county|                        link                        |
|--:|-------------------|--------:|-----:|-----|------:|------|------|----------------------------------------------------|
|  1|Aliso Viejo        |        2|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Aliso Viejo>)        |
|  2|Anaheim            |        3|    11|1140 |    905|SCAG  |Orange|[link](<counties/Orange/cities/Anaheim>)            |
|  3|Brea               |        4|     9|335  |    312|SCAG  |Orange|[link](<counties/Orange/cities/Brea>)               |
|  4|Buena Park         |        3|     6|2122 |   2081|SCAG  |Orange|[link](<counties/Orange/cities/Buena Park>)         |
|  5|Costa Mesa         |        4|    15|67   |     48|SCAG  |Orange|[link](<counties/Orange/cities/Costa Mesa>)         |
|  6|Cypress            |        3|     5|828  |    607|SCAG  |Orange|[link](<counties/Orange/cities/Cypress>)            |
|  7|Dana Point         |        5|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Dana Point>)         |
|  8|Fountain Valley    |        3|     0|2    |      0|SCAG  |Orange|[link](<counties/Orange/cities/Fountain Valley>)    |
|  9|Fullerton          |        1|     1|510  |    476|SCAG  |Orange|[link](<counties/Orange/cities/Fullerton>)          |
| 10|Garden Grove       |        3|     6|1183 |   1176|SCAG  |Orange|[link](<counties/Orange/cities/Garden Grove>)       |
| 11|Irvine             |        4|    17|23764|   9549|SCAG  |Orange|[link](<counties/Orange/cities/Irvine>)             |
| 12|La Habra           |        5|     1|68   |     29|SCAG  |Orange|[link](<counties/Orange/cities/La Habra>)           |
| 13|La Palma           |        3|     3|136  |    132|SCAG  |Orange|[link](<counties/Orange/cities/La Palma>)           |
| 14|Laguna Beach       |        4|     6|82   |     60|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Beach>)       |
| 15|Laguna Hills       |        4|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Hills>)       |
| 16|Laguna Niguel      |        2|     1|9    |      4|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Niguel>)      |
| 17|Laguna Woods       |        4|     4|173  |     60|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Woods>)       |
| 18|Lake Forest        |        4|     6|1621 |    734|SCAG  |Orange|[link](<counties/Orange/cities/Lake Forest>)        |
| 19|Los Alamitos       |        4|     8|434  |    362|SCAG  |Orange|[link](<counties/Orange/cities/Los Alamitos>)       |
| 20|Mission Viejo      |        1|     1|24   |     17|SCAG  |Orange|[link](<counties/Orange/cities/Mission Viejo>)      |
| 21|Newport Beach      |        5|     4|12   |      4|SCAG  |Orange|[link](<counties/Orange/cities/Newport Beach>)      |
| 22|Orange             |        4|     6|137  |     61|SCAG  |Orange|[link](<counties/Orange/cities/Orange>)             |
| 23|Placentia          |        2|     2|589  |    566|SCAG  |Orange|[link](<counties/Orange/cities/Placentia>)          |
| 24|San Clemente       |        4|     4|220  |    216|SCAG  |Orange|[link](<counties/Orange/cities/San Clemente>)       |
| 25|San Juan Capistrano|        3|     9|397  |    283|SCAG  |Orange|[link](<counties/Orange/cities/San Juan Capistrano>)|
| 26|Santa Ana          |        3|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Santa Ana>)          |
| 27|Seal Beach         |        2|     3|422  |    333|SCAG  |Orange|[link](<counties/Orange/cities/Seal Beach>)         |
| 28|Stanton            |        3|    13|806  |    510|SCAG  |Orange|[link](<counties/Orange/cities/Stanton>)            |
| 29|Tustin             |        5|     7|399  |    192|SCAG  |Orange|[link](<counties/Orange/cities/Tustin>)             |
| 30|Villa Park         |        5|     4|13   |     12|SCAG  |Orange|[link](<counties/Orange/cities/Villa Park>)         |
| 31|Westminster        |        4|     7|5293 |   2969|SCAG  |Orange|[link](<counties/Orange/cities/Westminster>)        |
| 32|Yorba Linda        |        3|     5|617  |    355|SCAG  |Orange|[link](<counties/Orange/cities/Yorba Linda>)        |

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     2|479 |    465|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     2|479 |    465|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     2|479 |    465|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     2|479 |    465|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     3|479 |    479|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     3|479 |    479|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     3|479 |    479|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     3|479 |    479|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     2|479 |    465|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     2|479 |    465|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        1|     2|479 |    465|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

# SCAG
|   | city  |documents|tables|apns|parcels|agency|  county   |                    link                     |
|--:|-------|--------:|-----:|----|------:|------|-----------|---------------------------------------------|
|  1|Arcadia|        5|    10|3271|   3234|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)|

