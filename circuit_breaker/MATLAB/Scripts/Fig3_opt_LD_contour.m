%%% Figure 3 optimal duration of LD %%%

clear all
close all
clc

%% Timeframe and initial conditions

ti          = -90;     
tmin        = -60;
tf          = 250;   
tap         = 150;  % was 120
tmax        = 90;%360;
tspan       = [ti tf];
lags        = 2;               % = tau
delay       = 0;
t1          = 0;
t2          = t1+28;
D           = 7;

%% Default Robs
R0      = 3.3;
Rt      = 0.8*R0;
Rtld    = 0.25*R0;
Rtald   = 0.6*R0;

%% para ploteo

Umbral  = 1000;
Alim    = 6e4;
Aclim   = 5e4;
Elim    = 5e4;
Nlim    = 0.4e3;
Dmax    = 7*8;              

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
Phi0        = 1;          % external contagion
nmax        = M*50/1e6;     % tracing limit
Phild       = Phi0/10;      % Influx during lockdown
tau_gen     = 4;        % generation time
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
phi = 0.4;%xeq(5)/xeq(4);

%% Determination of start of the lockdown (day zero) and reorganization of the days

options = ddeset('RelTol',1e-9,'AbsTol',1e-9);

sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
[~,Nobs_rep,~,~,ts,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
    Thrs1 = Neqcrit; 
[~,id] = max(Nobs_rep>=Thrs1);
tdel = ts(id)+delay;

ti = -90-tdel;     
tf = 250-tdel;   
tspan = [ti tf];
t1 = 0;
t2 = t1+28;

%% Ld Duration

tol = 0;
d = 4;
paso = 2;
flag = 0;
Rt_LockDown = linspace(0,0.6*R0,75);
T1 = [14 21 28 35 42 7*7];
DOPT = NaN(length(Rt_LockDown), length(T1));

N0 = zeros(size(T1));
for k = 1:length(T1)
    t1 = T1(k);
    sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
    [~,Nobs_rep,~,~,ts,~] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
    idx = ts == t1; N0(k) = Nobs_rep(idx);
    for i = 1:length(Rt_LockDown)
        if i>1
            if not(isnan(DOPT(i-1,k)))
                Rtldi = Rt_LockDown(i);
                [DOPT(i,k),~,~] = LD_SEIR(M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,ti,tf,tap,t1,D,Rtldi,Rtald,phi,lambda_s2,lambda_r2,x0,tol,R0,Neqcrit);
            end
        else
            Rtldi = Rt_LockDown(i);
            [DOPT(i,k),~,~] = LD_SEIR(M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,ti,tf,tap,t1,D,Rtldi,Rtald,phi,lambda_s2,lambda_r2,x0,tol,R0,Neqcrit);
            
        end
    end
end

%% Visualization

load('Colores.mat')

%% Solo real 

ax = backplot('Fig~0: Opt. LD duration');
for k = 1:length(T1)
    plot(100*Rt_LockDown/R0,smooth(DOPT(:,k))/7,lt,'LineWidth',3*fact_curva)
    hold on
end
% plot([100*Rtcmax2/R0 100*Rtcmax2/R0],[0 Dmax/7],lh,'Color',red2,'LineWidth',1*fact_curva)
hold on
% legend({'$\hat{N}^{\mbox{obs}}$','Threshold'},'interpreter','latex','FontSize',15*fact_axis);
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('$\%$ of pre COVID-19 contacts during lockdown','interpreter','latex','FontSize',10*fact_label) 
ylabel('min. LD [weeks]','interpreter','latex','FontSize',10*fact_label)
hold on
xlim([0 60])
set(gca,'YTick',[4 8 12])
ylim([0 Dmax/7])
ax.TickLabelInterpreter='latex';
