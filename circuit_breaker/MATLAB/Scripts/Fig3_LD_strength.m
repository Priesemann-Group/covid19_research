%%% Figure 3 LD Strength %%%

clear all
close all
clc

%% Timeframe and initial conditions

ti = -90;     
tmin = -4*7;
tf = 360;   
tmax = 16*7;%360;
tspan = [ti tf];
lags = 2;               % = tau
delay = 28;
t1 = 0;
t2 = t1+28;
D = 7;
defWeeks = 4;  % should be 4
%% Default Robs
R0      = 3.3;
Rt      = 0.8*R0;
Rtld    = 0.25*R0;
Rtald   = 0.6*R0;

%% para ploteo

Umbral  = 1000;
Alim = 6e4;
Aclim = 5e4;
Elim = 5e4;
Nlim = 0.5e3;
Dmax = 7*12;              
Rti = 0.5;
Rtf = 1.25;
Clim = 10e4;
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

sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan);
[~,Nobs_rep,~,~,ts,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
    Thrs1 = Neqcrit; 
[~,id] = max(Nobs_rep>=Thrs1);
tdel = ts(id)+delay;

ti = ti-tdel;     
tf = tf-tdel;   
tspan = [ti tf];
t1 = 0;
t2 = t1+28;

%% solver
options = ddeset('RelTol',1e-9,'AbsTol',1e-9);
sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
x = sol.y; t = sol.x;
[Ntest,~,~,ne,ts,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
Tdis = ts;

%% Visualization

load('Colores.mat')
str = strcat('$\tau=$',num2str(tau));
load('Pink_Map.mat')

%% Figure lockdown strength
ax = backplot('Fig 2: Contact reduction');
K = [0.8; 0.6 ; 0.5; 0.4; 0.25; 0.15];
N_K = length(K);
Nobs_rep = NaN(length(ti:tf),N_K);
Rt_hat = Nobs_rep;
tk = t1; tk2 = t1 + defWeeks*7;
idx = Tdis>=-1 & Tdis<=12*7; nt = sum(idx);
Cumulative_cases = NaN(nt,N_K);
Rthat = NaN(length(ts),N_K);
for k = 1:N_K
    Rtld = K(k)*R0;
    id(k)= floor(512*(k/(9 + 1)));
    if k == 1
        sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,tk,tk2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
        [~,Nobs_rep(:,k),~,~,Tdis,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,tk,tk2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0);
        N_T = Nobs_rep(:,k);
        plot(Tdis/7,Nobs_rep(:,k),lt,'Color',map(id(k),:),'LineWidth',1*fact_curva)
        hold on
        Cumulative_cases(:,k) = acumula(Tdis(idx),Nobs_rep(idx,k));
        Rthat(:,k) = N_T./[NaN(tau_gen,1) ; N_T(1:end-tau_gen)];
    else
        sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,tk,tk2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan,options);
        [~,Nobs_rep(:,k),~,~,Tdis,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,tk,tk2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
        N_T = Nobs_rep(:,k);
        plot(Tdis/7,Nobs_rep(:,k),lt,'Color',map(id(k),:),'LineWidth',1*fact_curva)
        hold on
        Cumulative_cases(:,k) = acumula(Tdis(idx),Nobs_rep(idx,k));
        Rthat(:,k) = N_T./[NaN(tau_gen,1) ; N_T(1:end-tau_gen)];
    end
end

plot(Tdis/7,Neqcrit*ones(size(Tdis)),ls,'Color',[1 0 0],'LineWidth',1.5*fact_curva)
hold on
plot(Tdis/7,250*ones(size(Tdis)),ls,'Color',[1 0 0],'LineWidth',1.5*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('Weeks','interpreter','latex','FontSize',15*fact_label)
ylabel('$\hat{N}^{\rm obs}$','interpreter','latex','FontSize',15*fact_label)
hold on
xlim([tmin/7 tmax/7-4])
set(gca, 'XTick', [-4 0 4 8 12])
ylim([0 Nlim])
ax.TickLabelInterpreter='latex';

%% Infecciones

ax = backplot('Fig 1: LD duration');
plot(K,Cumulative_cases(end,:),'*','Color',red2,'LineWidth',3*fact_curva)
hold on
plot(K(2:end),Cumulative_cases(end,2:end),'-','Color',red2,'LineWidth',1*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('$k_t$','interpreter','latex','FontSize',15*fact_label)
ylabel('$\int_{0}^{3\rm mo}\hat{N}^{\rm obs}$','interpreter','latex','FontSize',15*fact_label)
hold on
ylim([0 Clim])
ax.TickLabelInterpreter='latex';

%% kt-profile

ax = backplot('Fig 1: LD duration');
kt_profiles = NaN(length(ts),N_K);
for k = 1:N_K
    Rtld = K(k)*R0;
    id(k)= floor(512*(k/(9 + 1)));
    if k == 1
        kt_profiles(:,1)  = Rt_t(Rt,Rt,Rt,Tdis,t1,t2,D)/R0;
    else
        kt_profiles(:,k)  = Rt_t(Rt,Rtld,Rtald,Tdis,t1,t2,D)/R0;
    end
    plot(Tdis/7,kt_profiles(:,k),lt,'Color',map(id(k),:),'LineWidth',3*fact_curva)
    hold on
end
set(gca,'FontSize',15*fact_axis)
hold on
xlabel('Weeks','interpreter','latex','FontSize',15*fact_label)
% ylabel('$\int_{0}^{3\rm mo}\hat{N}^{\rm obs}$','interpreter','latex','FontSize',15*fact_label)
hold on
xlim([tmin/7 tmax/7-4])
set(gca, 'XTick', [-4 0 4 8 12])
ylim([0.1 0.8])
set(gca, 'YTick', [0.25 0.8])
ax.TickLabelInterpreter='latex';

