palestine
=========

Data on Palestinian victims of Protective Edge (July-August 2014)

###Contents

* "data_raw_Aug4" - data, downloaded on August 4th, 2014
  * "raw_Aug4_alakhbar.txt" - downloaded from http://english.al-akhbar.com/node/20528
  * "raw_Aug4_imemc.txt" - downloaded from http://www.imemc.org/article/68429
  * "raw_Aug4_toi.txt" - downloaded from http://www.timesofisrael.com/fallen-idf-soldiers-in-operation-protective-edge/
* "scripts raw scrape" - scripts (Python) to scrape the files TODO: alter so that the download+scraping is done automatically. Already done for "alakhbar".
* "data parsed" - data parsed by the Python scripts
* "combined_akhbar_toisrael.txt" - a single file with the parsed data for Palestinians and Israeli soldiers. 
* "script_draw.R" - R script to process data and draw plots
* "plots" - plots
  * "p_protedge_sim_noisraeli.png" - scatterplot, with simulated data, no datapoints for Israeli soldiers
  * "p_protedge_sim_plusisraeli.png" - scatterplot, with simulated data, datapoints for Israeli soldiers
  * "p_protedge_sim_noisraeli_boxplot.png" - boxplot, no data for Israeli soldiers
  * "p_protedge_nosim_noisraeli_hexbin.png" - hexbin plot, no simulated data, no datapoints for Israeli soldiers
  * "p_protedge_sim_noisraeli_hexbin.png" - hexbin plot, with simulated data, no datapoints for Israeli soldiers
  * "p_protedge_nosim_plusisraeli_cumsum.png" - cumulative deaths, datapoints for Israeli soldiers


###Gender data
Name-gender correspondence was established from http://www.indiachildnames.com/genderof.aspx?name= and then from http://www.gpeters.com/names/baby-names.php?name= . The gender of 12 names could not be established.


###Variables in the parsed files:
* Date
* Ordinal_day - day of the operation
* Full_name
* First_name (derived from Full_name)
* Last_name (derived from Full_name)
* Age
* Ethnic_group ("Palestinian" "Israeli")
* Sex (derived from First_name, see above)
* Name_summary (derived from Last_name): a summary of the name, for plotting name-vs.-age etc., graphs: ((ord(last_name_low[0])-96)*10+(ord(last_name_low[1])-96))
* Age_group: "0" if unknown, "1" if <=14; "2"  if >14 and <=24, "3" if >24 and <=54, "4" if >54. (Unknown, child, young adult, adult, elderly.) Cf. http://www.indexmundi.com/gaza_strip/demographics_profile.html for demographics of the Gaza strip.
* Name_unknown: "1" if name unknown
* Age_unknown: "0" if age unknown
* Circumstances: for Al-Akhbar and IMEMC data, whatever was written in the death listing.


TODO (apart from the mentioned above):
* Tidy up the data AND the scripts.
* IMEMC and Al-Akhbar (and [Al-Jazeera](http://www.aljazeera.com/news/middleeast/2014/07/gaza-under-seige-naming-dead-2014710105846549528.html), for that matter, use different Arab transliterations. Try to match up the IMEMC and Al-Akhbar data.
* Create the markdown.
