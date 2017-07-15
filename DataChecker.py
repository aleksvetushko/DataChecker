import json, io, csv

#load config data (array of table objects with expected values) from JSON file
def getConfig():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data

def checkData(table_name, table_config):
    with open(table_name, 'rb') as table_file:
        #TODO: make sure csv format is cross-platform, so far works on Mac
        table_data = csv.reader(table_file)
        
        date(table_data)
        for stats in table_config.values():
            for name, expected in stats.items():
                table_file.seek(0)
                if name == "mean":
                    mean(expected, table_data)
                elif name == "coverage":
                    coverage(expected, table_data)

def date(table_data):
    next(table_data) #start after row with variable names
    correct = True
    for row in table_data:
        #using 7/13/17 as sample expected date for now
        if row[0] != "7/13/17":
            print "ERROR! Expected date: 7/13/17. Actual date: " + row[0] + "."
            correct = False
    if correct == True:
        print "Dates are 7/13/17. Correct."
    
def mean(expected, table_data):
    sum = 0
    count = 0
    next(table_data)
    for row in table_data:
        sum += float(row[2])
        count += 1
    mean = sum/count
    if expected[0]-expected[1] <= mean <= expected[0]+expected[1]:
        print "Mean is " + str(mean) + ", within " + str(expected[1]) + " of " + str(expected[0]) + " Correct."
    else:
        print "ERROR! Expected mean: " + str(expected[0]) + " +/- " + str(expected[1]) + ". Actual mean: " + str(mean) + "."

def coverage(expected, table_data):
    count = 0
    next(table_data)
    for row in table_data:
        count += 1
    if expected[0]-expected[1] <= count <= expected[0]+expected[1]:
        print "Coverage is " + str(count) + ", within " + str(expected[1]) + " of " + str(expected[0]) + " Correct."
    else:
        print "ERROR! Expected coverage: " + str(expected[0]) + " +/- " + str(expected[1]) + ". Actual coverage: " + str(count) + "."

#main    
if __name__ == "__main__":
    config = getConfig()

    for table_config in config:
        table_name = table_config.keys()[0]
        print table_name + "\n"
        checkData(table_name, table_config)
        print "-----------------------------------------------------------"
        
