set xdata time
set timefmt "%H:%M:%S"
set yrange [0:]
set terminal png nocrop enhanced font verdana 8 size 800,600
set output "/home/jjrh/CODE/project1999_serverPopulation/p99_graph.png"
plot "/home/jjrh/CODE/project1999_serverPopulation/p99_server_pop.dat" using 2:3 with lines
