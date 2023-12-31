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

# ABAG
|   |       city        |documents|tables|apns|parcels|agency|   county    |                         link                          |
|--:|-------------------|--------:|-----:|----|------:|------|-------------|-------------------------------------------------------|
|  1|Alameda            |        2|     7|50  |     39|ABAG  |Alameda      |[link](<counties/Alameda/cities/Alameda>)              |
|  2|Albany             |        2|    62|1063|   1502|ABAG  |Alameda      |[link](<counties/Alameda/cities/Albany>)               |
|  3|American Canyon    |        2|     0|   0|      0|ABAG  |Napa         |[link](<counties/Napa/cities/American Canyon>)         |
|  4|Antioch            |        2|    13|638 |    517|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Antioch>)         |
|  5|Atherton           |        2|     0|   0|      0|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Atherton>)           |
|  6|Belmont            |        2|     2|16  |     10|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Belmont>)            |
|  7|Belvedere          |        1|     8|83  |     79|ABAG  |Marin        |[link](<counties/Marin/cities/Belvedere>)              |
|  8|Benicia            |        2|    42|877 |    756|ABAG  |Solano       |[link](<counties/Solano/cities/Benicia>)               |
|  9|Berkeley           |        3|     3|576 |     16|ABAG  |Alameda      |[link](<counties/Alameda/cities/Berkeley>)             |
| 10|Brentwood          |        2|    11|295 |    197|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Brentwood>)       |
| 11|Brisbane           |        4|    12|1240|   1156|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Brisbane>)           |
| 12|Burlingame         |        1|     4|140 |    258|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Burlingame>)         |
| 13|Calistoga          |        2|     5|52  |     52|ABAG  |Napa         |[link](<counties/Napa/cities/Calistoga>)               |
| 14|Campbell           |        3|    14|997 |    968|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Campbell>)         |
| 15|Clayton            |        2|     4|102 |    111|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Clayton>)         |
| 16|Cloverdale         |        2|     5|40  |    391|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Cloverdale>)            |
| 17|Colma              |        2|     2|145 |    109|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Colma>)              |
| 18|Concord            |        2|     6|1037|    440|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Concord>)         |
| 19|Corte Madera       |        3|     0|   0|      0|ABAG  |Marin        |[link](<counties/Marin/cities/Corte Madera>)           |
| 20|Cotati             |        2|     6|69  |    169|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Cotati>)                |
| 21|Cupertino          |        1|     0|   0|      0|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Cupertino>)        |
| 22|Daly City          |        1|     2|171 |    162|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Daly City>)          |
| 23|Danville           |        2|    61|435 |    768|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Danville>)        |
| 24|Dixon              |        2|     6|33  |     24|ABAG  |Solano       |[link](<counties/Solano/cities/Dixon>)                 |
| 25|Dublin             |        2|     9|82  |    130|ABAG  |Alameda      |[link](<counties/Alameda/cities/Dublin>)               |
| 26|East Palo Alto     |        2|    19|118 |    307|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/East Palo Alto>)     |
| 27|El Cerrito         |        2|     6|160 |    149|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/El Cerrito>)      |
| 28|Emeryville         |        2|    16|230 |      6|ABAG  |Alameda      |[link](<counties/Alameda/cities/Emeryville>)           |
| 29|Fairfax            |        1|    10|432 |    181|ABAG  |Marin        |[link](<counties/Marin/cities/Fairfax>)                |
| 30|Fairfield          |        2|    14|215 |    503|ABAG  |Solano       |[link](<counties/Solano/cities/Fairfield>)             |
| 31|Foster City        |        2|    13|95  |     81|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Foster City>)        |
| 32|Fremont            |        2|     6|574 |    723|ABAG  |Alameda      |[link](<counties/Alameda/cities/Fremont>)              |
| 33|Gilroy             |        2|    33|124 |     72|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Gilroy>)           |
| 34|Hayward            |        3|    14|348 |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/Hayward>)              |
| 35|Healdsburg         |        2|     3|21  |      2|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Healdsburg>)            |
| 36|Hercules           |        3|     5|5   |      0|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Hercules>)        |
| 37|Hillsborough       |        2|     7|109 |     46|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Hillsborough>)       |
| 38|Lafayette          |        2|    27|708 |    416|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Lafayette>)       |
| 39|Larkspur           |        1|     4|80  |     74|ABAG  |Marin        |[link](<counties/Marin/cities/Larkspur>)               |
| 40|Livermore          |        3|     7|292 |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/Livermore>)            |
| 41|Los Altos          |        2|     7|589 |    550|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Altos>)        |
| 42|Los Altos Hills    |        3|    23|295 |    190|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Altos Hills>)  |
| 43|Los Gatos          |        3|    11|551 |    519|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Gatos>)        |
| 44|Menlo Park         |        2|   214|1088|    633|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Menlo Park>)         |
| 45|Mill Valley        |        1|     3|257 |    263|ABAG  |Marin        |[link](<counties/Marin/cities/Mill Valley>)            |
| 46|Millbrae           |        2|    14|318 |    128|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Millbrae>)           |
| 47|Milpitas           |        2|     0|   0|      0|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Milpitas>)         |
| 48|Monte Sereno       |        2|     2|280 |    371|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Monte Sereno>)     |
| 49|Moraga             |        3|     9|169 |   2027|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Moraga>)          |
| 50|Morgan Hill        |        2|     6|118 |    780|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Morgan Hill>)      |
| 51|Mountain View      |        3|    11|688 |    639|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Mountain View>)    |
| 52|Napa               |        1|     0|   0|      0|ABAG  |Napa         |[link](<counties/Napa/cities/Napa>)                    |
| 53|Newark             |        1|     3|12  |      2|ABAG  |Alameda      |[link](<counties/Alameda/cities/Newark>)               |
| 54|Novato             |        1|     4|44  |     20|ABAG  |Marin        |[link](<counties/Marin/cities/Novato>)                 |
| 55|Oakland            |        2|    11|4185|    431|ABAG  |Alameda      |[link](<counties/Alameda/cities/Oakland>)              |
| 56|Oakley             |        4|    31|596 |    566|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Oakley>)          |
| 57|Orinda             |        3|    21|1784|   1808|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Orinda>)          |
| 58|Pacifica           |        1|     2|49  |     47|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Pacifica>)           |
| 59|Palo Alto          |        1|    13|447 |    447|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Palo Alto>)        |
| 60|Petaluma           |        2|     6|130 |     87|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Petaluma>)              |
| 61|Piedmont           |        2|     8|289 |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/Piedmont>)             |
| 62|Pinole             |        2|    15|144 |    138|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pinole>)          |
| 63|Pittsburg          |        1|     2|124 |    118|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pittsburg>)       |
| 64|Pleasant Hill      |        1|     4|154 |    141|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pleasant Hill>)   |
| 65|Pleasanton         |        2|    28|839 |     48|ABAG  |Alameda      |[link](<counties/Alameda/cities/Pleasanton>)           |
| 66|Portola Valley     |        1|     7|27  |     30|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Portola Valley>)     |
| 67|Redwood City       |        2|     3|176 |    214|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Redwood City>)       |
| 68|Richmond           |        2|     5|383 |    321|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Richmond>)        |
| 69|Rio Vista          |        2|     9|160 |    156|ABAG  |Solano       |[link](<counties/Solano/cities/Rio Vista>)             |
| 70|Rohnert Park       |        2|     7|93  |    110|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Rohnert Park>)          |
| 71|Ross               |        1|     3|40  |     40|ABAG  |Marin        |[link](<counties/Marin/cities/Ross>)                   |
| 72|San Bruno          |        2|     4|116 |    101|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Bruno>)          |
| 73|San Carlos         |        2|     5|995 |    915|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Carlos>)         |
| 74|San Francisco      |        4|     7|174 |    156|ABAG  |San Francisco|[link](<counties/San Francisco/cities/San Francisco>)  |
| 75|San Jose           |        1|     3|231 |    124|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/San Jose>)         |
| 76|San Leandro        |        2|     8|99  |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/San Leandro>)          |
| 77|San Mateo          |        2|     8|577 |    446|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Mateo>)          |
| 78|San Pablo          |        1|     4|195 |    185|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/San Pablo>)       |
| 79|San Rafael         |        2|     3|392 |    126|ABAG  |Marin        |[link](<counties/Marin/cities/San Rafael>)             |
| 80|San Ramon          |        3|    25|195 |   2034|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/San Ramon>)       |
| 81|San Anselmo        |        1|     1|418 |    154|ABAG  |Marin        |[link](<counties/Marin/cities/San Anselmo>)            |
| 82|Santa Clara        |        2|     6|157 |    143|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Santa Clara>)      |
| 83|Santa Rosa         |        2|    20|2748|   2706|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Santa Rosa>)            |
| 84|Saratoga           |        2|    37|896 |    808|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Saratoga>)         |
| 85|Sausalito          |        2|    14|2477|   2430|ABAG  |Marin        |[link](<counties/Marin/cities/Sausalito>)              |
| 86|Sebastopol         |        2|     8|154 |    148|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Sebastopol>)            |
| 87|Sonoma             |        2|     1|20  |      0|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Sonoma>)                |
| 88|South San Francisco|        2|    11|363 |    656|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/South San Francisco>)|
| 89|Suisun City        |        2|     8|73  |     71|ABAG  |Solano       |[link](<counties/Solano/cities/Suisun City>)           |
| 90|Sunnyvale          |        1|     6|232 |    211|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Sunnyvale>)        |
| 91|Tiburon            |        2|     4|127 |    123|ABAG  |Marin        |[link](<counties/Marin/cities/Tiburon>)                |
| 92|Union City         |        2|     7|166 |    358|ABAG  |Alameda      |[link](<counties/Alameda/cities/Union City>)           |
| 93|Vacaville          |        2|    15|804 |    607|ABAG  |Solano       |[link](<counties/Solano/cities/Vacaville>)             |
| 94|Walnut Creek       |        4|    14|2810|   1656|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Walnut Creek>)    |
| 95|Windsor            |        2|     8|159 |    152|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Windsor>)               |
| 96|Woodside           |        2|     6|724 |    630|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Woodside>)           |
| 97|Yountville         |        2|     6|21  |     20|ABAG  |Napa         |[link](<counties/Napa/cities/Yountville>)              |

# SCAG (Orange County)
|   |       city        |documents|tables|apns |parcels|agency|county|                        link                        |
|--:|-------------------|--------:|-----:|-----|------:|------|------|----------------------------------------------------|
|  1|Aliso Viejo        |        2|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Aliso Viejo>)        |
|  2|Anaheim            |        3|    11|1140 |    994|SCAG  |Orange|[link](<counties/Orange/cities/Anaheim>)            |
|  3|Brea               |        4|    11|335  |    307|SCAG  |Orange|[link](<counties/Orange/cities/Brea>)               |
|  4|Buena Park         |        3|     6|2122 |   2076|SCAG  |Orange|[link](<counties/Orange/cities/Buena Park>)         |
|  5|Costa Mesa         |        4|    15|67   |     43|SCAG  |Orange|[link](<counties/Orange/cities/Costa Mesa>)         |
|  6|Cypress            |        3|     5|828  |   2846|SCAG  |Orange|[link](<counties/Orange/cities/Cypress>)            |
|  7|Dana Point         |        5|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Dana Point>)         |
|  8|Fountain Valley    |        3|     1|2    |      0|SCAG  |Orange|[link](<counties/Orange/cities/Fountain Valley>)    |
|  9|Fullerton          |        1|     1|510  |    443|SCAG  |Orange|[link](<counties/Orange/cities/Fullerton>)          |
| 10|Garden Grove       |        3|     6|1183 |   1148|SCAG  |Orange|[link](<counties/Orange/cities/Garden Grove>)       |
| 11|Irvine             |        4|    23|23764|  12975|SCAG  |Orange|[link](<counties/Orange/cities/Irvine>)             |
| 12|La Habra           |        5|     5|68   |     24|SCAG  |Orange|[link](<counties/Orange/cities/La Habra>)           |
| 13|La Palma           |        3|     4|136  |    164|SCAG  |Orange|[link](<counties/Orange/cities/La Palma>)           |
| 14|Laguna Beach       |        4|     6|82   |     60|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Beach>)       |
| 15|Laguna Hills       |        4|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Hills>)       |
| 16|Laguna Niguel      |        2|     1|9    |      4|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Niguel>)      |
| 17|Laguna Woods       |        4|    12|173  |     60|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Woods>)       |
| 18|Lake Forest        |        4|     9|1621 |    734|SCAG  |Orange|[link](<counties/Orange/cities/Lake Forest>)        |
| 19|Los Alamitos       |        4|     8|434  |    362|SCAG  |Orange|[link](<counties/Orange/cities/Los Alamitos>)       |
| 20|Mission Viejo      |        1|     1|24   |     17|SCAG  |Orange|[link](<counties/Orange/cities/Mission Viejo>)      |
| 21|Newport Beach      |        5|     4|12   |      4|SCAG  |Orange|[link](<counties/Orange/cities/Newport Beach>)      |
| 22|Orange             |        4|    12|137  |     61|SCAG  |Orange|[link](<counties/Orange/cities/Orange>)             |
| 23|Placentia          |        2|     2|589  |    566|SCAG  |Orange|[link](<counties/Orange/cities/Placentia>)          |
| 24|San Clemente       |        4|     4|220  |    216|SCAG  |Orange|[link](<counties/Orange/cities/San Clemente>)       |
| 25|San Juan Capistrano|        3|    10|397  |    283|SCAG  |Orange|[link](<counties/Orange/cities/San Juan Capistrano>)|
| 26|Santa Ana          |        3|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Santa Ana>)          |
| 27|Seal Beach         |        2|     3|422  |    333|SCAG  |Orange|[link](<counties/Orange/cities/Seal Beach>)         |
| 28|Stanton            |        3|    13|806  |    510|SCAG  |Orange|[link](<counties/Orange/cities/Stanton>)            |
| 29|Tustin             |        5|    14|399  |    203|SCAG  |Orange|[link](<counties/Orange/cities/Tustin>)             |
| 30|Villa Park         |        5|     5|13   |     12|SCAG  |Orange|[link](<counties/Orange/cities/Villa Park>)         |
| 31|Westminster        |        4|     7|5293 |   2978|SCAG  |Orange|[link](<counties/Orange/cities/Westminster>)        |
| 32|Yorba Linda        |        3|     5|617  |    346|SCAG  |Orange|[link](<counties/Orange/cities/Yorba Linda>)        |

# SCAG (Los Angeles County)
|   |        city         |documents|tables|apns|parcels|agency|  county   |                           link                            |
|--:|---------------------|--------:|-----:|----|------:|------|-----------|-----------------------------------------------------------|
|  1|Agoura Hills         |        3|     1|91  |     96|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Agoura Hills>)         |
|  2|Alhambra             |        4|     4|148 |     42|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Alhambra>)             |
|  3|Arcadia              |        5|    11|3271|   3809|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)              |
|  4|Artesia              |        2|     2|336 |    318|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Artesia>)              |
|  5|Avalon               |        4|     3|6   |      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Avalon>)               |
|  6|Azusa                |        5|    12|891 |   2858|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Azusa>)                |
|  7|Bell                 |        4|     2|32  |     36|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bell>)                 |
|  8|Bell Gardens         |        3|     3|142 |    146|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bell Gardens>)         |
|  9|Bellflower           |        4|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bellflower>)           |
| 10|Beverly Hills        |        4|     7|3416|   3167|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Beverly Hills>)        |
| 11|Bradbury             |        2|     3|51  |     46|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bradbury>)             |
| 12|Burbank              |        5|    12|3145|   3184|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Burbank>)              |
| 13|Calabasas            |        3|     4|38  |     38|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Calabasas>)            |
| 14|Carson               |        3|    11|941 |    791|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Carson>)               |
| 15|Cerritos             |        3|     5|76  |  31720|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Cerritos>)             |
| 16|Claremont            |        3|     3|265 |    284|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Claremont>)            |
| 17|Covina               |        2|     1|142 |    145|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Covina>)               |
| 18|Cudahy               |        4|     5|83  |     40|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Cudahy>)               |
| 19|Culver City          |        3|     1|1666|   1649|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Culver City>)          |
| 20|Diamond Bar          |        3|     3|642 |    598|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Diamond Bar>)          |
| 21|Downey               |        3|     4|2534|    467|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Downey>)               |
| 22|Duarte               |        3|     7|163 |    193|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Duarte>)               |
| 23|El Monte             |        3|     6|4725|   4290|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/El Monte>)             |
| 24|El Segundo           |        3|     5|92  |     69|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/El Segundo>)           |
| 25|Gardena              |        6|    16|5381|   5140|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Gardena>)              |
| 26|Glendale             |        4|     4|3691|   1170|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Glendale>)             |
| 27|Glendora             |        3|     2|339 |    284|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Glendora>)             |
| 28|Hawaiian Gardens     |        3|    13|175 |    118|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Hawaiian Gardens>)     |
| 29|Hermosa Beach        |        2|     5|174 |   3343|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Hermosa Beach>)        |
| 30|Hidden Hills         |        3|     3|18  |     64|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Hidden Hills>)         |
| 31|Huntington Park      |        4|     3|195 |    192|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Huntington Park>)      |
| 32|Industry             |        3|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Industry>)             |
| 33|Inglewood            |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Inglewood>)            |
| 34|Irwindale            |        1|     1|21  |     18|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Irwindale>)            |
| 35|La Habra Heights     |        2|     4|386 |    620|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Habra Heights>)     |
| 36|La Mirada            |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Mirada>)            |
| 37|La Puente            |        3|     2|536 |    536|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Puente>)            |
| 38|La Verne             |        3|     5|416 |      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Verne>)             |
| 39|Lakewood             |        4|     2|586 |    570|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lakewood>)             |
| 40|Lancaster            |        4|    13|3113|   3033|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lancaster>)            |
| 41|Lawndale             |        2|     4|315 |    172|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lawndale>)             |
| 42|Lomita               |        3|     7|848 |    746|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lomita>)               |
| 43|Long Beach           |        3|     1|948 |    875|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Long Beach>)           |
| 44|Lynwood              |        3|     1|8   |      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lynwood>)              |
| 45|Malibu               |        2|     2|64  |     44|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Malibu>)               |
| 46|Maywood              |        3|     3|210 |    175|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Maywood>)              |
| 47|Monrovia             |        4|     3|382 |    243|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Monrovia>)             |
| 48|Montebello           |        3|    10|40  |   2653|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Montebello>)           |
| 49|Monterey Park        |        4|     7|3353|   2856|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Monterey Park>)        |
| 50|Norwalk              |        2|     1|262 |    226|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Norwalk>)              |
| 51|Palmdale             |        5|     6|948 |    579|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Palmdale>)             |
| 52|Paramount            |        3|     7|62  |     58|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Paramount>)            |
| 53|Pasadena             |        4|     4|1636|   1057|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Pasadena>)             |
| 54|Pico Rivera          |        3|     7|80  |     55|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Pico Rivera>)          |
| 55|Pomona               |        3|    10|718 |    585|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Pomona>)               |
| 56|Rancho Palos Verdes  |        2|     1|31  |     29|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rancho Palos Verdes>)  |
| 57|Redondo Beach        |        4|     4|4007|   3799|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Redondo Beach>)        |
| 58|Rolling Hills        |        4|    20|169 |    490|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rolling Hills>)        |
| 59|Rolling Hills Estates|        6|     6|96  |     92|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rolling Hills Estates>)|
| 60|Rosemead             |        3|     7|1199|    845|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rosemead>)             |
| 61|San Dimas            |        3|     2|72  |     68|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Dimas>)            |
| 62|San Fernando         |        2|     2|213 |    212|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Fernando>)         |
| 63|San Gabriel          |        3|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Gabriel>)          |
| 64|San Marino           |        2|     4|23  |     26|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Marino>)           |
| 65|Santa Clarita        |        3|     3|289 |    285|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Santa Clarita>)        |
| 66|Santa Fe Springs     |        3|    11|175 |    136|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Santa Fe Springs>)     |
| 67|Santa Monica         |        4|     7|3345|   2860|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Santa Monica>)         |
| 68|Sierra Madre         |        5|     5|369 |    365|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Sierra Madre>)         |
| 69|Signal Hill          |        4|     6|98  |    370|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Signal Hill>)          |
| 70|South El Monte       |        3|    12|151 |     98|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/South El Monte>)       |
| 71|South Gate           |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/South Gate>)           |
| 72|South Pasadena       |        5|    79|1742|   1446|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/South Pasadena>)       |
| 73|Temple City          |        4|     3|137 |    134|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Temple City>)          |
| 74|Torrance             |        3|     7|2248|  39953|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Torrance>)             |
| 75|Vernon               |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Vernon>)               |
| 76|Walnut               |        5|    10|196 |    730|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Walnut>)               |
| 77|West Covina          |        2|     2|1080|   1098|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/West Covina>)          |
| 78|West Hollywood       |        3|    15|385 |  39422|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/West Hollywood>)       |
| 79|Westlake Village     |        3|     8|57  |     43|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Westlake Village>)     |
| 80|Whittier             |        3|     3|442 |    350|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Whittier>)             |

