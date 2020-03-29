function [out] = TriChess(n)
% Calculates the number of possible triple-pairings in the first round of a Tri-Chess tournament with n = 3k players

if n == 3
    value = 1;
elseif mod(n,3) ~= 0
    disp("You need at least a multiple of 3 to be able to assign all players")  
    return
else
    value = (1/2)*(n-1)*(n-2)*TriChess(n-3);
end

out = value;

end

