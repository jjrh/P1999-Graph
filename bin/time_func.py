import time
import os


import p1999_pop_config

"""
This program reads everything in the old directory.
'PATH' is the location to the 'old' directory.

All we do is read the file, switch the format to unix time,
then output one large file with the time.

There was a problem with some of my files - at some point when I
deployed this on another server the time was different. By the time
I noticed this and changed it, some values were out of wack. It's
not obvious which ones they were so I did a sort.

The code is fairly straight forward,
I read the file, double check ot make sure
the file i'm writing all the values to (ALL_TIME.dat)
doesn't get included.

1. I split the line by.
2. I find where it's time and where it's date and get make that into a string I can work with
	(note, this could be done with the formating of time.strtime() )
3. make the time struct, with time.strptime()
4. Convert it to unix time.
	I do this in a try, so that I can deal with any problems with formating - like if there was a bad value
5. Here is where some explaination is a bit more useful,
	Because like I said, some data was mucked up, I add it to a list called dateList
        I create a parallel list called popList.
        The issue here is that some of the data will be wrong because I can't do a proper sort with the pop

        I added 3 methods of writeing do deal with this.
        	1. Standard unsorted. (if the data is fine)
                2. time only sort. (may get incorrect values)
                3. Tuple storted, This is the best way if the values are wrong, I create a tuple with only two things in in and sort that.
        You can use these by setting WRITE_TYPE to the type you want.
		SORT_TYPES = {'unsorted':1,'listSorted':2,'tupleSorted':3}
		WRITE_TYPE = SORT_TYPES['tupleSorted']

"""



bigList = []


bigestTime = 0
dateList = []
popList = []

tupleList = []

Count = 0
PATH = "/home/jjrh/CODE/project1999_serverPopulation/old/"
for f in os.listdir(PATH):
    if("ALL_TIME" in f):
        pass

    else:
        for line in open(PATH+f,'r'):
            l = line.split()
            data = None
            timeString = []
            for c in l:
                if(':' in c):
                    for i in c.split(':'):
                        timeString.append(i)

                if('-' in c):
                    for i in c.split('-'):
                        timeString.append(i)


                if('-' not in c) and (':' not in c):
                    data = c
            try:
                TS = timeString[0] + " " + timeString[1] + " " + timeString[2] + " " + timeString[3] + " " + timeString[4] + " " + timeString[5]
                t = time.strptime(TS, "%Y %m %d %H %M %S")

                if(data != None):
                    bigestTime = time.mktime(t)
                    bigList.append([time.mktime(t),data])
                    dateList.append(time.mktime(t))
                    popList.append(data)

                    tupleList.append((time.mktime(t),data))
                
        #
            except:
                continue
               # print line
               # for i in TS:
               #     print type(i)
                #print Count,"--> ",timeString, len(timeString)

            Count+=1



FILE = open(PATH+"ALL_TIME.dat", 'w')
dateList.sort()
i = 0



tupleSorted = sorted(tupleList, key=lambda item: item[1])
print tupleSorted



SORT_TYPES = {'unsorted':1,'listSorted':2,'tupleSorted':3}

WRITE_TYPE = SORT_TYPES['tupleSorted']


if(WRITE_TYPE == 1):
    for item in bigList:
        FILE.write(str(item[0]) + "    " + str(item[1]) + "\n")
        i+=1
        
if(WRITE_TYPE == 2):
    for item in bigList:
        FILE.write(str(dateList[i]) + "    " + str(item[1]) + "\n")
        i+=1

if(WRITE_TYPE == 3):
    for item in tupleSorted:
        FILE.write(str(item[0]) + "    " + str(item[1]) + "\n")


FILE.write("#END")
FILE.close()
#   2012-04-10 00:01:00
