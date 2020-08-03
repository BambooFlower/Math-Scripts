function output = generate(s)
% Given a size s in bits, generates a random prime number between 2^(s?1) and 2^s ? 1

p = 0;

while isprime(p) == 0
    a = 2^(s-1);
    b = 2^s  - 1;
    p = floor(a + b*rand);
end

output = p;

end

