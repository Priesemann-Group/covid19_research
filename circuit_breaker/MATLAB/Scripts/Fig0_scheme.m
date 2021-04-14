%%% Scheme %%% 

clear all
close all
clc

%% Definici?n de parametros "Default"

N_sampling  = 1e5;
lambda_r    = 0;            % random testing | screening
lambda_r2   = 0;
tc          = 4;            % latency period
Gamma       = 0.1;          % recovery rate
R0          = 3.3;
xi          = 0.32;         % Asymptomatic ratio
eta         = 0.66;         % tracing efficiency
tau         = 2;            % tracing delay
lambda_s    = 0.25;         % symptomatic testing/self reporting
lambda_s2   = 0.1; 
nu          = 0.075;        % isolation factor
epsilon     = 0.05;         % leak     
Phi         = 1;            % 

%% second order parameters

xim = 1-xi;
ktcrit_TTI = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2)/R0;
ktcrit_Hosp = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r2,0,epsilon,R0),2)/R0;

%% Calculatio of the equilibrium level for different phis

kt = linspace(0,1,100);
N_eq = Phi./(ktcrit_TTI-kt); idx = N_eq<0; N_eq(idx) = 1e3;
N_eq_imag = Phi./(0.75-kt); idx = N_eq_imag<0; N_eq_imag(idx) = 1e3;

k1 = 0.89*ktcrit_TTI; k2 = 0.99*ktcrit_TTI;
N1 = Phi/(ktcrit_TTI-k1); N2 = Phi/(ktcrit_TTI-k2);
eN = (N2-N1)/N1
ek = (k2-k1)/k1
Dn = Phi * (k2-k1)/((ktcrit_TTI-k2)*(ktcrit_TTI-k1))

%% Visualization

load('Colores.mat')
load('mapmap.mat')
% load('Pink_map.mat')
ax = sqplot();
plot(kt,N_eq,lt,'Color',or1,'LineWidth',1.5*fact_curva)
hold on
plot([k1 k2],[N1 N1],lt,'Color',red1,'LineWidth',1.5*fact_curva)
hold on
plot([k2 k2],[N1 N2],lt,'Color',red1,'LineWidth',1.5*fact_curva)
xlim([0.2 0.8])
ylim([0 200])

ax = sqplot();
plot(kt,N_eq,lt,'Color',or1,'LineWidth',1.5*fact_curva)
hold on
plot(kt,10*N_eq,lt,'Color',or1,'LineWidth',1.5*fact_curva)
hold on
xlim([0.2 0.8])
ylim([0 200])


ax = sqplot();
plot(kt,N_eq,lt,'Color',or1,'LineWidth',1.5*fact_curva)
hold on
plot(kt,N_eq_imag,lt,'Color',or1,'LineWidth',1.5*fact_curva)
hold on
plot([ktcrit_TTI ktcrit_TTI],[0 1e3],lt,'Color',red1,'LineWidth',1.5*fact_curva)
hold on
plot([0.75 0.75],[0 1e3],lt,'Color',red1,'LineWidth',1.5*fact_curva)
xlim([0.2 0.8])
ylim([0 200])