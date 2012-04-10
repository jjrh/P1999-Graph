
hour_list = []
average = 0
def get_average(fileLoc):
    alltime_total = 0
    alltime_count = 0
    alltime_average = 0
    
    hourly_total = 0
    hourly_count = 0
    hourly_average = 0
    hourly_list = []
    hourly_current = None
    with open(fileLoc, "r") as f:
        for l in f:
            s = l.split()
            hour = s[1].split(":")
            if hourly_current == None:
                hourly_current = hour[0]

            if hourly_current != hour[0]:
                hourly_average = hourly_total/hourly_count
                entry = []
                entry.append(hourly_current)
                entry.append(hourly_average)
                hourly_list.append(entry)
                hourly_average = 0
                hourly_total = 0
                hourly_count = 0
                hourly_current = hour[0]
            else:
                hourly_count += 1
                hourly_total += int(s[2])
                
            
            alltime_total += int(s[2])
            alltime_count += 1
    if hourly_count == 0:
        hourly_count = 1

    hourly_average = hourly_total/hourly_count
    entry = []
    entry.append(hourly_current)
    entry.append(hourly_average)
    hourly_list.append(entry)
    

    if alltime_count != 0:
        alltime_average = alltime_total/alltime_count

    global hour_list
    hour_list = hourly_list

    global average
    average = alltime_average
    
    return alltime_average


def print_pretty():
    count = 0
    print "+-------------------------------+"
    for entry in hour_list:
        count += 1
        print "|\t" + str(entry[0]) + "\t|\t", str(entry[1]) + "\t|"
    print "+-------------------------------+"
        
fileloc = "/home/jjrh/CODE/project1999_serverPopulation/p99_server_pop.dat"

get_average(fileloc)
print_pretty()
print "| OVERALL AVERAGE:", str(average ), "\t\t|"
print "+-------------------------------+"
