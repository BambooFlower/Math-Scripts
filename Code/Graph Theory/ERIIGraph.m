function A = ERIIGraph(N,rho)
% Erdos-Renyi Type II Random Graph generator 

R = triu(rand(N),1);
R = R + transpose(R) + eye(N);
A = sparse(R<rho);

end

%%% Show degree distribution for c=5, N1 = 100 ('o') and N2 = 1000 ('s')
%%% We also superimpose a Poisson Distribution plot 

% c = 5;
% N1 = 100;
% A1 = ERIIGraph(N1,c/N1);
% N2 = 1000; 
% A2 = ERIIGraph(N2,c/N2);
% drange = (0:20);
% pd1 = hist(sum(A1),drange)/N1;
% pd2 = hist(sum(A2),drange)/N2;
% plot(drange,pd1,'o',drange,pd2,'s',...
%     drange,exp(-c)*c.^ (drange)./factorial(drange))

