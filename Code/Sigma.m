function [output] = Sigma(n)
% Implementation of Liebniz formula to approximate the value of pi
% Use a big value of n for a better approximation

value = 0;

for j=0:n
    value = value + ((-1)^(j))*(1/(2*j+1));
end

output = 4*value;

end


