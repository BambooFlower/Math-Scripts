function [plaintext] = decrypt(k,str)
% The function dencrypts a string 'str' using a key 'k' via a Ceasar Cypher
% It does the opposite of the function 'encrypt'
% For semplicity it only handles upper case letters

plaintext = encrypt(-k,str);

end

% Example:
% decrypt(12,'QVOCG WGBH O DWH. QVOCG WG O ZORRSF.')
