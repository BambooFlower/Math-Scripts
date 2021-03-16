function [output] = score(k,str)
% The function counts the occurrences of common English words, encrypted 
% with key 'k' , in the string 'str'

dictionary  = {'THE','ARE','WAS','WERE','AND','THAT','HAVE','FOR','NOT','WITH','YOU'};
counter = 0;

for i = 1:length(dictionary)
    new_dictionary = encrypt(k,dictionary{i});
    check = length(strfind(str,new_dictionary));
    if check > 0
        counter  = counter + 1;
    end
end

output  = counter;

end

% Example:
% secret = 'D RDNC D RVN OCZ HJINOZM TJP OCDIF D VH.';
% score(5,secret) = 3
