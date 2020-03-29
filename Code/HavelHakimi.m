function is_graphical = HavelHakimi(d)
% Check if a Sequence is graphical

d = sort(d,'descend');
% if d is full of zeros, it is graphical (empty graph)
if nnz(d) == 0
    is_graphical = true;
    % if d has a negative entry it is not graphical
elseif d(end) < 0
    is_graphical = false;
    % if d(1) is too large, d is not graphical
elseif d(1) > length(d)-1
    is_graphical = false;
else
    is_graphical = HavelHakimi([d(2:d(1)+1)-1,d(d(1)+2:end)]);
end

end
        
        