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
|Alameda      |Alameda             |      3|   385|  57|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda/output)                         |
|Alameda      |Alameda County      |      1|     0| 349|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda%20County/output)                |
|Alameda      |Albany              |      3|  1103| 987|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Albany/output)                          |
|Alameda      |Berkeley            |      3|   793|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Berkeley/output)                        |
|Alameda      |Dublin              |      3|   821|  21|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Dublin/output)                          |
|Alameda      |Emeryville          |      3|  1818|  56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Emeryville/output)                      |
|Alameda      |Fremont             |      3|   744|1085|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Fremont/output)                         |
|Alameda      |Hayward             |      4|  2604|  44|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Hayward/output)                         |
|Alameda      |Livermore           |      4|  2198| 273|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Livermore/output)                       |
|Alameda      |Newark              |      2|   243|  69|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Newark/output)                          |
|Alameda      |Oakland             |      3|   961|3173|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Oakland/output)                         |
|Alameda      |Piedmont            |      3|  1276|  77|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Piedmont/output)                        |
|Alameda      |Pleasanton          |      3|   470| 890|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Pleasanton/output)                      |
|Alameda      |San Leandro         |      3|   820|  19|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/San%20Leandro/output)                   |
|Alameda      |Union City          |      3|   606| 264|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Union%20City/output)                    |
|Contra Costa |Antioch             |      3|  2790| 747|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Antioch/output)                  |
|Contra Costa |Brentwood           |      3|  1662| 232|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Brentwood/output)                |
|Contra Costa |Clayton             |      3|   336| 106|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Clayton/output)                  |
|Contra Costa |Concord             |      3|  3161| 750|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Concord/output)                  |
|Contra Costa |Contra Costa County |      1|     0| 131|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Contra%20Costa%20County/output)  |
|Contra Costa |Danville            |      3|   900| 514|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Danville/output)                 |
|Contra Costa |El Cerrito          |      3|   448| 225|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/El%20Cerrito/output)             |
|Contra Costa |Hercules            |      3|   945|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Hercules/output)                 |
|Contra Costa |Lafayette           |      2|   847| 627|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Lafayette/output)                |
|Contra Costa |Martinez            |      1|     0| 110|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Martinez/output)                 |
|Contra Costa |Moraga              |      4|  1138| 148|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Moraga/output)                   |
|Contra Costa |Oakley              |      5|  1830| 655|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Oakley/output)                   |
|Contra Costa |Orinda              |      4|  1271|2007|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Orinda/output)                   |
|Contra Costa |Pinole              |      2|  1242| 138|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pinole/output)                   |
|Contra Costa |Pittsburg           |      1|   278| 120|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pittsburg/output)                |
|Contra Costa |Pleasant Hill       |      2|   327|  71|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pleasant%20Hill/output)          |
|Contra Costa |Richmond            |      3|   234| 501|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Richmond/output)                 |
|Contra Costa |San Pablo           |      2|   192| 279|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/San%20Pablo/output)              |
|Contra Costa |San Ramon           |      3|   957|  27|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/San%20Ramon/output)              |
|Contra Costa |Walnut Creek        |      5|  2288|2322|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Walnut%20Creek/output)           |
|Marin        |Belvedere           |      2|   361|  49|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Belvedere/output)                         |
|Marin        |Corte Madera        |      4|  1427|  37|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Corte%20Madera/output)                    |
|Marin        |Fairfax             |      2|   614| 319|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Fairfax/output)                           |
|Marin        |Larkspur            |      2|   351|  75|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Larkspur/output)                          |
|Marin        |Marin County        |      1|     0| 149|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Marin%20County/output)                    |
|Marin        |Mill Valley         |      1|   519| 244|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Mill%20Valley/output)                     |
|Marin        |Novato              |      2|   235|  40|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Novato/output)                            |
|Marin        |Ross                |      2|   152|  54|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Ross/output)                              |
|Marin        |San Anselmo         |      2|   585| 367|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/San%20Anselmo/output)                     |
|Marin        |San Rafael          |      3|  1789| 564|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/San%20Rafael/output)                      |
|Marin        |Sausalito           |      3|   773|2451|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Sausalito/output)                         |
|Marin        |Tiburon             |      3|   507| 187|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Tiburon/output)                           |
|Napa         |American Canyon     |      2|   410|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/American%20Canyon/output)                  |
|Napa         |Calistoga           |      3|   264|  57|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Calistoga/output)                          |
|Napa         |Napa                |      2|   501|  51|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Napa/output)                               |
|Napa         |Napa County         |      1|     0|   1|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Napa%20County/output)                      |
|Napa         |St. Helena          |      1|     0|   5|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/St.%20Helena/output)                       |
|Napa         |Yountville          |      3|   396|  24|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Yountville/output)                         |
|San Francisco|San Francisco       |      5|  1845|9770|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Francisco/cities/San%20Francisco/output)         |
|San Francisco|San Francisco County|      0|     0|  56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Francisco/cities/San%20Francisco%20County/output)|
|San Mateo    |Atherton            |      3|  1660| 129|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Atherton/output)                    |
|San Mateo    |Belmont             |      3|   666|  53|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Belmont/output)                     |
|San Mateo    |Brisbane            |      5|  2801|1262|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Brisbane/output)                    |
|San Mateo    |Broadmoor           |      0|     0|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Broadmoor/output)                   |
|San Mateo    |Burlingame          |      2|   304|  99|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Burlingame/output)                  |
|San Mateo    |Colma               |      3|   805|  73|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Colma/output)                       |
|San Mateo    |Daly City           |      2|   266| 182|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Daly%20City/output)                 |
|San Mateo    |East Palo Alto      |      3|   729| 152|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/East%20Palo%20Alto/output)          |
|San Mateo    |Foster City         |      3|  1372| 111|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Foster%20City/output)               |
|San Mateo    |Half Moon Bay       |      0|     0|   0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Half%20Moon%20Bay/output)           |
|San Mateo    |Hillsborough        |      3|  4394|  82|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Hillsborough/output)                |
|San Mateo    |Menlo Park          |      3|  2748| 696|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Menlo%20Park/output)                |
|San Mateo    |Millbrae            |      3|  3068| 319|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Millbrae/output)                    |
|San Mateo    |Pacifica            |      2|    42|  60|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Pacifica/output)                    |
|San Mateo    |Portola Valley      |      1|   459|   2|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Portola%20Valley/output)            |
|San Mateo    |Redwood City        |      3|   707| 153|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Redwood%20City/output)              |
|San Mateo    |San Bruno           |      3|  1560| 146|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Bruno/output)                 |
|San Mateo    |San Carlos          |      3|   748|1073|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Carlos/output)                |
|San Mateo    |San Mateo           |      3|  2599| 777|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Mateo/output)                 |
|San Mateo    |San Mateo County    |      1|     0| 465|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Mateo%20County/output)        |
|San Mateo    |South San Francisco |      3|   224| 483|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/South%20San%20Francisco/output)     |
|San Mateo    |Woodside            |      3|  1104| 131|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Woodside/output)                    |
|Santa Clara  |Campbell            |      3|     1| 941|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Campbell/output)                  |
|Santa Clara  |Cupertino           |      2|   342|  57|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Cupertino/output)                 |
|Santa Clara  |Gilroy              |      3|  1802| 164|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Gilroy/output)                    |
|Santa Clara  |Los Altos           |      3|   322| 706|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Altos/output)               |
|Santa Clara  |Los Altos Hills     |      4|   884| 308|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Altos%20Hills/output)       |
|Santa Clara  |Los Gatos           |      4|  2056| 576|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Gatos/output)               |
|Santa Clara  |Milpitas            |      3|   129|  39|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Milpitas/output)                  |
|Santa Clara  |Monte Sereno        |      3|   394| 336|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Monte%20Sereno/output)            |
|Santa Clara  |Morgan Hill         |      3|  1108|  25|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Morgan%20Hill/output)             |
|Santa Clara  |Mountain View       |      4|   637| 754|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Mountain%20View/output)           |
|Santa Clara  |Palo Alto           |      2|   341| 480|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Palo%20Alto/output)               |
|Santa Clara  |San Jose            |      2|   383| 610|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/San%20Jose/output)                |
|Santa Clara  |Santa Clara         |      3|   407| 209|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Santa%20Clara/output)             |
|Santa Clara  |Santa Clara County  |      1|     0|  22|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Santa%20Clara%20County/output)    |
|Santa Clara  |Saratoga            |      3|   866| 752|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Saratoga/output)                  |
|Santa Clara  |Sunnyvale           |      2|   309| 378|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Sunnyvale/output)                 |
|Solano       |Benicia             |      3|  1391| 993|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Benicia/output)                          |
|Solano       |California Forever  |      0|     0|  51|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/California%20Forever/output)             |
|Solano       |Dixon               |      3|   574|  19|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Dixon/output)                            |
|Solano       |Fairfield           |      3|   555| 166|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Fairfield/output)                        |
|Solano       |Rio Vista           |      3|   549| 224|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Rio%20Vista/output)                      |
|Solano       |Solano County       |      1|     0| 102|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Solano%20County/output)                  |
|Solano       |Suisun City         |      3|   568|  84|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Suisun%20City/output)                    |
|Solano       |Vacaville           |      3|  4287| 491|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Vacaville/output)                        |
|Solano       |Vallejo             |      0|     0| 102|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Vallejo/output)                          |
|Sonoma       |Cloverdale          |      3|   425|  49|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Cloverdale/output)                       |
|Sonoma       |Cotati              |      3|   781|  67|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Cotati/output)                           |
|Sonoma       |Healdsburg          |      2|   690|   9|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Healdsburg/output)                       |
|Sonoma       |Petaluma            |      3|   754| 118|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Petaluma/output)                         |
|Sonoma       |Rohnert Park        |      3|   573|  85|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Rohnert%20Park/output)                   |
|Sonoma       |Santa Rosa          |      3|   899|3379|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Santa%20Rosa/output)                     |
|Sonoma       |Sebastopol          |      3|   412| 184|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sebastopol/output)                       |
|Sonoma       |Sonoma              |      3|   598| 119|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sonoma/output)                           |
|Sonoma       |Sonoma County       |      1|     0|  49|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sonoma%20County/output)                  |
|Sonoma       |Windsor             |      3|   283| 166|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Windsor/output)                          |

# SACOG
|  County  |  Municipality   |Sources|Tables|APNs|                                                          Link                                                           |
|----------|-----------------|------:|-----:|---:|-------------------------------------------------------------------------------------------------------------------------|
|Sacramento|Citrus Heights   |      4|  1021| 141|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda/output)         |
|Sacramento|Elk Grove        |      4|   922| 470|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda%20County/output)|
|Sacramento|Folsom           |      4|   620|1215|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Albany/output)          |
|Sacramento|Galt             |      5|   771| 395|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Berkeley/output)        |
|Sacramento|Isleton          |      4|   585|  23|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Dublin/output)          |
|Sacramento|Rancho Cordova   |      4|   612| 185|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Emeryville/output)      |
|Sacramento|Sacramento       |      4|  1749|7071|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Fremont/output)         |
|Sacramento|Sacramento County|      1|     0|2471|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Hayward/output)         |
|Sutter    |Live Oak         |      2|   292| 339|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Livermore/output)       |
|Sutter    |Sutter County    |      1|     0|  41|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Newark/output)          |
|Sutter    |Yuba City        |      3|  1188| 450|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Oakland/output)         |
|Yolo      |Davis            |      4|  2015| 259|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Piedmont/output)        |
|Yolo      |West Sacramento  |      4|   499| 576|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Pleasanton/output)      |
|Yolo      |Winters          |      3|  1282| 347|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/San%20Leandro/output)   |
|Yolo      |Woodland         |      6|  1389| 801|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Union%20City/output)    |
|Yolo      |Yolo County      |      1|     0| 172|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Antioch/output)  |
|Yuba      |Marysville       |      4|  1874| 596|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Brentwood/output)|
|Yuba      |Wheatland        |      2|   131| 106|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Clayton/output)  |
|Yuba      |Yuba County      |      1|     0| 334|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Concord/output)  |

# SCAG
|    County    |     Municipality     |Sources|Tables| APNs |                                                                  Link                                                                   |
|--------------|----------------------|------:|-----:|-----:|-----------------------------------------------------------------------------------------------------------------------------------------|
|Imperial      |Brawley               |      5|  1169|    60|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda/output)                         |
|Imperial      |Calexico              |      2|   805|    29|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Alameda%20County/output)                |
|Imperial      |Calipatria            |      6|  1015|   144|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Albany/output)                          |
|Imperial      |El Centro             |      3|   821|   194|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Berkeley/output)                        |
|Imperial      |Holtville             |      6|  1123|    55|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Dublin/output)                          |
|Imperial      |Imperial              |      6|  1275|   367|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Emeryville/output)                      |
|Imperial      |Imperial County       |      1|     0|   112|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Fremont/output)                         |
|Imperial      |Westmorland           |      1|    50|     3|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Hayward/output)                         |
|Los Angeles   |Agoura Hills          |      3|   897|    89|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Livermore/output)                       |
|Los Angeles   |Alhambra              |      5|  1490|    80|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Newark/output)                          |
|Los Angeles   |Arcadia               |      5|  2573|  3211|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Oakland/output)                         |
|Los Angeles   |Artesia               |      2|   205|   334|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Piedmont/output)                        |
|Los Angeles   |Avalon                |      5|  1340|     1|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Pleasanton/output)                      |
|Los Angeles   |Azusa                 |      6|  1385|   724|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/San%20Leandro/output)                   |
|Los Angeles   |Baldwin Park          |      1|     0|   131|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Alameda/cities/Union%20City/output)                    |
|Los Angeles   |Bell                  |      5|  2179|    14|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Antioch/output)                  |
|Los Angeles   |Bell Gardens          |      3|   796|   135|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Brentwood/output)                |
|Los Angeles   |Bellflower            |      4|  1557|     0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Clayton/output)                  |
|Los Angeles   |Beverly Hills         |      5|  1713|  3289|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Concord/output)                  |
|Los Angeles   |Bradbury              |      3|   455|    68|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Contra%20Costa%20County/output)  |
|Los Angeles   |Burbank               |      6|  2656|  3172|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Danville/output)                 |
|Los Angeles   |Calabasas             |      4|  1015|    32|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/El%20Cerrito/output)             |
|Los Angeles   |Carson                |      4|  1503|   794|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Hercules/output)                 |
|Los Angeles   |Cerritos              |      4|  1245|    55|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Lafayette/output)                |
|Los Angeles   |Claremont             |      4|  1424|   288|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Martinez/output)                 |
|Los Angeles   |Commerce              |      1|     0|    13|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Moraga/output)                   |
|Los Angeles   |Compton               |      0|     0|     3|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Oakley/output)                   |
|Los Angeles   |Covina                |      3|   211|   163|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Orinda/output)                   |
|Los Angeles   |Cudahy                |      4|  1417|    79|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pinole/output)                   |
|Los Angeles   |Culver City           |      3|  3223|  1652|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pittsburg/output)                |
|Los Angeles   |Diamond Bar           |      3|   541|   623|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Pleasant%20Hill/output)          |
|Los Angeles   |Downey                |      4|  1161|  2385|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Richmond/output)                 |
|Los Angeles   |Duarte                |      4|   970|   177|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/San%20Pablo/output)              |
|Los Angeles   |El Monte              |      4|  1979|  4900|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/San%20Ramon/output)              |
|Los Angeles   |El Segundo            |      3|  1145|    62|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Contra%20Costa/cities/Walnut%20Creek/output)           |
|Los Angeles   |Gardena               |      6|  2468|  4523|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Belvedere/output)                         |
|Los Angeles   |Glendale              |      5|  2517|  4692|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Corte%20Madera/output)                    |
|Los Angeles   |Glendora              |      4|   758|   385|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Fairfax/output)                           |
|Los Angeles   |Hawaiian Gardens      |      3|  1209|   130|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Larkspur/output)                          |
|Los Angeles   |Hawthorne             |      1|     0|    60|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Marin%20County/output)                    |
|Los Angeles   |Hermosa Beach         |      3|   314|   122|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Mill%20Valley/output)                     |
|Los Angeles   |Hidden Hills          |      4|   350|    18|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Novato/output)                            |
|Los Angeles   |Huntington Park       |      5|  1616|   271|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Ross/output)                              |
|Los Angeles   |Industry              |      4|   363|     1|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/San%20Anselmo/output)                     |
|Los Angeles   |Inglewood             |      2|   845|     0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/San%20Rafael/output)                      |
|Los Angeles   |Irwindale             |      1|   412|    21|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Sausalito/output)                         |
|Los Angeles   |La Canada Flintridge  |      3|  3629|  1180|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Marin/cities/Tiburon/output)                           |
|Los Angeles   |La Habra Heights      |      2|   236|   320|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/American%20Canyon/output)                  |
|Los Angeles   |La Mirada             |      3|   292|    42|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Calistoga/output)                          |
|Los Angeles   |La Puente             |      4|  1205|   650|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Napa/output)                               |
|Los Angeles   |La Verne              |      4|  1611|   412|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Napa%20County/output)                      |
|Los Angeles   |Lakewood              |      4|   591|   584|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/St.%20Helena/output)                       |
|Los Angeles   |Lancaster             |      5|  1290|  3148|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Napa/cities/Yountville/output)                         |
|Los Angeles   |Lawndale              |      2|   539|   252|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Francisco/cities/San%20Francisco/output)         |
|Los Angeles   |Lomita                |      4|  1117|   593|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Francisco/cities/San%20Francisco%20County/output)|
|Los Angeles   |Long Beach            |      4|   786|  2123|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Atherton/output)                    |
|Los Angeles   |Los Angeles           |      6|  3831|304163|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Belmont/output)                     |
|Los Angeles   |Los Angeles County    |      0|     0|     0|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Brisbane/output)                    |
|Los Angeles   |Lynwood               |      4|  1138|   351|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Broadmoor/output)                   |
|Los Angeles   |Malibu                |      3|   251|    59|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Burlingame/output)                  |
|Los Angeles   |Manhattan Beach       |      5|  1960|    50|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Colma/output)                       |
|Los Angeles   |Maywood               |      4|   271|   269|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Daly%20City/output)                 |
|Los Angeles   |Monrovia              |      5|  1124|   387|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/East%20Palo%20Alto/output)          |
|Los Angeles   |Montebello            |      3|   554|    22|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Foster%20City/output)               |
|Los Angeles   |Monterey Park         |      5|  1052|  1558|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Half%20Moon%20Bay/output)           |
|Los Angeles   |Norwalk               |      3|   562|   414|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Hillsborough/output)                |
|Los Angeles   |Palmdale              |      5|  2171|   570|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Menlo%20Park/output)                |
|Los Angeles   |Palos Verdes Estates  |      1|     0|    41|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Millbrae/output)                    |
|Los Angeles   |Paramount             |      4|   556|    74|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Pacifica/output)                    |
|Los Angeles   |Pasadena              |      5|  2561|  1600|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Portola%20Valley/output)            |
|Los Angeles   |Pico Rivera           |      3|  1992|    77|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Redwood%20City/output)              |
|Los Angeles   |Pomona                |      3|  2110|    56|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Bruno/output)                 |
|Los Angeles   |Rancho Palos Verdes   |      2|   496|    28|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Carlos/output)                |
|Los Angeles   |Redondo Beach         |      5|  1234|  4571|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Mateo/output)                 |
|Los Angeles   |Rolling Hills         |      5|  1311|   144|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/San%20Mateo%20County/output)        |
|Los Angeles   |Rolling Hills Estates |      7|  1402|   106|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/South%20San%20Francisco/output)     |
|Los Angeles   |Rosemead              |      4|  1398|  1226|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/San%20Mateo/cities/Woodside/output)                    |
|Los Angeles   |San Dimas             |      3|   553|    66|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Campbell/output)                  |
|Los Angeles   |San Fernando          |      3|   627|   346|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Cupertino/output)                 |
|Los Angeles   |San Gabriel           |      4|   843|   144|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Gilroy/output)                    |
|Los Angeles   |San Marino            |      2|   497|    23|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Altos/output)               |
|Los Angeles   |Santa Clarita         |      4|  1493|   426|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Altos%20Hills/output)       |
|Los Angeles   |Santa Fe Springs      |      3|   482|   132|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Los%20Gatos/output)               |
|Los Angeles   |Santa Monica          |      5|  4565|  2277|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Milpitas/output)                  |
|Los Angeles   |Sierra Madre          |      6|  1388|   316|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Monte%20Sereno/output)            |
|Los Angeles   |Signal Hill           |      5|   881|    80|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Morgan%20Hill/output)             |
|Los Angeles   |South El Monte        |      4|  1214|   133|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Mountain%20View/output)           |
|Los Angeles   |South Gate            |      3|   504|   457|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Palo%20Alto/output)               |
|Los Angeles   |South Pasadena        |      6|  6903|  1533|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/San%20Jose/output)                |
|Los Angeles   |Temple City           |      5|  1141|   246|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Santa%20Clara/output)             |
|Los Angeles   |Torrance              |      4|  2407|  1451|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Santa%20Clara%20County/output)    |
|Los Angeles   |Vernon                |      3|   332|     3|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Saratoga/output)                  |
|Los Angeles   |Walnut                |      5|  1101|   171|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Santa%20Clara/cities/Sunnyvale/output)                 |
|Los Angeles   |West Covina           |      3|   346|  1214|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Benicia/output)                          |
|Los Angeles   |West Hollywood        |      4|  1598|   339|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/California%20Forever/output)             |
|Los Angeles   |Westlake Village      |      4|   443|    67|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Dixon/output)                            |
|Los Angeles   |Whittier              |      4|  1337|   507|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Fairfield/output)                        |
|Orange        |Aliso Viejo           |      3|   301|     9|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Rio%20Vista/output)                      |
|Orange        |Anaheim               |      4|  2429|   925|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Solano%20County/output)                  |
|Orange        |Brea                  |      5|  1841|   352|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Suisun%20City/output)                    |
|Orange        |Buena Park            |      4|  1317|  2219|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Vacaville/output)                        |
|Orange        |Costa Mesa            |      4|  5367|    38|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Solano/cities/Vallejo/output)                          |
|Orange        |Cypress               |      4|   805|   650|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Cloverdale/output)                       |
|Orange        |Dana Point            |      6|  1582|    18|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Cotati/output)                           |
|Orange        |Fountain Valley       |      4|   583|     9|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Healdsburg/output)                       |
|Orange        |Fullerton             |      2|   179|   479|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Petaluma/output)                         |
|Orange        |Garden Grove          |      4|  1313|  2089|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Rohnert%20Park/output)                   |
|Orange        |Huntington Beach      |      0|     0|    42|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Santa%20Rosa/output)                     |
|Orange        |Irvine                |      5|  4670|  9563|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sebastopol/output)                       |
|Orange        |La Habra              |      6|  1074|    66|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sonoma/output)                           |
|Orange        |La Palma              |      4|   391|   172|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Sonoma%20County/output)                  |
|Orange        |Laguna Beach          |      5|  1823|    71|[link](https://github.com/zakdances/housing-element-shapefiles/tree/main/counties/Sonoma/cities/Windsor/output)                          |
|Orange        |Laguna Hills          |      5|  2812|     4|NaN                                                                                                                                      |
|Orange        |Laguna Niguel         |      3|   348|    67|NaN                                                                                                                                      |
|Orange        |Laguna Woods          |      4|  1840|    56|NaN                                                                                                                                      |
|Orange        |Lake Forest           |      5|  1694|   821|NaN                                                                                                                                      |
|Orange        |Los Alamitos          |      5|  1194|   379|NaN                                                                                                                                      |
|Orange        |Mission Viejo         |      2|    95|    35|NaN                                                                                                                                      |
|Orange        |Newport Beach         |      6|  3481|   113|NaN                                                                                                                                      |
|Orange        |Orange                |      4|  1675|    56|NaN                                                                                                                                      |
|Orange        |Orange County         |      0|     0|     0|NaN                                                                                                                                      |
|Orange        |Placentia             |      3|   384|   709|NaN                                                                                                                                      |
|Orange        |Rancho Santa Margarita|      0|     0|    28|NaN                                                                                                                                      |
|Orange        |San Clemente          |      5|  1256|   149|NaN                                                                                                                                      |
|Orange        |San Juan Capistrano   |      4|  1639|   407|NaN                                                                                                                                      |
|Orange        |Santa Ana             |      4|  1282|    96|NaN                                                                                                                                      |
|Orange        |Seal Beach            |      3|   612|   334|NaN                                                                                                                                      |
|Orange        |Stanton               |      4|  1453|   564|NaN                                                                                                                                      |
|Orange        |Tustin                |      5|  4131|   330|NaN                                                                                                                                      |
|Orange        |Villa Park            |      6|   712|    15|NaN                                                                                                                                      |
|Orange        |Westminster           |      5|  2453|  2862|NaN                                                                                                                                      |
|Orange        |Yorba Linda           |      4|  1035|   374|NaN                                                                                                                                      |
|Riverside     |Banning               |      3|   747|  1051|NaN                                                                                                                                      |
|Riverside     |Beaumont              |      3|   740|    89|NaN                                                                                                                                      |
|Riverside     |Blythe                |      3|   364|  1643|NaN                                                                                                                                      |
|Riverside     |Calimesa              |      4|  1103|   530|NaN                                                                                                                                      |
|Riverside     |Canyon Lake           |      4|   978|   481|NaN                                                                                                                                      |
|Riverside     |Cathedral City        |      2|   305|    41|NaN                                                                                                                                      |
|Riverside     |Coachella             |      2|   791|  1459|NaN                                                                                                                                      |
|Riverside     |Corona                |      4|  1683|  2638|NaN                                                                                                                                      |
|Riverside     |Desert Hot Springs    |      5|  1243|  1537|NaN                                                                                                                                      |
|Riverside     |Eastvale              |      3|   615|   208|NaN                                                                                                                                      |
|Riverside     |Hemet                 |      3|   804|  3674|NaN                                                                                                                                      |
|Riverside     |Indian Wells          |      3|   458|    26|NaN                                                                                                                                      |
|Riverside     |Indio                 |      4|  1606|  1269|NaN                                                                                                                                      |
|Riverside     |Jurupa Valley         |      4|  1329|   466|NaN                                                                                                                                      |
|Riverside     |La Quinta             |      6|  1102|  1882|NaN                                                                                                                                      |
|Riverside     |Lake Elsinore         |      4|  1183|  1080|NaN                                                                                                                                      |
|Riverside     |Menifee               |      8|  3906|  4147|NaN                                                                                                                                      |
|Riverside     |Moreno Valley         |      4|  2347| 13676|NaN                                                                                                                                      |
|Riverside     |Murrieta              |      5|  1913|  4446|NaN                                                                                                                                      |
|Riverside     |Norco                 |      6|  3029|   503|NaN                                                                                                                                      |
|Riverside     |Palm Desert           |      6|  1069|   221|NaN                                                                                                                                      |
|Riverside     |Palm Springs          |      4|   886|    65|NaN                                                                                                                                      |
|Riverside     |Perris                |      5|  2298|   683|NaN                                                                                                                                      |
|Riverside     |Rancho Mirage         |      6|   467|   465|NaN                                                                                                                                      |
|Riverside     |Riverside             |      5|  1955|  3040|NaN                                                                                                                                      |
|Riverside     |Riverside County      |      1|     0|   295|NaN                                                                                                                                      |
|Riverside     |San Jacinto           |      3|  2697|   799|NaN                                                                                                                                      |
|Riverside     |Temecula              |      4|  2050|   525|NaN                                                                                                                                      |
|Riverside     |Wildomar              |      3|   508|   445|NaN                                                                                                                                      |
|San Bernardino|Adelanto              |      2|   171|   564|NaN                                                                                                                                      |
|San Bernardino|Apple Valley          |      7|  1681|    38|NaN                                                                                                                                      |
|San Bernardino|Barstow               |      3|   602|    25|NaN                                                                                                                                      |
|San Bernardino|Big Bear Lake         |      5|   498|    38|NaN                                                                                                                                      |
|San Bernardino|Chino                 |      4|  2000|   130|NaN                                                                                                                                      |
|San Bernardino|Chino Hills           |      6|  1340|     9|NaN                                                                                                                                      |
|San Bernardino|Colton                |      4|   868|   251|NaN                                                                                                                                      |
|San Bernardino|Fontana               |      5|  2354|   473|NaN                                                                                                                                      |
|San Bernardino|Grand Terrace         |      1|    81|   186|NaN                                                                                                                                      |
|San Bernardino|Hesperia              |      6|  1260|  1289|NaN                                                                                                                                      |
|San Bernardino|Highland              |      3|  1165|   238|NaN                                                                                                                                      |
|San Bernardino|Loma Linda            |      5|  1240|   408|NaN                                                                                                                                      |
|San Bernardino|Montclair             |      3|   836|     3|NaN                                                                                                                                      |
|San Bernardino|Needles               |      3|   550|    13|NaN                                                                                                                                      |
|San Bernardino|Ontario               |      4|   982|    61|NaN                                                                                                                                      |
|San Bernardino|Rancho Cucamonga      |      4|  1142|     6|NaN                                                                                                                                      |
|San Bernardino|Redlands              |      5|  1022|   137|NaN                                                                                                                                      |
|San Bernardino|Rialto                |      5|  2828|    68|NaN                                                                                                                                      |
|San Bernardino|San Bernardino        |      1|     0|   555|NaN                                                                                                                                      |
|San Bernardino|San Bernardino County |      1|     0|    54|NaN                                                                                                                                      |
|San Bernardino|Twentynine Palms      |      4|   786|    23|NaN                                                                                                                                      |
|San Bernardino|Upland                |      3|   477|    20|NaN                                                                                                                                      |
|San Bernardino|Victorville           |      5|  2631|   378|NaN                                                                                                                                      |
|San Bernardino|Yucaipa               |      5|  1028|    10|NaN                                                                                                                                      |
|San Bernardino|Yucca Valley          |      4|   962|   265|NaN                                                                                                                                      |
|Ventura       |Camarillo             |      4|  1289|   218|NaN                                                                                                                                      |
|Ventura       |Fillmore              |      1|   292|   218|NaN                                                                                                                                      |
|Ventura       |Moorpark              |      4|   985|   218|NaN                                                                                                                                      |
|Ventura       |Ojai                  |      3|   548|   218|NaN                                                                                                                                      |
|Ventura       |Oxnard                |      5|  2657|  2754|NaN                                                                                                                                      |
|Ventura       |Port Hueneme          |      3|   648|   274|NaN                                                                                                                                      |
|Ventura       |Santa Paula           |      3|   519|   218|NaN                                                                                                                                      |
|Ventura       |Simi Valley           |      5|  1429|   767|NaN                                                                                                                                      |
|Ventura       |Thousand Oaks         |      3|  1193|    59|NaN                                                                                                                                      |
|Ventura       |Ventura               |      5|  1738|  1300|NaN                                                                                                                                      |
|Ventura       |Ventura County        |      1|     0|   276|NaN                                                                                                                                      |

## END Summary

