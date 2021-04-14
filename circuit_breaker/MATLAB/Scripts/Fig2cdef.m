%%% Figure 2 %%%

clear all
close all
clc

%% Timeframe and initial conditions

ti = -30;     
tmin = -8*7;
tf = 180;   
tmax = 16*7;
tspan = [ti tf];
lags = 2;
t1 = 0;
t2 = t1+28;
D = 7;
tik = [tmin:28:tmax]/7;
%% Default Robs (there are no lockdowns, but we use the same code)

R0      = 3.3;
Rt      = 0.8*R0;
Rtld    = Rt; 
Rtald   = Rt; 

%% para ploteo

Umbral  = 1000;
Alim = 5e3;
Aclim = 5e4;
Elim = 5e4;
Nlim = 0.5e3;         

%% Parameters 

M           = 1e6;          % Total population
I0          = M*100/1e6;    % initial infections
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
Phild       = Phi0;         % Influx during lockdown
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

%% Determination of day zero (when crossing TTI capacity)

delay = 0;%4*7;
sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan);
[~,Nobs_rep,~,~,ts,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
    Thrs1 = Neqcrit; 
[~,id] = max(Nobs_rep>=Thrs1);
tdel = ts(id)+delay;
ti = -30-tdel;     
tf = 250-tdel;   
tspan = [ti tf];
t1 = 0;
t2 = t1+28;
nT = length(ti:tf);

%% solver
Nobs = zeros(nT,2);
Rtobs = zeros(nT,2);
options = ddeset('RelTol',1e-9,'AbsTol',1e-9);
sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
[~,Nobs(:,1),~,~,~,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
t = sol.x;
ts = t(1):t(end);
x = deval(sol,ts);
ET1  = x(2,:); EH1  = x(3,:); T1 = x(4,:); H1 = x(5,:);
N_T = Nobs(:,1);
Rtobs(:,1) = N_T./[NaN(tau_gen,1) ; N_T(1:end-tau_gen)];
nmax = 10*nmax;
sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
[~,Nobs(:,2),~,~,~,~] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
t = sol.x;
ts = t(1):t(end);
x = deval(sol,ts);
ET2  = x(2,:); EH2  = x(3,:); T2 = x(4,:); H2 = x(5,:);
Tdis = ts;
N_T = Nobs(:,2);
Rtobs(:,2) = N_T./[NaN(tau_gen,1) ; N_T(1:end-tau_gen)];


%% Visualization

load('Colores.mat')
tmax = 12*7;

%% Fig 2c

ax = sqplot();
plot(Tdis/7,Nobs(:,1),lt,'Color',or2,'LineWidth',3*fact_curva)
hold on
plot(Tdis/7,Nobs(:,2),lt,'Color',red2,'LineWidth',3*fact_curva)
hold on
plot(Tdis,Neqcrit*ones(size(Tdis)),ls,'Color',[1 0 0],'LineWidth',1.5*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('Weeks','interpreter','latex','FontSize',10*fact_label) 
ylabel('$\hat{N}^{\rm obs}$','interpreter','latex','FontSize',10*fact_label)
hold on
xlim([tmin tmax]/7)
set(gca, 'XTick', tik)
ylim([0 Nlim])
ax.TickLabelInterpreter='latex';

%% Fig 2d

ax = sqplot();
plot(Tdis/7,Rtobs(:,1),lt,'Color',red1,'LineWidth',3*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
ylim([0.8 1.6])
ylabel('Obs Rep. Number','interpreter','latex','FontSize',10*fact_label)
hold on
yyaxis right
plot(Tdis/7,Rt*ones(size(Tdis)),lh,'Color',or2,'LineWidth',3*fact_curva)
ylim([0.8 3.2])
hold on
ylabel('Hidden Rep. Number','interpreter','latex','FontSize',10*fact_label)
hold on
xlim([tmin tmax]/7)
xlabel('Weeks','interpreter','latex','FontSize',10*fact_label) 
set(gca, 'XTick', tik)
ax.TickLabelInterpreter='latex';

%% Fig 2e

ax = sqplot();
plot(Tdis/7,T1,lt,'Color',bl1,'LineWidth',3*fact_curva)
hold on
plot(Tdis/7,H1,lh,'Color',bl3,'LineWidth',3*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('Weeks','interpreter','latex','FontSize',10*fact_label) 
ylabel('$I^{H},\,I^{Q}$','interpreter','latex','FontSize',10*fact_label)
ax.TickLabelInterpreter='latex';
xlim([tmin tmax]/7)
set(gca, 'XTick', tik)
ylim([0 Alim])
hold on


%% Fig 2f

ax = sqplot();
plot(Tdis/7,H1./T1,lt,'Color',red1,'LineWidth',3*fact_curva)
hold on
plot(Tdis/7,H2./T2,lt,'Color',red2,'LineWidth',3*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('Weeks','interpreter','latex','FontSize',10*fact_label) 
ylabel('$I^H/I^{Q}$','interpreter','latex','FontSize',10*fact_label)
hold on
xlim([tmin tmax]/7)
ylim([0 3])
set(gca, 'XTick', tik)
ax.TickLabelInterpreter='latex';

