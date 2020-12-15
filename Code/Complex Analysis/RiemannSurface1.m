% Rieman surface for f(z) = sqrt(z)


% create a matrix of complex inputs
r = (0:1:15)';    

theta = pi*(-2:0.05:2);
z = r*exp(1i*theta);

% calculate the complex outputs
w = sqrt(r)*exp(1i*theta/2);

figure('Name','Graphique complexe','units','normalized','outerposition',[ 0.08 0.1 0.8 0.55]);
subplot(121)

% visualize the complex function using surf
surf(real(z),imag(z),real(w),imag(w))    
xlabel('Real(z)')
ylabel('Imag(z)')
zlabel('Real(u)')
title('Plot of the Real Component')

% gradient from blue to red
colormap jet   
axis tight


% visualize the complex function using surf
subplot(122)
surf(real(z),imag(z),imag(w),real(w)) 

xlabel('Real(z)')
ylabel('Imag(z)')
zlabel('Imag(v)')
title('Plot of the Imaginary Component')

% gradient from blue to red
colormap jet      
axis tight
