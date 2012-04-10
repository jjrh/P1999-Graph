#!/bin/bash
d=$(date +%F)
PROG_PATH=/home/jjrh/CODE/project1999_serverPopulation/
cat $PROG_PATH/p99_server_pop.dat >> full.dat
mv /home/jjrh/CODE/project1999_serverPopulation/p99_server_pop.dat /home/jjrh/CODE/project1999_serverPopulation/old/$d.dat



