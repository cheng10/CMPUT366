plot "avgret.dat" using 1:2 title "Average return obtained by Sarsa after n-th episode", \
     "avgsteps.dat" using 1:2 title "Average steps obtained by Sarsa after n-th episode"
set xlabel "Episode number (n)"
set ylabel "Averages"
set terminal postscript eps enhanced color
set output "learningcurve.eps"
replot
