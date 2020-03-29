function findPi(dart)
% Estimates the value of pi using Monte Carlo simulations 
% To estimate the value of pi, we use the prodecudere proposed by Buffon
% and Laplace of throwing darts at random at a circle inscribed into a
% square. We then compare the number of darts that are inside the circle to
% those that are outside the circle

% Ideal Case: findPi(1000)

close all

p_size = 0.25;
dcolor = [0,0,0];

% Estimates the x & y coordinates of an array of random numbers
x = rand(1,dart);
y = rand(1,dart);figure;


% Plots the darts, the circle and the square
figure;
circle(1/2,1/2,1/2)
square(1)
hold on
plot(x,y,'*','MarkerSize',p_size,'MarkerEdgeColor',dcolor)
title('Estimate of pi')
hold off


% Counter for darts inside the circle
dartCircle = 0;
estimate = zeros(1,dart);

for k = 1:dart
    if (x(k))^2 + (y(k))^2 < 1
        dartCircle = dartCircle + 1;
    end
    estimate(k) = 4*dartCircle/k;
end


% Plots the pi estimate against the number of darts
figure;
plot(1:dart,estimate,'b')
piValue = refline([0, 3.14159]);
piValue.Color = 'r';
legend('Estimate of pi','Value of pi')
title('pi estimate against number of darts')
xlabel('Number of darts')
ylabel('pi estimate')

% Final Value 
guess = 4*dartCircle/dart;
value = ['The estimate of pi after ',num2str(dart),' trials is: ', num2str(guess)];
disp(value)

end

