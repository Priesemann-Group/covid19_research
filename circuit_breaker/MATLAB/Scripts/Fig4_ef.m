%%% Figura 4 ef %%%

clear all
close all
clc

%% Mode == 1: log; 0 : lin

mode = 0;

%% Definici?n de parametros "Default"

N_sampling = 1e3;
lambda_r    = 0;            % random testing | screening
lambda_r2   = 0;
tc          = 4;            % latency period
Gamma       = 0.1;          % recovery rate
R0          = 4.3;          % 4.3 for B.1.1.7 
%% Model parameters

xi          = 0.32;         % Asymptomatic ratio
eta         = 0.66;         % tracing efficiency
tau         = 2;            % tracing delay
lambda_s    = 0.25;         % symptomatic testing/self reporting
lambda_s2   = 0.1; 
nu          = 0.075;        % isolation factor
epsilon     = 0.05;         % leak              The idea behind this is to set kISOL = 1/3 k lockdown, and 2/3 of contacts traced
% parameters after threshold

%% second order parameters

xim = 1-xi;
ktdef = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2)/R0;
ktdef0 = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r2,0,epsilon,R0),2)/R0;

load('DefColors.mat')
red = [1 0 0]; blue = [0 0 1]; green = [0 1 0];
BW = 0.025;
BWparam = 0.025;
fact_axis = 1.2;
fact_label = 1.3;
fact_curva = 3;
siz = 15;

%% Grafico FigS2a
Nmax = 100;
lr0 = 0; lr1 = 1;
Lambda_r = logspace(-8,-1,Nmax);
ktcrit = NaN(2,Nmax);
for i = 1:Nmax
    try
    ktcrit(1,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,Lambda_r(i),eta,epsilon,R0),2);
    catch err
        ktcrit(1,i) = NaN;
    end
    try
    ktcrit(2,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,Lambda_r(i),0,epsilon,R0),2);
    catch err
        ktcrit(2,i) = NaN;
    end
end
% ktcrit = ktcrit';

M = [Lambda_r ; Lambda_r];
xl = {'$\lambda_r$' ; '$\lambda_r(\eta = 0)$' };
% num = {'1';'2';'3';'5';'4'};
W = 8; H = 6;

for i = 1:2
    figure('units','centimeters','position',[5 5 W H]);
    ax = subplot(1,1,1);
    ax.Position = [0.28 0.32 0.65 0.55];
    ax.ActivePositionProperty = 'position';
    if mode == 1
        semilogx(M(i,:),ktcrit(i,:),'Color',Default(i,:),'LineWidth',3*fact_curva)
        hold on
        semilogx(M(i,:),ktdef*ones(size(M(i,:))),'r--','LineWidth',2*fact_curva,'HandleVisibility','off');
        hold on
        semilogx(M(i,:),ktdef0*ones(size(M(i,:))),'r--','LineWidth',2*fact_curva,'HandleVisibility','off');
        hold on
        xlim([1e-8 1e-1])
    else
        plot(M(i,:),ktcrit(i,:),'Color',Default(i,:),'LineWidth',3*fact_curva)
        hold on
        plot(M(i,:),ktdef*ones(size(M(i,:))),'r--','LineWidth',2*fact_curva,'HandleVisibility','off');
        hold on
        plot(M(i,:),ktdef0*ones(size(M(i,:))),'r--','LineWidth',2*fact_curva,'HandleVisibility','off');
        hold on
        xlim([0 0.1])
    end
    set(gca,'FontSize',15*fact_axis)
    ylabel('$k_t^{\rm crit}$','interpreter','latex','FontSize',15*fact_label)
    
    ylim([0 1])
    xlabel(xl{i},'interpreter','latex','FontSize',15*fact_label)
    ax.TickLabelInterpreter='latex';
    %extractData(0,1,0.5,3.5,strcat('Rev1_FigS2a_',num{i},'.csv'))
end

%% Other option

f=0:0.01:0.9;
kpcrit_t = ktdef./(1-f);
kpcrit0_t = ktdef0./(1-f);
figure('units','centimeters','position',[5 5 W H]);
ax = subplot(1,1,1);
ax.Position = [0.28 0.32 0.65 0.55];
ax.ActivePositionProperty = 'position';
plot(f,kpcrit_t,'Color',Default(1,:),'LineWidth',3*fact_curva)
hold on
plot(f,kpcrit0_t,'Color',Default(2,:),'LineWidth',3*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
ylabel('$k_t^{\rm crit}(f)$','interpreter','latex','FontSize',15*fact_label)
ylim([0 1])
xlim([0 1])
xlabel('Immune fraction $f$','interpreter','latex','FontSize',15*fact_label)
ax.TickLabelInterpreter='latex';