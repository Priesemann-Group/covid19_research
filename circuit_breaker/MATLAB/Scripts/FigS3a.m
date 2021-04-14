%%%%%% FigS3a %%%%%%

clear all
close all
clc

%% Definici?n de parametros "Default"

lambda_r    = 0;            % random testing | screening
lambda_r2   = 0;
tc          = 4;            % latent period
Gamma       = 0.1;          % recovery rate
R0          = 3.3;
xi          = 0.32;         % Asymptomatic ratio
eta         = 0.66;         % tracing efficiency
tau         = 2;            % tracing delay
lambda_s    = 0.25;         % symptomatic testing/self reporting
lambda_s2   = 0.1; 
nu          = 0.075;        % isolation factor
epsilon     = 0.05;         % leak              

%% second order parameters

xim = 1-xi;
ktdef = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2)/R0;
ktdef0 = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r2,0,epsilon,R0),2)/R0;

%% Grafico FigS2a
Nmax = 100;
nu0 = 0; nu1 = 1;
epsilon0 = 0; epsilon1=1;
ls0 = 0; ls1 = 1;
eta0 = 0 ; eta1 = 1;
xi0 = 0; xi1=1;
tau0 = 0; tau1 = 10;
Nu = linspace(nu0,nu1,Nmax);
Epsilon = linspace(epsilon0,epsilon1,Nmax);
Lambda_s = linspace(ls0,ls1,Nmax);
Eta = linspace(eta0,eta1,Nmax);
Xi = linspace(xi0,xi1,Nmax);
Tau = linspace(tau0,tau1,Nmax);
ktcrit = NaN(6,Nmax);

for i = 1:Nmax
    try
    ktcrit(1,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,Nu(i),Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit(1,i) = NaN;
    end
    try
    ktcrit(2,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,Epsilon(i),R0),2);
    catch err
        ktcrit(2,i) = NaN;
    end
    try
    ktcrit(3,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,Lambda_s(i),lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit(3,i) = NaN;
    end
    try
    ktcrit(4,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,Eta(i),epsilon,R0),2);
    catch err
        ktcrit(4,i) = NaN;
    end
    try
    ktcrit(5,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(Xi(i),tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit(5,i) = NaN;
    end
    try
    ktcrit(6,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,Tau(i),nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit(6,i) = NaN;
    end
end

M = [Nu ; Epsilon ; Lambda_s ; Eta ; Xi ; Tau];
xl = {'$\nu$'; '$\epsilon$'; '$\lambda_s$' ; '$\eta$' ; '$\xi^{\rm ap}$' ; '$\tau$'};
load('DefColors.mat')
red = [1 0 0]; blue = [0 0 1]; green = [0 1 0];
BW = 0.025;
BWparam = 0.025;
fact_axis = 1.2;
fact_label = 1.3;
fact_curva = 3;
siz = 15;
W = 8; H = 6;

for i = 1:6
    figure('units','centimeters','position',[5 5 W H]);
    ax = subplot(1,1,1);
    ax.Position = [0.28 0.32 0.65 0.55];
    ax.ActivePositionProperty = 'position';
    plot(M(i,:),ktcrit(i,:),'Color',Default(i,:),'LineWidth',3*fact_curva)
    hold on
    plot(M(i,:),ktdef*ones(size(M(i,:))),'r--','LineWidth',2*fact_curva,'HandleVisibility','off');
    hold on
    set(gca,'FontSize',15*fact_axis)
    ylabel('$k_t^{\rm crit}$','interpreter','latex','FontSize',15*fact_label)
    if i<6
        xlim([0 1])
    end
    ylim([0 1])
    xlabel(xl{i},'interpreter','latex','FontSize',15*fact_label)
    ax.TickLabelInterpreter='latex';
end