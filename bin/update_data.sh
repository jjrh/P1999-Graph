#/bin/bash 

python ~/CODE/project1999_serverPopulation/p99_serverstatus.py
p=`cat ~/CODE/project1999_serverPopulation/plot_test`
pop=`cat  ~/CODE/project1999_serverPopulation/currentPop`
echo $p >  ~/CODE/project1999_serverPopulation/plot_tmp
echo 'set title  "Current Population: '$pop'"' ';' >> ~/CODE/project1999_serverPopulation/plot_tmp
echo 'plot "/home/jjrh/CODE/project1999_serverPopulation/p99_server_pop.dat" using 2:3 title "Project 1999 Blue Server Population" with lines;' >> ~/CODE/project1999_serverPopulation/plot_tmp
gnuplot ~/CODE/project1999_serverPopulation/plot_tmp

