function fisher()

close all

options = odeset('RelTol',1e-6);
figure(1);

u=0:.1:1;
plot(u,0*u,'g');hold on;
plot(u,u.*(1-u),'g');
plot(u,.5*u.*(1-u),'b');


for u=[0:.1:.9,.91:.01:.99,.9999]
    [~,Y] = ode45(@rigid,[0 -10], [u,0*u],options);
    plot(Y(:,1),Y(:,2),'r');
    [~,Y] = ode45(@rigid,[0 .2], [u,0*u],options);
    plot(Y(:,1),Y(:,2),'b');
    [~,Y] = ode45(@rigid,[0 -10], [u,u.*(1-u)],options);
    plot(Y(:,1),Y(:,2),'r');
    [~,Y] = ode45(@rigid,[0 .2], [u,u.*(1-u)],options);
    plot(Y(:,1),Y(:,2),'b');
end

hold off
end



function dy = rigid(~,y)
dy = zeros(2,1);    
dy(1) = y(2) ;
dy(2) = 2*y(2) - y(1)*(1- y(1));
end



