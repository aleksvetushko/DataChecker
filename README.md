# DataChecker

Prototype of DataChecker program. 

Program opens a config.json file, which contains an array of objects representing each table and its configuration.
For each of these tables, a csv file corresponding to the table is opened (or exception is raised).
For each table, iterate through its corresponding stats in config.json. 
For each stat, compare the expected values (in config.json) to the actual values (calculated/found in csv).
Print description (error or correct) to console for each stat.
