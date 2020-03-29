function circle(x,y,r)
% It plots a circle with center (x,y) and radius r

close all

hold on
th = 0:pi/50:2*pi;
xunit = r * cos(th) + x;
yunit = r * sin(th) + y;
plot(xunit, yunit,'r');
hold off

end