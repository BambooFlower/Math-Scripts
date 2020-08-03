function a = expMod(x,e,m)
% Modular Exponentiation
%   expMod(x,e,m) computes x^e mod m by the binary method:
%   x^2e'   mod m  =    (x^2 mod m)^e' mod m
%   x^2e'+1 mod m  =  x*(x^2 mod m)^e' mod m
%   e,m must be nonnegative integers

% Base case: exponent 0
if e == 0
    a = 1; 
% Base case: exponent 1
elseif e == 1 
    a = x ; 
elseif mod(e,2) == 0    % Recursion: e even
    a = expMod( mod(x*x,m) , e/2 , m);
else                    % Recursion: e odd
    a = mod(x * expMod( mod(x*x,m) , (e-1)/2 , m) , m);
end
    
end
