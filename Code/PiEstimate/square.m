function square(l)
% It plots a square with the lower left vertex at the origin and side of
% lenght l

vertex1 = [0,0];
vertex2 = [0,l];
vertex3 = [l,l];
vertex4 = [l,0];


hold on
plot([vertex1(1),vertex2(1)],[vertex1(2),vertex2(2)],'b')
plot([vertex2(1),vertex3(1)],[vertex2(2),vertex3(2)],'b')
plot([vertex3(1),vertex4(1)],[vertex3(2),vertex4(2)],'b')
plot([vertex4(1),vertex1(1)],[vertex4(2),vertex1(2)],'b')
hold off

end

