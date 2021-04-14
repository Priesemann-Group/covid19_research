%%%%%% FigS3c %%%%%%

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

%% second order parameters

xim = 1-xi;

%% Definici?n par?metros para ser barridos

[axi,bxi] = findBparam(0.32,0.0025);                % mean = 0.32, variance pm 0.0025;
[aeta,beta] = findBparam(0.66,0.005/4);             % mean = 0.66, variance = 0.0025;
[anu,bnu] = findBparam(0.075,0.005/8);              % mean = 0.1, variance = 0.005;
[aepsilon,bepsilon] = findBparam(0.05,0.005/8);     % mean = 0.1, variance = 0.005;
[als,bls] = findBparam(0.25,0.005/6);               % mean = 0.1, variance = 0.005;

%% calculo 10%
ktcrit_TTI = zeros(N_sampling,1);
ktcrit_Hosp = ktcrit_TTI;
Xi =  betarnd(axi,bxi,N_sampling,1);
Eta =  betarnd(aeta,beta,N_sampling,1);
Lambda_s = betarnd(als,bls,N_sampling,1);
Nu =  betarnd(anu,bnu,N_sampling,1);
Epsilon =  betarnd(aepsilon,bepsilon,N_sampling,1);
Tau = gamrnd(4,1,N_sampling,1); 
for i = 1:N_sampling
    try
    ktcrit_TTI(i) = (1/R0)*fzero(@(Rt) maxvpdde_lin_extra_comp(Xi(i),tc,Tau(i),Nu(i),Rt,Gamma,Lambda_s(i),lambda_r,Eta(i),Epsilon(i),R0),2);
    catch err
        ktcrit_TTI(i) = NaN;
    end
    try
    ktcrit_Hosp(i) = (1/R0)*fzero(@(Rt) maxvpdde_lin_extra_comp(Xi(i),tc,Tau(i),Nu(i),Rt,Gamma,lambda_s2,lambda_r,0,Epsilon(i),R0),2);
    catch err
        ktcrit_Hosp(i) = NaN;
    end
end


load('DefColors.mat')

fact_axis = 1.2;
fact_label = 1.3;
fact_curva = 3;
siz = 15;
W = 8; H = 6;
BW = 0.01;
BWparam = 0.001;

Pct = zeros(2,3);
%% Dist conjunta total

figure('units','centimeters','position',[5 5 2*W 2*H]);
    ax = subplot(1,1,1);
    ax.Position = [0.28 0.3 0.65 0.55];
    ax.ActivePositionProperty = 'position';
C = Default(7,:);

idx = ktcrit_Hosp>0;
set(gca,'FontSize',siz*fact_axis)
hold on
pdi = fitdist(ktcrit_Hosp(idx),'gev');
xi = 0:0.01:1;
yi = pdf(pdi,xi); yi = yi/100;
p1 = plot(xi,yi,'LineWidth',fact_curva,'Color',C);
%expected value
Pct(1,:) = prctile(ktcrit_Hosp(idx),[2.5 50 97.5]);
med0 = median(pdi);
mu0 = quadgk(@(x) x.*pdf(pdi,x),xi(1),xi(end));
%
hold on
patch([xi fliplr(xi)],[yi zeros(size(yi))],C,'FaceAlpha',0.25,'LineStyle','none','HandleVisibility','off');%,[0 0.5 0],'FaceColor','interpolate')
hold on
hold on
    plot([med0 med0],[0 max(yi)],'r--','HandleVisibility','off')
idx = ktcrit_TTI>0;
pdi = fitdist(ktcrit_TTI(idx),'gev');
xi = 0:0.01:1;
yi = pdf(pdi,xi);  yi = yi/100;
%expected value
Pct(2,:) = prctile(ktcrit_TTI(idx),[2.5 50 97.5]);
med = median(pdi);
mu = quadgk(@(x) x.*pdf(pdi,x),xi(1),xi(end));
%

hold on
p2 = plot(xi,yi,'LineWidth',fact_curva,'Color',C);
hold on
    plot([med med],[0 max(yi)],'r--','HandleVisibility','off')
patch([xi fliplr(xi)],[yi zeros(size(yi))],C,'FaceAlpha',0.75,'LineStyle','none','HandleVisibility','off');%,[0 0.5 0],'FaceColor','interpolate')
hold on
p1.Color(4) = 0.25;
p2.Color(4) = 0.75;
set(gca, 'XTick', [0 0.25 0.5 0.75 1])
% set(gca, 'YTick', [0 0.04])
xlim([0 1])
ylim([0 0.2])
xlabel('$k_t^{\mbox{crit}}$','interpreter','latex','FontSize',siz*fact_label)
ylabel('probability','interpreter','latex','FontSize',siz*fact_label)
legend({'$\eta=0$','$\eta=0.66$'},'interpreter','latex','FontSize',siz*fact_label);
ax.TickLabelInterpreter='latex';
save('S7b_three_compartment.mat')
