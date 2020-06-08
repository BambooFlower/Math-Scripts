function [nbr A lambdass Nss Pss] = ODE_rhs(l,L,lambda_max)
% Numerical Differential equation solver

disp(['Computing right-hand-side of the ODE...']) %#ok<NBRAK>

% Some variables
u1 = [1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0];
u2 = [0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0];
u3 = [0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0];
u4 = [0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1];
v1 = [1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0];
v2 = [0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0];
v3 = [0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0];
v4 = [0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1];
k = zeros(1,4);
r= zeros(1,4);
jac = 1/2*(l*L)^(3/2)/pi;
Ma =                [-1  1;...
    1 -1;...
    1  1;...
    -1 -1;...
    1 -1;...
    -1  1;...
    -1 -1;...
    1  1;...
    -1 -1;...
    1  1;...
    1 -1;...
    -1  1;...
    1  1;...
    -1 -1;...
    -1  1;...
    1 -1];
rel_time1 = 0;

% Compute the number of modes
N = (1:150)'*ones(1,150);
P = N';
lambda = N.^2./l^2+P.^2./L^2; %eigenvalues of the problem
I = find(lambda<lambda_max);
nbr = length(I);
disp(['Number of modes (degrees of freedom): ',num2str(nbr)]);

lambdas = lambda(I);
Ns = N(I);
Ps = P(I);
clear N
clear P
clear lambda
[lambdass IX] = sort(lambdas);
Nss = Ns(IX);
Pss = Ps(IX);

A = cell(nbr);
Tmax = nbr^2;

disp('Computation in progess...')
disp('0%------20%-------40%-------60%-------80%------100%')

% Main loop
for cont0 = 1:nbr
    A{cont0}=sparse(nbr,nbr);
end
for cont1 = 1:nbr
    n1 = Nss(cont1);
    p1 = Pss(cont1);
    for cont2 = 1:nbr
        
        % Display remaining time
        rel_time = floor((cont1*cont2/Tmax)*50);
        string = repmat('|',1,rel_time-rel_time1);
        rel_time1 = max(rel_time,rel_time1);
        fprintf(1,string)
 
        n2 = Nss(cont2);
        p2 = Pss(cont2);
        ind_guess = [n2-n1,p2-p1;...
            n2-n1,p2+p1;...
            n2-n1,-p2+p1;...
            n2+n1,p2-p1;...
            n2+n1,p2+p1;...
            n2+n1,-p2+p1;...
            -n2+n1,p2-p1;...
            -n2+n1,p2+p1;...
            -n2+n1,-p2+p1];
        for cont3 = 1:9
            cont4 = find(Nss == ind_guess(cont3,1) & Pss == ind_guess(cont3,2));
            if ~isempty(cont4)
                n3 = Nss(cont4);
                p3 = Pss(cont4);
                m1 = n3*p2;
                m2 = n2*p3;
                k(1) = n3-n2+n1;
                k(2) = n3-n2-n1;
                k(3) = n3+n2-n1;
                k(4) = n3+n2+n1;
                r(1) = p3-p2+p1;
                r(2) = p3-p2-p1;
                r(3) = p3+p2-p1;
                r(4) = p3+p2+p1;
                a = (Ma*[m1; m2]).';
                
                K = pi*ones(1,4);
                R = K;
                K(k~=0) = 0;
                R(r~=0) = 0;
                b = diag(K(1)*u1+K(2)*u2+K(3)*u3+K(4)*u4);
                c = b*(R(1)*v1+R(2)*v2+R(3)*v3+R(4)*v4).';
                
                multi = 1/sqrt((n3^2*L^2+l^2*p3^2)*(n2^2*L^2+l^2*p2^2)*...
                    (n1^2*L^2+l^2*p1^2));
                val_propre = (n2^2/l^2+p2^2/L^2);
                A{cont1}(cont4,cont2) = a*c*multi*val_propre*jac;
                
            end
        end
    end
end
fprintf('\n\n')
end
