function [tLD,F] = CostoLockdown(ktald,mode,Thrs1)

ti = -30;     
tmin = -5*7;
tmax = 30*7;%360;
tf = 360;   

tspan = [ti tf];
lags = 2;           % = tau
t1 = 0;
D_LD = 2*7;
t2 = t1+D_LD;
D = 7;
delay = 0;

%% Default Robs
R0      = 3.3;
Rt      = 0.8*R0;
Rtld    = 0.25*Rt; 
Rtald   = ktald*R0;  

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
nu          = 0.075;         % isolation factor
epsilon     = 0.05;        % leak              The idea behind this is to set kISOL = 1/3 k lockdown, and 2/3 of contacts traced
Phi0        = 1;          % external contagion
nmax        = M*50/1e6;     % tracing limit
Phild       = Phi0/10;    % Influx during lockdown
tau_gen     = 4;        % generation time
% parameters after threshold
lambda_s2   = 0.1; 
lambda_r2   = 0;
xim = 1-xi;
phi = 0.4;

%% Initial condition

% x0 = [S ET EH T H Hs R]
x0      = zeros(1,7);
x0(4)   = I0; x0(5) = x0(4); x0(6) = xim*x0(5); x0(2:3) = x0(4:5);
x0(1)   = M-sum(x0(2:end))+x0(6);


%% Determination of start of the lockdown (day zero) and reorganization of the days

% options = ddeset('RelTol',1e-9,'AbsTol',1e-9);
sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan);%,options);
[~,Nobs_rep,~,~,ts,Neqcrit0] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phi0,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
[~,id] = max(Nobs_rep>=Neqcrit0);
tdel = ts(id)+delay;

ti = ti-tdel;     
tf = tf-tdel;   
tspan = [ti tf];
t1 = 0;
t2 = t1+28;


%% solver

sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rt,Rt,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan);%,options);
[~,Nobs_rep,~,~,ts,Neqcrit] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
if mode == 1
    Thrs1 = Neqcrit; 
end
[~,id] = max(Nobs_rep>=Thrs1);
T1 = ts(id)+delay;
flag = 1;

while flag
    sol = dde23(@(t,x,Z) dde_CB_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan);%,options);
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

sol = dde23(@(t,x,Z) dde_CB_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan);%,options);
[~,Nobs_rep,~,~,Tdis,~] = dailyCases_CB_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);

%% lockdown time

if tmax-T1(end)<=D_LD
    tLD = (length(T1)-1)*D_LD + (tmax-T1(end))+1;
else
    tLD = length(T1)*D_LD;
end

%% cumulative cases

idx = Tdis>=tmin & Tdis <=tmax;
Cumulative  = acumula(Tdis(idx),Nobs_rep(idx));
F = Cumulative(end);

