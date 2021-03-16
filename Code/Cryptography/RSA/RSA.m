classdef RSA
% main class used for RSA encryption
    
    properties
        public_key_pt1
        public_key_pt2
        private_key
    end
    
    methods
        
        % Generator function
        function K = RSA
            size = 53;
            i = ceil((size/2) + rand*(4));
            j = size - i;
            p = generate(i);
            q = generate(j);
            N = p*q;
            A = 65537;
            n = (p-1)*(q-1);
            [G,~,M] = gcd(A,n);
            a = (G - M*n)/A;
            K.public_key_pt1 = sym(N);
            K.public_key_pt2 = sym(A);
            K.private_key = sym(a);
        end
        
        function disp(K)
            fprintf('Public key part 1: %d \n', K.public_key_pt1)
            fprintf('Public key part 2: %d \n', K.public_key_pt2)
            fprintf('Private key : %d \n', K.private_key)
        end
        
        function c = encrypt(K,m)
            if m < K.public_key_pt1
                c = expMod(sym(m), K.public_key_pt2, K.public_key_pt1);
            else
                disp('The message is longer than N')
            end      
        end
        
        function m = decrypt(K,c)
            m = expMod(c, K.private_key, K.public_key_pt1);
        end
    end
    
end

