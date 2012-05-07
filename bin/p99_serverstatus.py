import urllib2
import re
import datetime

ur = urllib2.urlopen("http://www.eqemulator.org/index.php?pageid=serverinfo&worldid=787")

arr = ""
count = 0
flag = False
for i in ur:
    if re.search('<tr><td width="150" valign=top>\&nbsp;<i>Players Online:</i></td>', i):
        flag = True
        
    if flag and count < 3: 
        arr = arr + i.rstrip()
        count += 1

numbers = []
arr = arr.split()
for i in arr:
    s= i.strip('<td><tr><i></;Playerswidth="Online:&nbspvalign=to')
    s= s.strip(' ')
    if len(s) > 0:
        numbers.append(s)


dt = datetime.datetime.now()
pop = numbers[1]

timeof =  dt.strftime("%Y-%m-%d %H:%M:00")


with open("/home/jjrh/CODE/project1999_serverPopulation/p99_server_pop.dat", "a") as f:
    f.write(timeof + "\t" + str(pop) + "\n")

f =  open("/home/jjrh/CODE/project1999_serverPopulation/currentPop", "w")
f.write(str(pop))
f.close()
