function [ciphertext] = encrypt(k,str)
% The function encrypts a string 'str' using a key 'k' via a Ceasar Cypher
% It iterates through every character in the string and moves it down by a 
% value k between 1 and 25

new_str = upper(str);

for i = 1:length(new_str)
    if (new_str(i) > 64 && new_str(i) < 91)
        new_str(i) = mod((new_str(i) - 65) - k, 26) + 65;
    else
        new_str(i) = new_str(i);
    end
    
    ciphertext = char(new_str);
    
end

end

% Test:
% encrypt(7,'A girl gives a man his own name')


 