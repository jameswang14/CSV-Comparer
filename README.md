# CSV-Duplicate-Remover
Simple python script that compares two csv files and outputs rows that appear in the second csv file but not the first. 

Originally built as a simple alternative to persistent storage for webscraping instead of setting up a database. 

First CSV File - Master File
Second CSV File - Most recent Crawl

Any rows that appear in the second file but not the first will be appended to the output (third) csv file. 
