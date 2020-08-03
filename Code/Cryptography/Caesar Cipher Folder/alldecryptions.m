function [text] = alldecryptions(str)
% The function lists the 25 potential decryptions of an encrypted message
% by using a cell array

cell_array = zeros(25,length(str));

for i = 1:25
    cell_array(i,:) = decrypt(-i,str); 
end

text = char(cell_array);

end

% Example:
% alldecryptions('KROG WKH GRRU!')