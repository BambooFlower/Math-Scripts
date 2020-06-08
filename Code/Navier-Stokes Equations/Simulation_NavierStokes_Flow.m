function alpha = Simulation_NavierStokes_Flow(l,L,lambda_max)
% Computes the solution of the Navier-Stokes equations 
% 
% Instructions for use:
% Run Simulation_Navier-Stokes_Flow first to get the simulated parameters
% which will be saved in the Data_NavierStokes_Flow.mat file, then run 
% Graph_Flow_Navier-Stokes for an animated visualization 
%
% Inputs:
% l: Height of the box containing the fluid
% L: Width of the box containing the fluid
% lambda_max: Number used to compute the degrees of freedom, the higher it
% is the better the simulation
%
% Example:
% Simulation_NavierStokes_Flow(5,4,80)

[nbr A lambdass Nss Pss] = ODE_rhs(l,L,lambda_max); %#ok<NASGU>
%initializing data randomly
alpha0 = zeros(1,nbr);
alpha0(1:3) = 2.5*rand(1,3);

%viscosity and viscosity matrix
nu = 0.03;
D = nu*diag(lambdass);
rel_time1 = 0;

disp('Solving now ODE...')
disp('0%------20%-------40%-------60%-------80%------100%')

Tmax = 100;
Time = linspace(0,Tmax,900);
[T, alpha] = ode113(@right_hand_side,Time,alpha0);

rel_time1 = 0;

    function dy = right_hand_side(t,y) %#ok<INUSL>
        % display remaining time
        rel_time = floor((t/Tmax)*50);
        string = repmat('|',1,rel_time-rel_time1);
        rel_time1 = max(rel_time,rel_time1);
        fprintf(1,string)
        
        dy = zeros(nbr,1);
        for k=1:nbr
            dy(k) = -0.3*y.'*A{k}*y;
        end
        % Adding viscosity (remove this line for Euler flow)
        dy = dy-nu*D*y; 
    end

% Saving the data
save('Data_NavierStokes_Flow','nbr','l','L','T','lambda_max',...
    'alpha0','alpha','lambdass','Nss','Pss')

fprintf('\n\n')
disp('Solution saved in file: data_euler_flow.mat')
disp('Use function graph_flow_euler.m to make a video')
end


