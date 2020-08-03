function [msg,k] = attack(str)
% The function performs a dictionary based attack on 
% an encrypted message 'str'

check = zeros(25, length(str));

for i = 1:25
    check(i,:) = score(i,str);  
    highest = max(check);
    if check(i,:) == highest
        key = i;
    end
end

msg = decrypt(key,str);
k = key;

end

% Example:
% secret = 'D RDNC D RVN OCZ HJINOZM TJP OCDIF D VH.'
% [msg,k] = attack(secret)

% Second Example (Part 6):
% secret = 'YMNX NX F MJQQ TK F HTZWXJ'
% In this case, none of the words in the secret are in our dictionary
% It's best to use alldecryptions(secret)