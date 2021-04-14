%%%%%% FigS3b %%%%%%

clear all
close all
clc

%% Definici?n de parametros "Default"

N_sampling  = 1e2;
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
epsilon     = 0.05;         % leak              The idea behind this is to set kISOL = 1/3 k lockdown, and 2/3 of contacts traced

%% second order parameters

xim = 1-xi;
ktdef = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2)/R0;
ktdef0 = fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r2,0,epsilon,R0),2)/R0;

%% Definici?n par?metros para ser barridos

[axi,bxi] = findBparam(0.32,0.0025);                % mean = 0.32, variance pm 0.0025;
[aeta,beta] = findBparam(0.66,0.005/4);             % mean = 0.66, variance = 0.0025;
[anu,bnu] = findBparam(0.075,0.005/8);              % mean = 0.1, variance = 0.005;
[aepsilon,bepsilon] = findBparam(0.05,0.005/8);     % mean = 0.1, variance = 0.005;
[als,bls] = findBparam(0.25,0.005/6);               % mean = 0.1, variance = 0.005;

%% calculo 10%

Xi =  betarnd(axi,bxi,N_sampling,1);
Eta =  betarnd(aeta,beta,N_sampling,1);
Lambda_s = betarnd(als,bls,N_sampling,1);
Nu =  betarnd(anu,bnu,N_sampling,1);
Epsilon =  betarnd(aepsilon,bepsilon,N_sampling,1);
Tau = gamrnd(4,1,N_sampling,1); 
ktcrit_rnd = NaN(6,N_sampling);
ktcrit0_rnd = NaN(6,N_sampling);
for i = 1:N_sampling
    try
        ktcrit_rnd(1,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,Nu(i),Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit_rnd(1,i) = NaN;
    end
    try
        ktcrit_rnd(2,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,Epsilon(i),R0),2);
    catch err
        ktcrit_rnd(2,i) = NaN;
    end
    try
        ktcrit_rnd(3,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,Lambda_s(i),lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit_rnd(3,i) = NaN;
    end
    try
        ktcrit_rnd(4,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,Eta(i),epsilon,R0),2);
    catch err
        ktcrit_rnd(4,i) = NaN;
    end
    try
        ktcrit_rnd(5,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(Xi(i),tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit_rnd(5,i) = NaN;
    end
    try
        ktcrit_rnd(6,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,Tau(i),nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0),2);
    catch err
        ktcrit_rnd(6,i) = NaN;
    end
end

for i = 1:N_sampling
    try
    ktcrit0_rnd(1,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,Nu(i),Rt,Gamma,lambda_s2,lambda_r,0,epsilon,R0),2);
    catch err
        ktcrit0_rnd(1,i) = NaN;
    end
    try
    ktcrit0_rnd(2,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r,0,Epsilon(i),R0),2);
    catch err
        ktcrit0_rnd(2,i) = NaN;
    end
    try
    ktcrit0_rnd(5,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(Xi(i),tc,tau,nu,Rt,Gamma,lambda_s2,lambda_r,0,epsilon,R0),2);
    catch err
        ktcrit0_rnd(5,i) = NaN;
    end
    try
    ktcrit0_rnd(6,i) = (1/R0)*fzero(@(Rt) maxvpdde_lin(xi,tc,Tau(i),nu,Rt,Gamma,lambda_s,lambda_r,0,epsilon,R0),2);
    catch err
        ktcrit0_rnd(6,i) = NaN;
    end
end


load('DefColors.mat')
red = [1 0 0]; blue = [0 0 1]; green = [0 1 0];
BW = 0.025;
BWparam = 0.025;
fact_axis = 1.2;
fact_label = 1.3;
fact_curva = 3;
siz = 15;
W = 8; H = 6;
name = {'ktcrit_ls','ktcrit_xiap','ktcrit_eta','ktcrit_ep','ktcrit_nu','ktcrit_nu'};
num = {'3_2';'4_2';'5_2';'2_2';'1_2'};
for j = [1 2 3 4 5 6]
    figure('units','centimeters','position',[5 5 W H]);
    ax = subplot(1,1,1);
    ax.Position = [0.28 0.32 0.65 0.55];
    ax.ActivePositionProperty = 'position';
    C = Default(j,:);
    if and(not(j==3),not(j==4))
        idx = ktcrit0_rnd(j,:)>0;
        set(gca,'FontSize',siz*fact_axis)
        hold on
        pdi = fitdist(ktcrit0_rnd(j,idx)','gev');
        xi = 0:0.01:1;
        yi = pdf(pdi,xi); yi = yi/100;
        p1 = plot(xi,yi,'LineWidth',fact_curva,'Color',C);
        hold on
        patch([xi fliplr(xi)],[yi zeros(size(yi))],C,'FaceAlpha',0.25,'LineStyle','none','HandleVisibility','off');%,[0 0.5 0],'FaceColor','interpolate')
        hold on
        idx = ktcrit_rnd(j,:)>0;
        pdi = fitdist(ktcrit_rnd(j,idx)','gev');
        xi = 0:0.01:1;
        yi = pdf(pdi,xi);  yi = yi/100;
        hold on
        p2 = plot(xi,yi,'LineWidth',fact_curva,'Color',C);
        hold on
        patch([xi fliplr(xi)],[yi zeros(size(yi))],C,'FaceAlpha',0.75,'LineStyle','none','HandleVisibility','off');%,[0 0.5 0],'FaceColor','interpolate')
        hold on
        p1.Color(4) = 0.25;
        p2.Color(4) = 0.75;
        ax.TickLabelInterpreter='latex';
    else
        idx = ktcrit_rnd(j,:)>0;
        pdi = fitdist(ktcrit_rnd(j,idx)','gev');
        xi = 0:0.01:1;
        yi = pdf(pdi,xi);  yi = yi/100;
        hold on
        p2 = plot(xi,yi,'LineWidth',fact_curva,'Color',C);
        hold on
        patch([xi fliplr(xi)],[yi zeros(size(yi))],C,'FaceAlpha',0.75,'LineStyle','none','HandleVisibility','off');%,[0 0.5 0],'FaceColor','interpolate')
        hold on
        p1.Color(4) = 0.25;
        p2.Color(4) = 0.75;
        ax.TickLabelInterpreter='latex';
    end
    set(gca,'FontSize',15*fact_axis)
    hold on
    plot([ktdef ktdef],[0 max(yi)],'r--','LineWidth',fact_curva,'HandleVisibility','off')
    hold on
    plot([ktdef0 ktdef0],[0 max(yi)],'r--','LineWidth',fact_curva,'HandleVisibility','off')
    hold on
    title(num2str(j))
    xlabel('$k_t^{\mbox{crit}}$','interpreter','latex','FontSize',15*fact_label)
    ax.TickLabelInterpreter='latex';
end

%% Distribuciones individuales

M = [Lambda_s Xi Eta Epsilon Nu Tau];
str = {'$\lambda_s$','$\xi^{\mbox{ap}}$','$\eta$','$\epsilon$','$\nu$','$\tau$'};
name = {'ls','xiap','eta','ep','nu','tau'};
num = {'3_1';'4_1';'5_1';'2_1';'1_1'};
for i = [1 2 3 4 5 6]
    figure('units','centimeters','position',[5 5 W H]);
    ax = subplot(1,1,1);
    ax.Position = [0.28 0.3 0.65 0.55];
    ax.ActivePositionProperty = 'position';
    C = Default(i,:);
    v = M(:,i);
    if i <6
        pdi = fitdist(v,'beta');
        xi = 0:0.01:1;
    else
        pdi = fitdist(v,'gamma');
        xi = 0:0.1:10;
    end
    
    yi = pdf(pdi,xi); yi = yi/100;
    hold on
    plot(xi,yi,'LineWidth',fact_curva,'Color',C)
    hold on
    patch([xi fliplr(xi)],[yi zeros(size(yi))],C,'FaceAlpha',0.5,'LineStyle','none','HandleVisibility','off');
    set(gca,'FontSize',siz*fact_axis)
    hold on
    legend({str{i}},'interpreter','latex','FontSize',siz*fact_label);
    hold on
    med = median(pdi);
    plot([med med],[0 max(yi)],'r--','HandleVisibility','off')
    if i<6
        xlim([0 1])
        ylim([0 0.25])
    end
    xlabel(str{i},'interpreter','latex','FontSize',siz*fact_label)
    ylabel('probability','interpreter','latex','FontSize',siz*fact_label)
    ax.TickLabelInterpreter='latex';
end
