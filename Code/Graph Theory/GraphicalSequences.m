function gs = GraphicalSequences(n)
% Count the number of graphical sequences of length n

% make an array of all decreasing sequences in {0,...,n-1}^n using the
% recursive function defined below
S = seq(n,n-1);
gs = 0;
% test each descreasing sequence
for k = 1:size(S,1)
    if HavelHakimi(S(k,:))
        gs = gs+1;
    end
end

end


function S = seq(n,m)
% Make an array of decreasing integer sequences in {0,...,m}^n

% length 1 sequences are just the numbers 0 to m
if n == 1
    S = (0:m)';
else
    % find all sequences that are one unit shorter (length n-1)
    T = seq(n-1,m);
    % container for sequences of length n
    S = [];
    for k = 1:size(T,1)
        % find a smaller number d to go on the end
        for d = 0:T(k,n-1)
            % extend it by adding d to the end, then
            % include it as a new row in S
            S = [S;T(k,:),d];
        end
    end
end

end