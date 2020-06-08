function HeatEquation()
% Create and solve the homogeneous heat equation
% We then create an animation showing the behavior of the heat equation
% We use MATLAB PDE package to create the PDE

thermalmodel = createpde('thermal','transient');

R1 = [3;4;-1;1;1;-1;-1;-1;1;1];
C1 = [1;0;0;0.4];
C1 = [C1;zeros(length(R1) - length(C1),1)];
gd = [R1,C1];
sf = 'R1+C1';
ns = char('R1','C1')';
g = decsg(gd,sf,ns);

geometryFromEdges(thermalmodel,g);

% Properties of the Heat Equation
thermalProperties(thermalmodel,'ThermalConductivity',1,...
    'MassDensity',1,...
    'SpecificHeat',1);

% Initial and Boundary Conditions:
thermalIC(thermalmodel,0);
thermalIC(thermalmodel,1,'Face',2);
thermalBC(thermalmodel,'Edge',1:4,'Temperature',0);

% Mesh size and Frame Rate 
msh = generateMesh(thermalmodel);
NumberFrames = 20;
tlist = linspace(0,0.1,NumberFrames);
result = solve(thermalmodel,tlist);

T = result.Temperature;

figure(1)
for j = 1:NumberFrames
    pdeplot(thermalmodel,'XYData',T(:,j),'ZData',T(:,j))
    colormap jet
    title('3D Animation of the Heat Equation')
    grid on
    axis([-1 1 -1 1 0 1]);
    Mv(j) = getframe;
end

HeatEquation()

end

