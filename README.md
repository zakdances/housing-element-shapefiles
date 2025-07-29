# Bounty Project for CA Yimby bounty
### Shapefiles from the housing element documents of all cities that are members of ABAG, SACOG and SCAG. (This project satisfies 2 bounties)

#### (shapefile path: counties/{county name}/cities/{city name}/output/{document name}/misc)

## How this project was created:
1. I generated a list of incorporated cities along with associated planning agency (SACOG, ABAG, etc), county, and downloaded links to housing element PDFs.
2. Geojson parcel data from each county website along with cleanup, normalization, and transfer to my database.
3. Download each PDF, use machine learning to extract the data. Then do a second pass to clean up the (very messy) data. Generate metadata (page count, thumbnail, etc). Transfer all data to my database.
4. Created endpoints to query database from the UI.
5. Extra: Created web UI viewer using nextjs and react.

## Summary explained

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

## ⬇️ START Summary ([Google Sheets version here](https://docs.google.com/spreadsheets/d/1X691RBS_-0LlXX-bfAE9GXXu0P1OJnbERTqipn-C1jQ/edit?usp=sharing))

# ABAG
|   County    |    Municipality    |Sources|Tables|APNs|                                                                  Link                                                                   |
|-------------|--------------------|------:|-----:|---:|-----------------------------------------------------------------------------------------------------------------------------------------|
|Alameda      |Berkeley            |      3|   793|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Berkeley/output)                        |
|Contra Costa |Hercules            |      3|   945|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Hercules/output)                 |
|Napa         |American Canyon     |      2|   410|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/American%20Canyon/output)                  |
|San Mateo    |Broadmoor           |      0|     0|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Broadmoor/output)                   |
|San Mateo    |Half Moon Bay       |      0|     0|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Half%20Moon%20Bay/output)           |
|Napa         |Napa County         |      1|     0|   1|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Napa%20County/output)                      |
|San Mateo    |Portola Valley      |      1|   459|   2|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Portola%20Valley/output)            |
|Napa         |St. Helena          |      1|     0|   5|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/St.%20Helena/output)                       |
|Sonoma       |Healdsburg          |      2|   690|   9|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Healdsburg/output)                       |
|Alameda      |San Leandro         |      3|   820|  19|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/San%20Leandro/output)                   |
|Solano       |Dixon               |      3|   574|  19|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Dixon/output)                            |
|Alameda      |Dublin              |      3|   821|  21|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Dublin/output)                          |
|Santa Clara  |Santa Clara County  |      1|     0|  22|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Santa%20Clara%20County/output)    |
|Napa         |Yountville          |      3|   396|  24|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Yountville/output)                         |
|Santa Clara  |Morgan Hill         |      3|  1108|  25|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Morgan%20Hill/output)             |
|Contra Costa |San Ramon           |      3|   957|  27|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/San%20Ramon/output)              |
|Marin        |Corte Madera        |      4|  1427|  37|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Corte%20Madera/output)                    |
|Santa Clara  |Milpitas            |      3|   129|  39|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Milpitas/output)                  |
|Marin        |Novato              |      2|   235|  40|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Novato/output)                            |
|Alameda      |Hayward             |      4|  2604|  44|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Hayward/output)                         |
|Marin        |Belvedere           |      2|   361|  49|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Belvedere/output)                         |
|Sonoma       |Cloverdale          |      3|   425|  49|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Cloverdale/output)                       |
|Sonoma       |Sonoma County       |      1|     0|  49|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sonoma%20County/output)                  |
|Napa         |Napa                |      2|   501|  51|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Napa/output)                               |
|Solano       |California Forever  |      0|     0|  51|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/California%20Forever/output)             |
|San Mateo    |Belmont             |      3|   666|  53|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Belmont/output)                     |
|Marin        |Ross                |      2|   152|  54|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Ross/output)                              |
|Alameda      |Emeryville          |      3|  1818|  56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Emeryville/output)                      |
|San Francisco|San Francisco County|      0|     0|  56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Francisco/cities/San%20Francisco%20County/output)|
|Alameda      |Alameda             |      3|   385|  57|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda/output)                         |
|Napa         |Calistoga           |      3|   264|  57|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Calistoga/output)                          |
|Santa Clara  |Cupertino           |      2|   342|  57|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Cupertino/output)                 |
|San Mateo    |Pacifica            |      2|    42|  60|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Pacifica/output)                    |
|Sonoma       |Cotati              |      3|   781|  67|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Cotati/output)                           |
|Alameda      |Newark              |      2|   243|  69|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Newark/output)                          |
|Contra Costa |Pleasant Hill       |      2|   327|  71|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pleasant%20Hill/output)          |
|San Mateo    |Colma               |      3|   805|  73|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Colma/output)                       |
|Marin        |Larkspur            |      2|   351|  75|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Larkspur/output)                          |
|Alameda      |Piedmont            |      3|  1276|  77|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Piedmont/output)                        |
|San Mateo    |Hillsborough        |      3|  4394|  82|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Hillsborough/output)                |
|Solano       |Suisun City         |      3|   568|  84|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Suisun%20City/output)                    |
|Sonoma       |Rohnert Park        |      3|   573|  85|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Rohnert%20Park/output)                   |
|San Mateo    |Burlingame          |      2|   304|  99|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Burlingame/output)                  |
|Solano       |Solano County       |      1|     0| 102|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Solano%20County/output)                  |
|Solano       |Vallejo             |      0|     0| 102|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Vallejo/output)                          |
|Contra Costa |Clayton             |      3|   336| 106|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Clayton/output)                  |
|Contra Costa |Martinez            |      1|     0| 110|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Martinez/output)                 |
|San Mateo    |Foster City         |      3|  1372| 111|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Foster%20City/output)               |
|Sonoma       |Petaluma            |      3|   754| 118|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Petaluma/output)                         |
|Sonoma       |Sonoma              |      3|   598| 119|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sonoma/output)                           |
|Contra Costa |Pittsburg           |      1|   278| 120|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pittsburg/output)                |
|San Mateo    |Atherton            |      3|  1660| 129|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Atherton/output)                    |
|Contra Costa |Contra Costa County |      1|     0| 131|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Contra%20Costa%20County/output)  |
|San Mateo    |Woodside            |      3|  1104| 131|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Woodside/output)                    |
|Contra Costa |Pinole              |      2|  1242| 138|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pinole/output)                   |
|San Mateo    |San Bruno           |      3|  1560| 146|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Bruno/output)                 |
|Contra Costa |Moraga              |      4|  1138| 148|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Moraga/output)                   |
|Marin        |Marin County        |      1|     0| 149|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Marin%20County/output)                    |
|San Mateo    |East Palo Alto      |      3|   729| 152|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/East%20Palo%20Alto/output)          |
|San Mateo    |Redwood City        |      3|   707| 153|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Redwood%20City/output)              |
|Santa Clara  |Gilroy              |      3|  1802| 164|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Gilroy/output)                    |
|Solano       |Fairfield           |      3|   555| 166|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Fairfield/output)                        |
|Sonoma       |Windsor             |      3|   283| 166|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Windsor/output)                          |
|San Mateo    |Daly City           |      2|   266| 182|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Daly%20City/output)                 |
|Sonoma       |Sebastopol          |      3|   412| 184|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sebastopol/output)                       |
|Marin        |Tiburon             |      3|   507| 187|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Tiburon/output)                           |
|Santa Clara  |Santa Clara         |      3|   407| 209|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Santa%20Clara/output)             |
|Solano       |Rio Vista           |      3|   549| 224|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Rio%20Vista/output)                      |
|Contra Costa |El Cerrito          |      3|   448| 225|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/El%20Cerrito/output)             |
|Contra Costa |Brentwood           |      3|  1662| 232|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Brentwood/output)                |
|Marin        |Mill Valley         |      1|   519| 244|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Mill%20Valley/output)                     |
|Alameda      |Union City          |      3|   606| 264|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Union%20City/output)                    |
|Alameda      |Livermore           |      4|  2198| 273|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Livermore/output)                       |
|Contra Costa |San Pablo           |      2|   192| 279|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/San%20Pablo/output)              |
|Santa Clara  |Los Altos Hills     |      4|   884| 308|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Altos%20Hills/output)       |
|Marin        |Fairfax             |      2|   614| 319|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Fairfax/output)                           |
|San Mateo    |Millbrae            |      3|  3068| 319|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Millbrae/output)                    |
|Santa Clara  |Monte Sereno        |      3|   394| 336|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Monte%20Sereno/output)            |
|Alameda      |Alameda County      |      1|     0| 349|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda%20County/output)                |
|Marin        |San Anselmo         |      2|   585| 367|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/San%20Anselmo/output)                     |
|Santa Clara  |Sunnyvale           |      2|   309| 378|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Sunnyvale/output)                 |
|San Mateo    |San Mateo County    |      1|     0| 465|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Mateo%20County/output)        |
|Santa Clara  |Palo Alto           |      2|   341| 480|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Palo%20Alto/output)               |
|San Mateo    |South San Francisco |      3|   224| 483|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/South%20San%20Francisco/output)     |
|Solano       |Vacaville           |      3|  4287| 491|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Vacaville/output)                        |
|Contra Costa |Richmond            |      3|   234| 501|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Richmond/output)                 |
|Contra Costa |Danville            |      3|   900| 514|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Danville/output)                 |
|Marin        |San Rafael          |      3|  1789| 564|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/San%20Rafael/output)                      |
|Santa Clara  |Los Gatos           |      4|  2056| 576|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Gatos/output)               |
|Santa Clara  |San Jose            |      2|   383| 610|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/San%20Jose/output)                |
|Contra Costa |Lafayette           |      2|   847| 627|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Lafayette/output)                |
|Contra Costa |Oakley              |      5|  1830| 655|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Oakley/output)                   |
|San Mateo    |Menlo Park          |      3|  2748| 696|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Menlo%20Park/output)                |
|Santa Clara  |Los Altos           |      3|   322| 706|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Altos/output)               |
|Contra Costa |Antioch             |      3|  2790| 747|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Antioch/output)                  |
|Contra Costa |Concord             |      3|  3161| 750|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Concord/output)                  |
|Santa Clara  |Saratoga            |      3|   866| 752|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Saratoga/output)                  |
|Santa Clara  |Mountain View       |      4|   637| 754|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Mountain%20View/output)           |
|San Mateo    |San Mateo           |      3|  2599| 777|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Mateo/output)                 |
|Alameda      |Pleasanton          |      3|   470| 890|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Pleasanton/output)                      |
|Santa Clara  |Campbell            |      3|     1| 941|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Campbell/output)                  |
|Alameda      |Albany              |      3|  1103| 987|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Albany/output)                          |
|Solano       |Benicia             |      3|  1391| 993|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Benicia/output)                          |
|San Mateo    |San Carlos          |      3|   748|1073|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Carlos/output)                |
|Alameda      |Fremont             |      3|   744|1085|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Fremont/output)                         |
|San Mateo    |Brisbane            |      5|  2801|1262|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Brisbane/output)                    |
|Contra Costa |Orinda              |      4|  1271|2007|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Orinda/output)                   |
|Contra Costa |Walnut Creek        |      5|  2288|2322|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Walnut%20Creek/output)           |
|Marin        |Sausalito           |      3|   773|2451|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Sausalito/output)                         |
|Alameda      |Oakland             |      3|   961|3173|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Oakland/output)                         |
|Sonoma       |Santa Rosa          |      3|   899|3379|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Santa%20Rosa/output)                     |
|San Francisco|San Francisco       |      5|  1845|9770|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Francisco/cities/San%20Francisco/output)         |

# SACOG
|  County  |  Municipality   |Sources|Tables|APNs|                                                             Link                                                              |
|----------|-----------------|------:|-----:|---:|-------------------------------------------------------------------------------------------------------------------------------|
|Sacramento|Citrus Heights   |      4|  1021| 141|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Citrus%20Heights/output)   |
|Sacramento|Elk Grove        |      4|   922| 470|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Elk%20Grove/output)        |
|Sacramento|Folsom           |      4|   620|1215|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Folsom/output)             |
|Sacramento|Galt             |      5|   771| 395|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Galt/output)               |
|Sacramento|Isleton          |      4|   585|  23|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Isleton/output)            |
|Sacramento|Rancho Cordova   |      4|   612| 185|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Rancho%20Cordova/output)   |
|Sacramento|Sacramento       |      4|  1749|7071|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Sacramento/output)         |
|Sacramento|Sacramento County|      1|     0|2471|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sacramento/cities/Sacramento%20County/output)|
|Sutter    |Live Oak         |      2|   292| 339|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sutter/cities/Live%20Oak/output)             |
|Sutter    |Sutter County    |      1|     0|  41|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sutter/cities/Sutter%20County/output)        |
|Sutter    |Yuba City        |      3|  1188| 450|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sutter/cities/Yuba%20City/output)            |
|Yolo      |Davis            |      4|  2015| 259|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yolo/cities/Davis/output)                    |
|Yolo      |West Sacramento  |      4|   499| 576|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yolo/cities/West%20Sacramento/output)        |
|Yolo      |Winters          |      3|  1282| 347|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yolo/cities/Winters/output)                  |
|Yolo      |Woodland         |      6|  1389| 801|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yolo/cities/Woodland/output)                 |
|Yolo      |Yolo County      |      1|     0| 172|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yolo/cities/Yolo%20County/output)            |
|Yuba      |Marysville       |      4|  1874| 596|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yuba/cities/Marysville/output)               |
|Yuba      |Wheatland        |      2|   131| 106|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yuba/cities/Wheatland/output)                |
|Yuba      |Yuba County      |      1|     0| 334|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Yuba/cities/Yuba%20County/output)            |

# SCAG
|    County    |     Municipality     |Sources|Tables| APNs |                                                                   Link                                                                    |
|--------------|----------------------|------:|-----:|-----:|-------------------------------------------------------------------------------------------------------------------------------------------|
|Imperial      |Brawley               |      5|  1169|    60|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/Brawley/output)                          |
|Imperial      |Calexico              |      2|   805|    29|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/Calexico/output)                         |
|Imperial      |Calipatria            |      6|  1015|   144|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/Calipatria/output)                       |
|Imperial      |El Centro             |      3|   821|   194|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/El%20Centro/output)                      |
|Imperial      |Holtville             |      6|  1123|    55|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/Holtville/output)                        |
|Imperial      |Imperial              |      6|  1275|   367|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/Imperial/output)                         |
|Imperial      |Imperial County       |      1|     0|   112|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/Imperial%20County/output)                |
|Imperial      |Westmorland           |      1|    50|     3|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Imperial/cities/Westmorland/output)                      |
|Los Angeles   |Agoura Hills          |      3|   897|    89|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Agoura%20Hills/output)              |
|Los Angeles   |Alhambra              |      5|  1490|    80|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Alhambra/output)                    |
|Los Angeles   |Arcadia               |      5|  2573|  3211|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Arcadia/output)                     |
|Los Angeles   |Artesia               |      2|   205|   334|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Artesia/output)                     |
|Los Angeles   |Avalon                |      5|  1340|     1|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Avalon/output)                      |
|Los Angeles   |Azusa                 |      6|  1385|   724|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Azusa/output)                       |
|Los Angeles   |Baldwin Park          |      1|     0|   131|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Baldwin%20Park/output)              |
|Los Angeles   |Bell                  |      5|  2179|    14|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Bell/output)                        |
|Los Angeles   |Bell Gardens          |      3|   796|   135|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Bell%20Gardens/output)              |
|Los Angeles   |Bellflower            |      4|  1557|     0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Bellflower/output)                  |
|Los Angeles   |Beverly Hills         |      5|  1713|  3289|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Beverly%20Hills/output)             |
|Los Angeles   |Bradbury              |      3|   455|    68|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Bradbury/output)                    |
|Los Angeles   |Burbank               |      6|  2656|  3172|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Burbank/output)                     |
|Los Angeles   |Calabasas             |      4|  1015|    32|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Calabasas/output)                   |
|Los Angeles   |Carson                |      4|  1503|   794|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Carson/output)                      |
|Los Angeles   |Cerritos              |      4|  1245|    55|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Cerritos/output)                    |
|Los Angeles   |Claremont             |      4|  1424|   288|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Claremont/output)                   |
|Los Angeles   |Commerce              |      1|     0|    13|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Commerce/output)                    |
|Los Angeles   |Compton               |      0|     0|     3|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Compton/output)                     |
|Los Angeles   |Covina                |      3|   211|   163|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Covina/output)                      |
|Los Angeles   |Cudahy                |      4|  1417|    79|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Cudahy/output)                      |
|Los Angeles   |Culver City           |      3|  3223|  1652|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Culver%20City/output)               |
|Los Angeles   |Diamond Bar           |      3|   541|   623|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Diamond%20Bar/output)               |
|Los Angeles   |Downey                |      4|  1161|  2385|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Downey/output)                      |
|Los Angeles   |Duarte                |      4|   970|   177|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Duarte/output)                      |
|Los Angeles   |El Monte              |      4|  1979|  4900|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/El%20Monte/output)                  |
|Los Angeles   |El Segundo            |      3|  1145|    62|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/El%20Segundo/output)                |
|Los Angeles   |Gardena               |      6|  2468|  4523|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Gardena/output)                     |
|Los Angeles   |Glendale              |      5|  2517|  4692|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Glendale/output)                    |
|Los Angeles   |Glendora              |      4|   758|   385|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Glendora/output)                    |
|Los Angeles   |Hawaiian Gardens      |      3|  1209|   130|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Hawaiian%20Gardens/output)          |
|Los Angeles   |Hawthorne             |      1|     0|    60|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Hawthorne/output)                   |
|Los Angeles   |Hermosa Beach         |      3|   314|   122|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Hermosa%20Beach/output)             |
|Los Angeles   |Hidden Hills          |      4|   350|    18|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Hidden%20Hills/output)              |
|Los Angeles   |Huntington Park       |      5|  1616|   271|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Huntington%20Park/output)           |
|Los Angeles   |Industry              |      4|   363|     1|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Industry/output)                    |
|Los Angeles   |Inglewood             |      2|   845|     0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Inglewood/output)                   |
|Los Angeles   |Irwindale             |      1|   412|    21|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Irwindale/output)                   |
|Los Angeles   |La Canada Flintridge  |      3|  3629|  1180|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/La%20Canada%20Flintridge/output)    |
|Los Angeles   |La Habra Heights      |      2|   236|   320|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/La%20Habra%20Heights/output)        |
|Los Angeles   |La Mirada             |      3|   292|    42|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/La%20Mirada/output)                 |
|Los Angeles   |La Puente             |      4|  1205|   650|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/La%20Puente/output)                 |
|Los Angeles   |La Verne              |      4|  1611|   412|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/La%20Verne/output)                  |
|Los Angeles   |Lakewood              |      4|   591|   584|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Lakewood/output)                    |
|Los Angeles   |Lancaster             |      5|  1290|  3148|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Lancaster/output)                   |
|Los Angeles   |Lawndale              |      2|   539|   252|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Lawndale/output)                    |
|Los Angeles   |Lomita                |      4|  1117|   593|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Lomita/output)                      |
|Los Angeles   |Long Beach            |      4|   786|  2123|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Long%20Beach/output)                |
|Los Angeles   |Los Angeles           |      6|  3831|304163|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Los%20Angeles/output)               |
|Los Angeles   |Los Angeles County    |      0|     0|     0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Los%20Angeles%20County/output)      |
|Los Angeles   |Lynwood               |      4|  1138|   351|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Lynwood/output)                     |
|Los Angeles   |Malibu                |      3|   251|    59|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Malibu/output)                      |
|Los Angeles   |Manhattan Beach       |      5|  1960|    50|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Manhattan%20Beach/output)           |
|Los Angeles   |Maywood               |      4|   271|   269|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Maywood/output)                     |
|Los Angeles   |Monrovia              |      5|  1124|   387|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Monrovia/output)                    |
|Los Angeles   |Montebello            |      3|   554|    22|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Montebello/output)                  |
|Los Angeles   |Monterey Park         |      5|  1052|  1558|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Monterey%20Park/output)             |
|Los Angeles   |Norwalk               |      3|   562|   414|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Norwalk/output)                     |
|Los Angeles   |Palmdale              |      5|  2171|   570|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Palmdale/output)                    |
|Los Angeles   |Palos Verdes Estates  |      1|     0|    41|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Palos%20Verdes%20Estates/output)    |
|Los Angeles   |Paramount             |      4|   556|    74|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Paramount/output)                   |
|Los Angeles   |Pasadena              |      5|  2561|  1600|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Pasadena/output)                    |
|Los Angeles   |Pico Rivera           |      3|  1992|    77|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Pico%20Rivera/output)               |
|Los Angeles   |Pomona                |      3|  2110|    56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Pomona/output)                      |
|Los Angeles   |Rancho Palos Verdes   |      2|   496|    28|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Rancho%20Palos%20Verdes/output)     |
|Los Angeles   |Redondo Beach         |      5|  1234|  4571|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Redondo%20Beach/output)             |
|Los Angeles   |Rolling Hills         |      5|  1311|   144|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Rolling%20Hills/output)             |
|Los Angeles   |Rolling Hills Estates |      7|  1402|   106|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Rolling%20Hills%20Estates/output)   |
|Los Angeles   |Rosemead              |      4|  1398|  1226|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Rosemead/output)                    |
|Los Angeles   |San Dimas             |      3|   553|    66|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/San%20Dimas/output)                 |
|Los Angeles   |San Fernando          |      3|   627|   346|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/San%20Fernando/output)              |
|Los Angeles   |San Gabriel           |      4|   843|   144|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/San%20Gabriel/output)               |
|Los Angeles   |San Marino            |      2|   497|    23|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/San%20Marino/output)                |
|Los Angeles   |Santa Clarita         |      4|  1493|   426|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Santa%20Clarita/output)             |
|Los Angeles   |Santa Fe Springs      |      3|   482|   132|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Santa%20Fe%20Springs/output)        |
|Los Angeles   |Santa Monica          |      5|  4565|  2277|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Santa%20Monica/output)              |
|Los Angeles   |Sierra Madre          |      6|  1388|   316|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Sierra%20Madre/output)              |
|Los Angeles   |Signal Hill           |      5|   881|    80|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Signal%20Hill/output)               |
|Los Angeles   |South El Monte        |      4|  1214|   133|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/South%20El%20Monte/output)          |
|Los Angeles   |South Gate            |      3|   504|   457|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/South%20Gate/output)                |
|Los Angeles   |South Pasadena        |      6|  6903|  1533|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/South%20Pasadena/output)            |
|Los Angeles   |Temple City           |      5|  1141|   246|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Temple%20City/output)               |
|Los Angeles   |Torrance              |      4|  2407|  1451|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Torrance/output)                    |
|Los Angeles   |Vernon                |      3|   332|     3|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Vernon/output)                      |
|Los Angeles   |Walnut                |      5|  1101|   171|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Walnut/output)                      |
|Los Angeles   |West Covina           |      3|   346|  1214|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/West%20Covina/output)               |
|Los Angeles   |West Hollywood        |      4|  1598|   339|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/West%20Hollywood/output)            |
|Los Angeles   |Westlake Village      |      4|   443|    67|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Westlake%20Village/output)          |
|Los Angeles   |Whittier              |      4|  1337|   507|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Los%20Angeles/cities/Whittier/output)                    |
|Orange        |Aliso Viejo           |      3|   301|     9|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Aliso%20Viejo/output)                      |
|Orange        |Anaheim               |      4|  2429|   925|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Anaheim/output)                            |
|Orange        |Brea                  |      5|  1841|   352|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Brea/output)                               |
|Orange        |Buena Park            |      4|  1317|  2219|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Buena%20Park/output)                       |
|Orange        |Costa Mesa            |      4|  5367|    38|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Costa%20Mesa/output)                       |
|Orange        |Cypress               |      4|   805|   650|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Cypress/output)                            |
|Orange        |Dana Point            |      6|  1582|    18|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Dana%20Point/output)                       |
|Orange        |Fountain Valley       |      4|   583|     9|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Fountain%20Valley/output)                  |
|Orange        |Fullerton             |      2|   179|   479|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Fullerton/output)                          |
|Orange        |Garden Grove          |      4|  1313|  2089|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Garden%20Grove/output)                     |
|Orange        |Huntington Beach      |      0|     0|    42|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Huntington%20Beach/output)                 |
|Orange        |Irvine                |      5|  4670|  9563|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Irvine/output)                             |
|Orange        |La Habra              |      6|  1074|    66|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/La%20Habra/output)                         |
|Orange        |La Palma              |      4|   391|   172|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/La%20Palma/output)                         |
|Orange        |Laguna Beach          |      5|  1823|    71|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Laguna%20Beach/output)                     |
|Orange        |Laguna Hills          |      5|  2812|     4|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Laguna%20Hills/output)                     |
|Orange        |Laguna Niguel         |      3|   348|    67|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Laguna%20Niguel/output)                    |
|Orange        |Laguna Woods          |      4|  1840|    56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Laguna%20Woods/output)                     |
|Orange        |Lake Forest           |      5|  1694|   821|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Lake%20Forest/output)                      |
|Orange        |Los Alamitos          |      5|  1194|   379|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Los%20Alamitos/output)                     |
|Orange        |Mission Viejo         |      2|    95|    35|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Mission%20Viejo/output)                    |
|Orange        |Newport Beach         |      6|  3481|   113|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Newport%20Beach/output)                    |
|Orange        |Orange                |      4|  1675|    56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Orange/output)                             |
|Orange        |Orange County         |      0|     0|     0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Orange%20County/output)                    |
|Orange        |Placentia             |      3|   384|   709|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Placentia/output)                          |
|Orange        |Rancho Santa Margarita|      0|     0|    28|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Rancho%20Santa%20Margarita/output)         |
|Orange        |San Clemente          |      5|  1256|   149|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/San%20Clemente/output)                     |
|Orange        |San Juan Capistrano   |      4|  1639|   407|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/San%20Juan%20Capistrano/output)            |
|Orange        |Santa Ana             |      4|  1282|    96|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Santa%20Ana/output)                        |
|Orange        |Seal Beach            |      3|   612|   334|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Seal%20Beach/output)                       |
|Orange        |Stanton               |      4|  1453|   564|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Stanton/output)                            |
|Orange        |Tustin                |      5|  4131|   330|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Tustin/output)                             |
|Orange        |Villa Park            |      6|   712|    15|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Villa%20Park/output)                       |
|Orange        |Westminster           |      5|  2453|  2862|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Westminster/output)                        |
|Orange        |Yorba Linda           |      4|  1035|   374|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Orange/cities/Yorba%20Linda/output)                      |
|Riverside     |Banning               |      3|   747|  1051|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Banning/output)                         |
|Riverside     |Beaumont              |      3|   740|    89|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Beaumont/output)                        |
|Riverside     |Blythe                |      3|   364|  1643|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Blythe/output)                          |
|Riverside     |Calimesa              |      4|  1103|   530|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Calimesa/output)                        |
|Riverside     |Canyon Lake           |      4|   978|   481|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Canyon%20Lake/output)                   |
|Riverside     |Cathedral City        |      2|   305|    41|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Cathedral%20City/output)                |
|Riverside     |Coachella             |      2|   791|  1459|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Coachella/output)                       |
|Riverside     |Corona                |      4|  1683|  2638|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Corona/output)                          |
|Riverside     |Desert Hot Springs    |      5|  1243|  1537|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Desert%20Hot%20Springs/output)          |
|Riverside     |Eastvale              |      3|   615|   208|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Eastvale/output)                        |
|Riverside     |Hemet                 |      3|   804|  3674|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Hemet/output)                           |
|Riverside     |Indian Wells          |      3|   458|    26|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Indian%20Wells/output)                  |
|Riverside     |Indio                 |      4|  1606|  1269|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Indio/output)                           |
|Riverside     |Jurupa Valley         |      4|  1329|   466|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Jurupa%20Valley/output)                 |
|Riverside     |La Quinta             |      6|  1102|  1882|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/La%20Quinta/output)                     |
|Riverside     |Lake Elsinore         |      4|  1183|  1080|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Lake%20Elsinore/output)                 |
|Riverside     |Menifee               |      8|  3906|  4147|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Menifee/output)                         |
|Riverside     |Moreno Valley         |      4|  2347| 13676|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Moreno%20Valley/output)                 |
|Riverside     |Murrieta              |      5|  1913|  4446|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Murrieta/output)                        |
|Riverside     |Norco                 |      6|  3029|   503|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Norco/output)                           |
|Riverside     |Palm Desert           |      6|  1069|   221|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Palm%20Desert/output)                   |
|Riverside     |Palm Springs          |      4|   886|    65|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Palm%20Springs/output)                  |
|Riverside     |Perris                |      5|  2298|   683|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Perris/output)                          |
|Riverside     |Rancho Mirage         |      6|   467|   465|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Rancho%20Mirage/output)                 |
|Riverside     |Riverside             |      5|  1955|  3040|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Riverside/output)                       |
|Riverside     |Riverside County      |      1|     0|   295|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Riverside%20County/output)              |
|Riverside     |San Jacinto           |      3|  2697|   799|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/San%20Jacinto/output)                   |
|Riverside     |Temecula              |      4|  2050|   525|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Temecula/output)                        |
|Riverside     |Wildomar              |      3|   508|   445|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Riverside/cities/Wildomar/output)                        |
|San Bernardino|Adelanto              |      2|   171|   564|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Adelanto/output)                 |
|San Bernardino|Apple Valley          |      7|  1681|    38|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Apple%20Valley/output)           |
|San Bernardino|Barstow               |      3|   602|    25|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Barstow/output)                  |
|San Bernardino|Big Bear Lake         |      5|   498|    38|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Big%20Bear%20Lake/output)        |
|San Bernardino|Chino                 |      4|  2000|   130|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Chino/output)                    |
|San Bernardino|Chino Hills           |      6|  1340|     9|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Chino%20Hills/output)            |
|San Bernardino|Colton                |      4|   868|   251|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Colton/output)                   |
|San Bernardino|Fontana               |      5|  2354|   473|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Fontana/output)                  |
|San Bernardino|Grand Terrace         |      1|    81|   186|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Grand%20Terrace/output)          |
|San Bernardino|Hesperia              |      6|  1260|  1289|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Hesperia/output)                 |
|San Bernardino|Highland              |      3|  1165|   238|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Highland/output)                 |
|San Bernardino|Loma Linda            |      5|  1240|   408|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Loma%20Linda/output)             |
|San Bernardino|Montclair             |      3|   836|     3|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Montclair/output)                |
|San Bernardino|Needles               |      3|   550|    13|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Needles/output)                  |
|San Bernardino|Ontario               |      4|   982|    61|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Ontario/output)                  |
|San Bernardino|Rancho Cucamonga      |      4|  1142|     6|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Rancho%20Cucamonga/output)       |
|San Bernardino|Redlands              |      5|  1022|   137|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Redlands/output)                 |
|San Bernardino|Rialto                |      5|  2828|    68|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Rialto/output)                   |
|San Bernardino|San Bernardino        |      1|     0|   555|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/San%20Bernardino/output)         |
|San Bernardino|San Bernardino County |      1|     0|    54|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/San%20Bernardino%20County/output)|
|San Bernardino|Twentynine Palms      |      4|   786|    23|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Twentynine%20Palms/output)       |
|San Bernardino|Upland                |      3|   477|    20|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Upland/output)                   |
|San Bernardino|Victorville           |      5|  2631|   378|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Victorville/output)              |
|San Bernardino|Yucaipa               |      5|  1028|    10|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Yucaipa/output)                  |
|San Bernardino|Yucca Valley          |      4|   962|   265|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Bernardino/cities/Yucca%20Valley/output)           |
|Ventura       |Camarillo             |      4|  1289|   218|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Camarillo/output)                         |
|Ventura       |Fillmore              |      1|   292|   218|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Fillmore/output)                          |
|Ventura       |Moorpark              |      4|   985|   218|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Moorpark/output)                          |
|Ventura       |Ojai                  |      3|   548|   218|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Ojai/output)                              |
|Ventura       |Oxnard                |      5|  2657|  2754|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Oxnard/output)                            |
|Ventura       |Port Hueneme          |      3|   648|   274|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Port%20Hueneme/output)                    |
|Ventura       |Santa Paula           |      3|   519|   218|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Santa%20Paula/output)                     |
|Ventura       |Simi Valley           |      5|  1429|   767|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Simi%20Valley/output)                     |
|Ventura       |Thousand Oaks         |      3|  1193|    59|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Thousand%20Oaks/output)                   |
|Ventura       |Ventura               |      5|  1738|  1300|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Ventura/output)                           |
|Ventura       |Ventura County        |      1|     0|   276|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Ventura/cities/Ventura%20County/output)                  |

## END Summary

