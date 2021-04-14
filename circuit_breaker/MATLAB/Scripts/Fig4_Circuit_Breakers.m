%%% Figure 2 %%%

clear all
close all
clc

%% Timeframe and initial conditions

ti = -30;     
tmin = -5*7;
tmax = 30*7;%360;
tf = 360;   
tspan = [ti tf];
lags = 2;
t1 = 0;
D_LD = 2*7;
t2 = t1+D_LD;
D = 7;
delay = 0;

%% Default pre- and during-lockdown settings
R0      = 3.3;
Rt      = 0.8*R0;
Rtld    = 0.25*R0; 
mode    = 1;          % [0 1] 1=TTI limit, 0=Hospital limit
Thrs1   = 250;       % Hospital alarm threshold (in terms of cases)

%% Mild contact reduction
%Rtald   = 0.80*R0;  
%% Moderate contact reduction
%Rtald   = 0.60*R0;  
%% Strong contact reduction
Rtald   = 0.40*R0; 


%% para ploteo

Umbral  = 1000;
Alim = 6e4;
Aclim = 5e4;
Elim = 5e4;
Nlim = 0.5e3;         

%% Parameters 

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

%% second order parameters

xim = 1-xi;
Rtcmax = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2);
Rtcmax2 = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r2,0,epsilon,R0),2);

%% Initial condition

% x0 = [S ET EH T H Hs R]
x0      = zeros(1,7);
x0(4)   = I0; x0(5) = x0(4); x0(6) = xim*x0(5); x0(2:3) = x0(4:5);
x0(1)   = M-sum(x0(2:end))+x0(6);
fun = @(x) syst_equilib(x,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,epsilon,nmax,Phi0);
xeq = fsolve(fun,x0(2:end-1));
phi = xeq(5)/xeq(4);

%% Determination of start of the lockdown (day zero) and reorganization of the days
options = ddeset('RelTol',1e-9,'AbsTol',1e-9);

sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
[~,Nobs_rep,~,~,ts,Neqcrit0] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
[~,id] = max(Nobs_rep>=Neqcrit0);
tdel = ts(id)+delay;
ti = ti-tdel;     
tf = tf-tdel;   
tspan = [ti tf];
t1 = 0;
t2 = t1+28;


%% solver

sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
[~,Nobs_rep,~,~,ts,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
if mode == 1
    Thrs1 = Neqcrit; 
end
[~,id] = max(Nobs_rep>=Thrs1);
T1 = ts(id)+delay;
flag = 1;

while flag
    sol = dde23(@(t,x,Z) dde_CB_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
    [~,Nobs_rep,~,~,ts,~] = dailyCases_CB_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
    Tdis = ts;
    idx = ts>=T1(end)+D_LD+D;
    Nobs_rep = Nobs_rep(idx); Tdis = Tdis(idx);
    [~,id] = max(Nobs_rep>=Thrs1);
    T1_app = Tdis(id)+delay;
    if T1_app>tmax
        flag = 0;
    elseif id == 1
        flag =0;
    else
        T1 = [T1 ; T1_app];
    end
end


%% Para ploteo

sol = dde23(@(t,x,Z) dde_CB_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
[Ntest,Nobs_rep,Nreal,ne,ts,Neqcrit] = dailyCases_CB_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
Tdis = ts;

t = sol.x;
ts = t(1):t(end);
x = deval(sol,ts);
S  = x(1,:); ET  = x(2,:); EH  = x(3,:);
T = x(4,:); H = x(5,:); Hs = x(6,:); t = ts;
N_hat_obs = Ntest';
N_T = Nobs_rep;
Rt_hat = N_T./[NaN(tau_gen,1) ; N_T(1:end-tau_gen)];

%% Visualization

load('Colores.mat')
str = strcat('$\tau=$',num2str(tau));

%% Solo real 

ax = backplot('Daily new cases');
if mode == 1
    plot(Tdis/7,Nobs_rep,lt,'Color',or2,'LineWidth',3*fact_curva)
else
    plot(Tdis/7,Nobs_rep,lt,'Color',red1,'LineWidth',3*fact_curva)
end
hold on
plot(Tdis/7,Thrs1*ones(size(Tdis)),ls,'Color',[1 0 0],'LineWidth',1.5*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('days since lockdown','interpreter','latex','FontSize',15*fact_label) 
ylabel('New infections','interpreter','latex','FontSize',15*fact_label)
hold on
xlim([tmin tmax]/7)
ylim([0 Nlim])
ax.TickLabelInterpreter='latex';

%% kt-profile

ax = backplot('Fig 1: LD duration');
A = []; 
for i = 1:length(T1)
    A          = [A ; Rt_t(Rt,Rtld,Rtald,Tdis,T1(i),T1(i)+D_LD,D)'/R0];
end
kt_profiles     = min(A,[],1);
if mode == 1
    plot(Tdis/7,kt_profiles,lt,'Color',or2,'LineWidth',3*fact_curva)
else
    plot(Tdis/7,kt_profiles,lt,'Color',red1,'LineWidth',3*fact_curva)
end
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('Weeks','interpreter','latex','FontSize',15*fact_label)
% ylabel('$\int_{0}^{3\rm mo}\hat{N}^{\rm obs}$','interpreter','latex','FontSize',15*fact_label)
hold on
xlim([tmin tmax]/7)
ylim([0.25 0.8])
set(gca, 'YTick', [0.25 0.8])
ax.TickLabelInterpreter='latex';