set multiplot layout 2,2

plot 'xising2D' us 1:2 title 'M' w l
plot 'xising2D' us 1:3 title 'E' w l
plot 'xising2D' us 1:4 title 'chi' w l
plot 'xising2D' us 1:5 title 'C' w l

unset multiplot
