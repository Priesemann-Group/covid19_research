%%% Figura costo lockdown %%%

clear all
close all
clc

%% Definición de variablesf

ktald = 0.2:0.005:0.8;
Thrs1 = 250;
Cumulative_TTI = NaN(size(ktald));
Cumulative_Hos = NaN(size(ktald));
LDtime_TTI = NaN(size(ktald));
LDtime_Hos = NaN(size(ktald));

%% loop

for i = 1:length(ktald)
    [LDtime_TTI(i),Cumulative_TTI(i)] = CostoLockdown(ktald(i),1,Thrs1);
    [LDtime_Hos(i),Cumulative_Hos(i)] = CostoLockdown(ktald(i),0,Thrs1);
end

%% Ploteo

load('Colores.mat')
ax = backplot('Daily new cases');
plot(ktald,LDtime_TTI/7,lt,'Color',bl1,'LineWidth',3*fact_curva)
hold on
plot(ktald,LDtime_Hos/7,lt,'Color',bl2,'LineWidth',3*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlim([ktald(1) ktald(end)])
ylim([0 12])
set(gca,'YTick',[0 4 8 12])
ax.TickLabelInterpreter='latex';


ax = backplot('Daily new cases');
plot(ktald,smooth(Cumulative_TTI),lt,'Color',red1,'LineWidth',3*fact_curva)
hold on
plot(ktald,smooth(Cumulative_Hos),lt,'Color',red2,'LineWidth',3*fact_curva)
hold on
set(gca,'FontSize',15*fact_axis)
hold on
xlim([ktald(1) ktald(end)])
ylim([0 6e4])
ax.TickLabelInterpreter='latex';
