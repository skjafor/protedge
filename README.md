palestine
=========

Data on Palestinian victims of Protective Edge (July-August 2014)

###Contents

* "Aug4" - data downloaded on August 4th, 2014
  * "raw" - downloaded
  * "parsed" - parsed
    * "alakhbar" - downloaded from http://english.al-akhbar.com/node/20528
    * "imemc" - downloaded from http://www.imemc.org/article/68429
    * "toi/toisrael" - downloaded from http://www.timesofisrael.com/fallen-idf-soldiers-in-operation-protective-edge/
* "Aug12" - as above, August 12, 2014
  * "combined" - highly processed files. In particular, any "_corrected" file has been corrected manually. "final.txt" is the final file
* "scripts for scraping" - python and R scripts that were used to create the final file, as well as some dictionaries that were needed for that (name-gender and placename)
* "summary" - html description of the results found in final.txt. The description should be on the relevant gh-page.


###Variables in the final file:
* date, ordinal day (starting from July 8th, 2014 as the first day of the operation), ethnicity;

* full name, first name, last name, name summary, age, sex, place of death, circumstances from the Al-Akhbar file;

Gender data was derived by running the first names through [here](http://www.indiachildnames.com/genderof.aspx) and [here](http://www.gpeters.com/names/baby-names.php).

Name summary is a numerical shorthand for name, defined as ((ord(last_name_low[0])-96)*10+(ord(last_name_low[1])-96)), where ord(x)=ASCII value of x. (ord(a)-96)=1

* full name, name summary, age, sex, place of death, circumstances from the IMEMC file - column names starting from (IMEMC_);

* combined-record name summary, age, sex, and place of death; IMEMC records, which are supposed to be more correct, take precedence over Al-Akhbar records;

* age group, defined as: "Unknown", "Child" (<=14), "Young adult" (<=24), "Adult" (<=54), "Elderly";

* simulated ages and name summaries, for the plots where I wanted to add the "unidentified" records.