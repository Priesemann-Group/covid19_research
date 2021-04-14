%%%% Fig 5: increasing freedom over time %%%% 

clear all
close all
clc

%% Parameters 
R0          = 3.3;
M           = 1e6;          % Total population
I0          = M*200/1e6;    % initial infections
xi          = 0.32;         % Asymptomatic ratio
tc          = 4;            % latency period
eta         = 0.66;         % tracing efficiency
tau         = 2;            % tracing delay
lambda_s    = 0.25;         % symptomatic testing/self reporting
lambda_r    = 0;            % random testing | screening
Gamma       = 0.1;          % recovery rate
nu          = 0.075;        % isolation factor
epsilon     = 0.05;         % leak              The idea behind this is to set kISOL = 1/3 k lockdown, and 2/3 of contacts traced
Phi0        = 1;            % external contagion
nmax        = M*50/1e6;     % tracing limit
Phild       = Phi0/10;      % Influx during lockdown
tau_gen     = 4;            % generation time
% parameters after threshold
lambda_s2   = 0.1; 
lambda_r2   = 0;
xim = 1-xi;

%% Parameters equilibrium

Neq         = 10;
Neq_hosp    = 250;
uptake      = 0.7;
kappa_eff   = 0.4; 

%% Critical hidden reproduction number

Rtcrit      = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2)
Rtcrit_hosp      = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r2,0,epsilon,R0),2)

%% estimation of the time for the vaccine roll-out

t           = -5*7:1:40*7;
t_start     = 0;
tau1        = 220;
tau2        = 150;
t_end       = t_start + tau1; 
t_ref       = t_start + tau2;
b           = -0.025;
a           = uptake*b*M/log((1+exp(-b*tau2))/(exp(-b*tau1)+exp(-b*tau2)));
V           = [t_start;t_end;kappa_eff;a;b;t_ref];
f           = kappa_eff*acumula(t,dvacdt(t,V))/(M*V(3));

RtH =   Rtcrit./(1-f) - Phi0/Neq;
RtH_hosp =   Rtcrit_hosp./(1-f) - Phi0/Neq_hosp;

%% Plot
load('DefColors.mat')
red = [1 0 0]; blue = [0 0 1]; green = [0 1 0];
BW = 0.025;
BWparam = 0.025;
fact_axis = 1.2;
fact_label = 1.3;
fact_curva = 1;
siz = 15;
W = 8; H = 6;


ax = backplot('Daily new cases');
plot(t/7,RtH,'Color',Default(1,:),'LineWidth',3*fact_curva)
hold on
plot(t/7,RtH_hosp,'Color',Default(2,:),'LineWidth',3*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
ylabel('$R_t^{\rm crit}(f)$','interpreter','latex','FontSize',15*fact_label)
ylim([0.5 4.5])
xlim([t(1) t(end)]/7)
xlabel('time [weeks]','interpreter','latex','FontSize',15*fact_label)
ax.TickLabelInterpreter='latex';

