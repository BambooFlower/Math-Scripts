function [DFact] = DFactorialRec(n)
% Recursive implementation of a double factorial function
% It takes an integer number n as input and calculates n!!

if n == 0
    value = 1;
elseif n == 1
    value = 1;
else
    value = n*DFactorialRec(n-2);
end

DFact = value;

end

