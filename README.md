# Bounty Project for CA Yimby bounty
### A project to create shapefiles for all cities belonging to ABAG, SACOG and SCAG. (This project satisfies 2 bounties)

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
|   |       city        |documents|tables|apns|parcels|agency|   county    |                         link                          |
|--:|-------------------|--------:|-----:|----|------:|------|-------------|-------------------------------------------------------|
|  1|Alameda            |        2|     7|50  |     41|ABAG  |Alameda      |[link](<counties/Alameda/cities/Alameda>)              |
|  2|Albany             |        2|    27|1063|    914|ABAG  |Alameda      |[link](<counties/Alameda/cities/Albany>)               |
|  3|American Canyon    |        2|     0|   0|      0|ABAG  |Napa         |[link](<counties/Napa/cities/American Canyon>)         |
|  4|Antioch            |        2|    13|638 |    565|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Antioch>)         |
|  5|Atherton           |        2|     0|   0|      0|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Atherton>)           |
|  6|Belmont            |        2|     2|16  |     10|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Belmont>)            |
|  7|Belvedere          |        1|     3|83  |     39|ABAG  |Marin        |[link](<counties/Marin/cities/Belvedere>)              |
|  8|Benicia            |        2|    42|877 |    851|ABAG  |Solano       |[link](<counties/Solano/cities/Benicia>)               |
|  9|Berkeley           |        3|     2|576 |      7|ABAG  |Alameda      |[link](<counties/Alameda/cities/Berkeley>)             |
| 10|Brentwood          |        2|    11|295 |    220|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Brentwood>)       |
| 11|Brisbane           |        4|    12|1240|   1160|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Brisbane>)           |
| 12|Burlingame         |        1|     3|140 |     73|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Burlingame>)         |
| 13|Calistoga          |        2|     5|52  |     44|ABAG  |Napa         |[link](<counties/Napa/cities/Calistoga>)               |
| 14|Campbell           |        3|    11|997 |    941|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Campbell>)         |
| 15|Clayton            |        2|     4|102 |     90|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Clayton>)         |
| 16|Cloverdale         |        2|     5|40  |     40|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Cloverdale>)            |
| 17|Colma              |        2|     2|145 |     72|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Colma>)              |
| 18|Concord            |        2|     6|1037|    500|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Concord>)         |
| 19|Corte Madera       |        3|     0|   0|      0|ABAG  |Marin        |[link](<counties/Marin/cities/Corte Madera>)           |
| 20|Cotati             |        2|     5|69  |     50|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Cotati>)                |
| 21|Cupertino          |        1|     0|   0|      0|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Cupertino>)        |
| 22|Daly City          |        1|     2|171 |    162|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Daly City>)          |
| 23|Danville           |        2|    59|435 |    401|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Danville>)        |
| 24|Dixon              |        2|     3|33  |     15|ABAG  |Solano       |[link](<counties/Solano/cities/Dixon>)                 |
| 25|Dublin             |        2|     1|82  |      2|ABAG  |Alameda      |[link](<counties/Alameda/cities/Dublin>)               |
| 26|East Palo Alto     |        2|    16|118 |    100|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/East Palo Alto>)     |
| 27|El Cerrito         |        2|     6|160 |    149|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/El Cerrito>)      |
| 28|Emeryville         |        2|     4|230 |     14|ABAG  |Alameda      |[link](<counties/Alameda/cities/Emeryville>)           |
| 29|Fairfax            |        1|    10|432 |    289|ABAG  |Marin        |[link](<counties/Marin/cities/Fairfax>)                |
| 30|Fairfield          |        2|    11|215 |    115|ABAG  |Solano       |[link](<counties/Solano/cities/Fairfield>)             |
| 31|Foster City        |        2|    11|95  |     89|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Foster City>)        |
| 32|Fremont            |        2|     4|574 |    616|ABAG  |Alameda      |[link](<counties/Alameda/cities/Fremont>)              |
| 33|Gilroy             |        2|    33|124 |    124|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Gilroy>)           |
| 34|Hayward            |        3|     0|348 |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/Hayward>)              |
| 35|Healdsburg         |        2|     3|21  |      9|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Healdsburg>)            |
| 36|Hercules           |        3|     0|5   |      0|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Hercules>)        |
| 37|Hillsborough       |        2|     5|109 |     51|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Hillsborough>)       |
| 38|Lafayette          |        2|    26|708 |    627|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Lafayette>)       |
| 39|Larkspur           |        1|     3|80  |     37|ABAG  |Marin        |[link](<counties/Marin/cities/Larkspur>)               |
| 40|Livermore          |        3|     5|301 |      170|ABAG  |Alameda      |[link](<counties/Alameda/cities/Livermore>)            |
| 41|Los Altos          |        2|     7|589 |    577|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Altos>)        |
| 42|Los Altos Hills    |        3|    21|295 |    260|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Altos Hills>)  |
| 43|Los Gatos          |        3|    11|551 |    530|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Los Gatos>)        |
| 44|Menlo Park         |        2|   211|1088|    686|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Menlo Park>)         |
| 45|Mill Valley        |        1|     3|257 |    244|ABAG  |Marin        |[link](<counties/Marin/cities/Mill Valley>)            |
| 46|Millbrae           |        2|    14|318 |    297|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Millbrae>)           |
| 47|Milpitas           |        2|     0|   0|      0|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Milpitas>)         |
| 48|Monte Sereno       |        2|     2|280 |    116|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Monte Sereno>)     |
| 49|Moraga             |        3|     6|169 |     82|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Moraga>)          |
| 50|Morgan Hill        |        2|     3|118 |     12|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Morgan Hill>)      |
| 51|Mountain View      |        3|    10|688 |    631|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Mountain View>)    |
| 52|Napa               |        1|     0|   0|      0|ABAG  |Napa         |[link](<counties/Napa/cities/Napa>)                    |
| 53|Newark             |        1|     3|12  |     13|ABAG  |Alameda      |[link](<counties/Alameda/cities/Newark>)               |
| 54|Novato             |        1|     4|44  |     37|ABAG  |Marin        |[link](<counties/Marin/cities/Novato>)                 |
| 55|Oakland            |        2|     8|2852|     2666|ABAG  |Alameda      |[link](<counties/Alameda/cities/Oakland>)              |
| 56|Oakley             |        4|    29|596 |    559|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Oakley>)          |
| 57|Orinda             |        3|    20|1784|   1745|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Orinda>)          |
| 58|Pacifica           |        1|     2|49  |     45|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Pacifica>)           |
| 59|Palo Alto          |        1|    13|447 |    429|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Palo Alto>)        |
| 60|Petaluma           |        2|     6|130 |     84|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Petaluma>)              |
| 61|Piedmont           |        2|     3|289 |     20|ABAG  |Alameda      |[link](<counties/Alameda/cities/Piedmont>)             |
| 62|Pinole             |        2|    15|144 |    138|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pinole>)          |
| 63|Pittsburg          |        1|     2|124 |    120|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pittsburg>)       |
| 64|Pleasant Hill      |        1|     1|154 |     32|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Pleasant Hill>)   |
| 65|Pleasanton         |        2|     15|777 |      702|ABAG  |Alameda      |[link](<counties/Alameda/cities/Pleasanton>)           |
| 66|Portola Valley     |        1|     2|27  |      2|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Portola Valley>)     |
| 67|Redwood City       |        2|     3|176 |     87|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Redwood City>)       |
| 68|Richmond           |        2|     5|383 |    328|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Richmond>)        |
| 69|Rio Vista          |        2|     9|160 |    157|ABAG  |Solano       |[link](<counties/Solano/cities/Rio Vista>)             |
| 70|Rohnert Park       |        2|     5|93  |     71|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Rohnert Park>)          |
| 71|Ross               |        1|     3|40  |     40|ABAG  |Marin        |[link](<counties/Marin/cities/Ross>)                   |
| 81|San Anselmo        |        1|     1|418 |    217|ABAG  |Marin        |[link](<counties/Marin/cities/San Anselmo>)            |
| 72|San Bruno          |        2|     4|116 |    108|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Bruno>)          |
| 73|San Carlos         |        2|     4|995 |    905|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Carlos>)         |
| 74|San Francisco      |        4|     1|174 |    143|ABAG  |San Francisco|[link](<counties/San Francisco/cities/San Francisco>)  |
| 75|San Jose           |        1|     3|231 |    129|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/San Jose>)         |
| 76|San Leandro        |        2|     0|99  |      0|ABAG  |Alameda      |[link](<counties/Alameda/cities/San Leandro>)          |
| 77|San Mateo          |        2|     8|577 |    571|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/San Mateo>)          |
| 78|San Pablo          |        1|     4|195 |    193|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/San Pablo>)       |
| 79|San Rafael         |        2|     3|392 |    375|ABAG  |Marin        |[link](<counties/Marin/cities/San Rafael>)             |
| 80|San Ramon          |        3|     7|195 |     27|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/San Ramon>)       |
| 82|Santa Clara        |        2|     6|157 |    146|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Santa Clara>)      |
| 83|Santa Rosa         |        2|    10|2748|   2714|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Santa Rosa>)            |
| 84|Saratoga           |        2|    28|896 |    691|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Saratoga>)         |
| 85|Sausalito          |        2|     9|2477|   2409|ABAG  |Marin        |[link](<counties/Marin/cities/Sausalito>)              |
| 86|Sebastopol         |        2|     7|154 |    148|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Sebastopol>)            |
| 87|Sonoma             |        2|     1|20  |     16|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Sonoma>)                |
| 88|South San Francisco|        2|     9|363 |    334|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/South San Francisco>)|
| 89|Suisun City        |        2|     8|73  |     72|ABAG  |Solano       |[link](<counties/Solano/cities/Suisun City>)           |
| 90|Sunnyvale          |        1|     6|232 |    198|ABAG  |Santa Clara  |[link](<counties/Santa Clara/cities/Sunnyvale>)        |
| 91|Tiburon            |        2|     4|127 |    126|ABAG  |Marin        |[link](<counties/Marin/cities/Tiburon>)                |
| 92|Union City         |        2|     7|166 |    207|ABAG  |Alameda      |[link](<counties/Alameda/cities/Union City>)           |
| 93|Vacaville          |        2|     6|804 |    424|ABAG  |Solano       |[link](<counties/Solano/cities/Vacaville>)             |
| 94|Walnut Creek       |        4|    14|2810|   2061|ABAG  |Contra Costa |[link](<counties/Contra Costa/cities/Walnut Creek>)    |
| 95|Windsor            |        2|     8|159 |    138|ABAG  |Sonoma       |[link](<counties/Sonoma/cities/Windsor>)               |
| 96|Woodside           |        2|     1|724 |      3|ABAG  |San Mateo    |[link](<counties/San Mateo/cities/Woodside>)           |
| 97|Yountville         |        2|     3|21  |     18|ABAG  |Napa         |[link](<counties/Napa/cities/Yountville>)              |

# SACOG
|   |     city      |documents|tables|apns|parcels|agency|  county  |                       link                        |
|--:|---------------|--------:|-----:|----|------:|------|----------|---------------------------------------------------|
|  1|Auburn         |        3|     4|788 |    772|SACOG |Placer    |[link](<counties/Placer/cities/Auburn>)            |
|  2|Citrus Heights |        3|     8|162 |    133|SACOG |Sacramento|[link](<counties/Sacramento/cities/Citrus Heights>)|
|  3|Colfax         |        2|     3|53  |     51|SACOG |Placer    |[link](<counties/Placer/cities/Colfax>)            |
|  4|Davis          |        3|    16|262 |    241|SACOG |Yolo      |[link](<counties/Yolo/cities/Davis>)               |
|  5|Elk Grove      |        4|    26|693 |    470|SACOG |Sacramento|[link](<counties/Sacramento/cities/Elk Grove>)     |
|  6|Folsom         |        3|    23|932 |    806|SACOG |Sacramento|[link](<counties/Sacramento/cities/Folsom>)        |
|  7|Galt           |        4|    19|933 |    234|SACOG |Sacramento|[link](<counties/Sacramento/cities/Galt>)          |
|  8|Isleton        |        3|     2|18  |     18|SACOG |Sacramento|[link](<counties/Sacramento/cities/Isleton>)       |
|  9|Lincoln        |        2|     3|51  |     51|SACOG |Placer    |[link](<counties/Placer/cities/Lincoln>)           |
| 10|Live Oak       |        2|     2|679 |    339|SACOG |Sutter    |[link](<counties/Sutter/cities/Live Oak>)          |
| 11|Loomis         |        2|     2|122 |    116|SACOG |Placer    |[link](<counties/Placer/cities/Loomis>)            |
| 12|Marysville     |        3|     9|522 |    522|SACOG |Yuba      |[link](<counties/Yuba/cities/Marysville>)          |
| 13|Placerville    |        4|     5|122 |      6|SACOG |El Dorado |[link](<counties/El Dorado/cities/Placerville>)    |
| 14|Rancho Cordova |        3|     6|159 |    145|SACOG |Sacramento|[link](<counties/Sacramento/cities/Rancho Cordova>)|
| 15|Rocklin        |        3|     6|516 |    491|SACOG |Placer    |[link](<counties/Placer/cities/Rocklin>)           |
| 16|Roseville      |        3|     3|649 |    454|SACOG |Placer    |[link](<counties/Placer/cities/Roseville>)         |
| 17|Sacramento     |        3|     5|5132|   4918|SACOG |Sacramento|[link](<counties/Sacramento/cities/Sacramento>)    |
| 18|West Sacramento|        4|     7|642 |    576|SACOG |Yolo      |[link](<counties/Yolo/cities/West Sacramento>)     |
| 19|Wheatland      |        2|     2|108 |      106|SACOG |Yuba      |[link](<counties/Yuba/cities/Wheatland>)           |
| 20|Winters        |        3|     7|668 |    347|SACOG |Yolo      |[link](<counties/Yolo/cities/Winters>)             |
| 21|Woodland       |        5|     8|849 |    660|SACOG |Yolo      |[link](<counties/Yolo/cities/Woodland>)            |
| 22|Yuba City      |        2|    10|502 |    351|SACOG |Sutter    |[link](<counties/Sutter/cities/Yuba City>)         |


# SCAG (Orange County)
|   |       city        |documents|tables|apns |parcels|agency|county|                        link                        |
|--:|-------------------|--------:|-----:|-----|------:|------|------|----------------------------------------------------|
|  1|Aliso Viejo        |        2|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Aliso Viejo>)        |
|  2|Anaheim            |        3|     7|974  |    794|SCAG  |Orange|[link](<counties/Orange/cities/Anaheim>)            |
|  3|Brea               |        4|     9|335  |    315|SCAG  |Orange|[link](<counties/Orange/cities/Brea>)               |
|  4|Buena Park         |        3|     6|2107 |   2064|SCAG  |Orange|[link](<counties/Orange/cities/Buena Park>)         |
|  5|Costa Mesa         |        4|     5|70   |     38|SCAG  |Orange|[link](<counties/Orange/cities/Costa Mesa>)         |
|  6|Cypress            |        3|     5|828  |    644|SCAG  |Orange|[link](<counties/Orange/cities/Cypress>)            |
|  7|Dana Point         |        5|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Dana Point>)         |
|  8|Fountain Valley    |        3|     1|2    |      2|SCAG  |Orange|[link](<counties/Orange/cities/Fountain Valley>)    |
|  9|Fullerton          |        1|     1|515  |    476|SCAG  |Orange|[link](<counties/Orange/cities/Fullerton>)          |
| 10|Garden Grove       |        3|     6|1147 |   1134|SCAG  |Orange|[link](<counties/Orange/cities/Garden Grove>)       |
| 11|Irvine             |        4|    17|24842|   9446|SCAG  |Orange|[link](<counties/Orange/cities/Irvine>)             |
| 12|La Habra           |        5|     3|93   |     43|SCAG  |Orange|[link](<counties/Orange/cities/La Habra>)           |
| 13|La Palma           |        3|     3|136  |    132|SCAG  |Orange|[link](<counties/Orange/cities/La Palma>)           |
| 14|Laguna Beach       |        4|     6|82   |     60|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Beach>)       |
| 15|Laguna Hills       |        4|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Hills>)       |
| 16|Laguna Niguel      |        2|     1|4    |      1|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Niguel>)      |
| 17|Laguna Woods       |        4|     4|154  |     56|SCAG  |Orange|[link](<counties/Orange/cities/Laguna Woods>)       |
| 18|Lake Forest        |        4|     9|1618 |    819|SCAG  |Orange|[link](<counties/Orange/cities/Lake Forest>)        |
| 19|Los Alamitos       |        4|     8|434  |    362|SCAG  |Orange|[link](<counties/Orange/cities/Los Alamitos>)       |
| 20|Mission Viejo      |        1|     1|23   |     16|SCAG  |Orange|[link](<counties/Orange/cities/Mission Viejo>)      |
| 21|Newport Beach      |        5|     5|26   |     13|SCAG  |Orange|[link](<counties/Orange/cities/Newport Beach>)      |
| 22|Orange             |        4|     6|157  |     56|SCAG  |Orange|[link](<counties/Orange/cities/Orange>)             |
| 23|Placentia          |        2|     2|589  |    566|SCAG  |Orange|[link](<counties/Orange/cities/Placentia>)          |
| 24|San Clemente       |        4|     6|139  |     96|SCAG  |Orange|[link](<counties/Orange/cities/San Clemente>)       |
| 25|San Juan Capistrano|        3|     5|397  |    360|SCAG  |Orange|[link](<counties/Orange/cities/San Juan Capistrano>)|
| 26|Santa Ana          |        3|     0|    0|      0|SCAG  |Orange|[link](<counties/Orange/cities/Santa Ana>)          |
| 27|Seal Beach         |        2|     3|422  |    333|SCAG  |Orange|[link](<counties/Orange/cities/Seal Beach>)         |
| 28|Stanton            |        3|    13|806  |    522|SCAG  |Orange|[link](<counties/Orange/cities/Stanton>)            |
| 29|Tustin             |        5|     9|415  |    330|SCAG  |Orange|[link](<counties/Orange/cities/Tustin>)             |
| 30|Villa Park         |        5|     5|13   |     13|SCAG  |Orange|[link](<counties/Orange/cities/Villa Park>)         |
| 31|Westminster        |        4|     5|5182 |   2661|SCAG  |Orange|[link](<counties/Orange/cities/Westminster>)        |
| 32|Yorba Linda        |        3|     5|725  |    342|SCAG  |Orange|[link](<counties/Orange/cities/Yorba Linda>)        |

# SCAG (LA County - A through J)
|   |      city      |documents|tables|apns|parcels|agency|  county   |                         link                         |
|--:|----------------|--------:|-----:|----|------:|------|-----------|------------------------------------------------------|
|  1|Agoura Hills    |        3|     1|92  |     89|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Agoura Hills>)    |
|  2|Alhambra        |        4|     2|96  |     60|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Alhambra>)        |
|  3|Arcadia         |        5|    10|3254|   3211|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Arcadia>)         |
|  4|Artesia         |        2|     2|336 |    334|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Artesia>)         |
|  5|Avalon          |        4|     0|6   |      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Avalon>)          |
|  6|Azusa           |        5|    10|689 |    541|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Azusa>)           |
|  7|Bell            |        4|     2|32  |      5|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bell>)            |
|  8|Bell Gardens    |        3|     3|141 |    135|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bell Gardens>)    |
|  9|Bellflower      |        4|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bellflower>)      |
| 10|Beverly Hills   |        4|     8|3288|   2984|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Beverly Hills>)   |
| 11|Bradbury        |        2|     3|51  |     51|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Bradbury>)        |
| 12|Burbank         |        5|    12|3145|   3098|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Burbank>)         |
| 13|Calabasas       |        3|     4|38  |     14|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Calabasas>)       |
| 14|Carson          |        3|    10|922 |    751|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Carson>)          |
| 15|Cerritos        |        3|     4|72  |     52|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Cerritos>)        |
| 16|Claremont       |        3|     3|265 |    264|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Claremont>)       |
| 17|Covina          |        2|     1|143 |    121|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Covina>)          |
| 18|Cudahy          |        4|     4|83  |     79|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Cudahy>)          |
| 19|Culver City     |        3|     1|1666|   1652|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Culver City>)     |
| 20|Diamond Bar     |        3|     3|642 |    623|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Diamond Bar>)     |
| 21|Downey          |        3|     4|2352|   2271|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Downey>)          |
| 22|Duarte          |        3|     7|166 |    162|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Duarte>)          |
| 23|El Monte        |        3|     5|4722|   4282|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/El Monte>)        |
| 24|El Segundo      |        3|     5|92  |     62|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/El Segundo>)      |
| 25|Gardena         |        6|    16|5683|   4523|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Gardena>)         |
| 26|Glendale        |        4|     3|4126|   3613|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Glendale>)        |
| 27|Glendora        |        3|     2|339 |    301|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Glendora>)        |
| 28|Hawaiian Gardens|        3|    13|189 |    130|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Hawaiian Gardens>)|
| 29|Hermosa Beach   |        2|     3|162 |     44|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Hermosa Beach>)   |
| 30|Hidden Hills    |        3|     0|18  |      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Hidden Hills>)    |
| 31|Huntington Park |        4|     3|248 |    192|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Huntington Park>) |
| 32|Industry        |        3|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Industry>)        |
| 33|Inglewood       |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Inglewood>)       |
| 34|Irwindale       |        1|     1|21  |     21|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Irwindale>)       |

# SCAG (LA County - K through Z)
|   |        city         |documents|tables|apns|parcels|agency|  county   |                           link                            |
|--:|---------------------|--------:|-----:|----|------:|------|-----------|-----------------------------------------------------------|
|  1|La Habra Heights     |        2|     4|386 |    320|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Habra Heights>)     |
|  2|La Mirada            |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Mirada>)            |
|  3|La Puente            |        3|     2|536 |    536|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Puente>)            |
|  4|La Verne             |        3|     5|368 |    331|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/La Verne>)             |
|  5|Lakewood             |        4|     2|586 |    584|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lakewood>)             |
|  6|Lancaster            |        4|    13|3091|   2783|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lancaster>)            |
|  7|Lawndale             |        2|     3|252 |    252|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lawndale>)             |
|  8|Lomita               |        3|     7|848 |    500|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lomita>)               |
|  9|Long Beach           |        3|     1|948 |    899|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Long Beach>)           |
| 10|Lynwood              |        3|     0|8   |      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Lynwood>)              |
| 11|Malibu               |        2|     2|64  |     56|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Malibu>)               |
| 12|Maywood              |        3|     3|210 |    202|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Maywood>)              |
| 13|Monrovia             |        4|     3|378 |    287|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Monrovia>)             |
| 14|Montebello           |        3|     5|34  |     22|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Montebello>)           |
| 15|Monterey Park        |        4|     5|3276|    771|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Monterey Park>)        |
| 16|Norwalk              |        2|     1|262 |    253|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Norwalk>)              |
| 17|Palmdale             |        5|     6|592 |    570|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Palmdale>)             |
| 18|Paramount            |        3|     7|62  |     58|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Paramount>)            |
| 19|Pasadena             |        4|     4|1641|   1061|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Pasadena>)             |
| 20|Pico Rivera          |        3|     7|80  |     77|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Pico Rivera>)          |
| 21|Pomona               |        3|     4|161 |     56|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Pomona>)               |
| 22|Rancho Palos Verdes  |        2|     1|31  |     28|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rancho Palos Verdes>)  |
| 23|Redondo Beach        |        4|     4|4007|   3757|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Redondo Beach>)        |
| 24|Rolling Hills        |        4|    10|169 |    123|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rolling Hills>)        |
| 25|Rolling Hills Estates|        6|     6|96  |     90|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rolling Hills Estates>)|
| 26|Rosemead             |        3|     5|1199|    862|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Rosemead>)             |
| 27|San Dimas            |        3|     2|73  |     66|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Dimas>)            |
| 28|San Fernando         |        2|     2|213 |    213|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Fernando>)         |
| 29|San Gabriel          |        3|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Gabriel>)          |
| 30|San Marino           |        2|     4|24  |     23|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/San Marino>)           |
| 31|Santa Clarita        |        3|     3|289 |    289|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Santa Clarita>)        |
| 32|Santa Fe Springs     |        3|    10|175 |    132|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Santa Fe Springs>)     |
| 33|Santa Monica         |        4|     6|3082|   2088|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Santa Monica>)         |
| 34|Sierra Madre         |        5|     5|369 |    272|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Sierra Madre>)         |
| 35|Signal Hill          |        4|     4|100 |     61|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Signal Hill>)          |
| 36|South El Monte       |        3|    10|144 |    110|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/South El Monte>)       |
| 37|South Gate           |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/South Gate>)           |
| 38|South Pasadena       |        5|    78|1713|   1507|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/South Pasadena>)       |
| 39|Temple City          |        4|     3|137 |    131|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Temple City>)          |
| 40|Torrance             |        3|     5|2247|   1213|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Torrance>)             |
| 41|Vernon               |        2|     0|   0|      0|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Vernon>)               |
| 42|Walnut               |        5|     5|196 |    171|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Walnut>)               |
| 43|West Covina          |        2|     2|1080|   1043|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/West Covina>)          |
| 44|West Hollywood       |        3|     5|376 |    218|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/West Hollywood>)       |
| 45|Westlake Village     |        3|     6|57  |     53|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Westlake Village>)     |
| 46|Whittier             |        3|     3|442 |    420|SCAG  |Los Angeles|[link](<counties/Los Angeles/cities/Whittier>)             |

