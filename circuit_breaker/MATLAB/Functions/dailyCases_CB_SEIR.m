function [Nobs_test,Nobs_total,Nreal,ne,ts,Ncrit] = dailyCases_CB_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0)
% solves the tti differential equations with a tracing delay of tau days.
% we also include a SEIR framework, with explicit compartments for traced
% and hidden pool, representing the imperfect quarantine and the
% "wild-type" of contagion occurring somewhere out there.
% Variables in x = [S ET EH T H Hs R]';

%% Extraction of variables
t = sol.x; ts = t(1):t(end);
x = deval(sol,ts);
S  = x(1,:); ET  = x(2,:);
T = x(4,:); H = x(5,:); Hs = x(6,:);
t=ts;

%% Approximation of the delay

% el problema aqu? lo da la no uniformidad del tiempo
Htlag = H(1)*ones(size(H));
Hslag = Hs(1)*ones(size(Hs));
idx = t>=t(1)+tau;
Htlag(idx) = H(1:length(Htlag(idx)));
Hslag(idx) = Hs(1:length(Hslag(idx)));

%% Tracing and other pre-solver quantities

tol         = 1e-5;
xim         = 1-xi;
chi         = exp(-tau/tc);

%% av Time spent in one pool

tsr = Gamma/(Gamma+lambda_s+lambda_r);
tr  = Gamma/(lambda_r+Gamma);
teq = (lambda_r*((1-phi)*tr +phi*tsr)+ phi*lambda_s*tsr)/(lambda_r+lambda_s*phi);
Hsinf = phi*nmax/(lambda_s*phi + lambda_r);
Hinf = nmax/(lambda_s*phi + lambda_r);
Ntest = lambda_r*min(H,Hinf)      + lambda_r2*max(0,H-Hinf)... 
    + lambda_s*min(Hs,Hsinf)    + lambda_s2*max(0,Hs-Hsinf);

%% loop TTI

ne = zeros(size(t));
Rt_vect = NaN(size(ne));%Rt_t(Rt,Rtld,Rtald,t,t1,t2,D);
Phi     = NaN(size(ne));%Phi_t(Phi0,Phild,Phi0,t,t1,t2,D);  
flag = 1;
iNcrit = 5;
for i = 1:length(t)
    % dirty trick
    A = [];
    A_del = [];
    B = [];
    for i = 1:length(T1)
        A          = [A ; Rt_t(Rt,Rtld,Rtald,t,T1(i),T1(i)+D_LD,D)];
        A_del      = [A_del ; Rt_t(Rt,Rtld,Rtald,t-tau,T1(i),T1(i)+D_LD,D)];
        B          = [B ; Phi_t(Phi0,Phild,Phi0,t,T1(i),T1(i)+D_LD,D)];
    end
    Rt_del      = min(A_del);
    Rt_vect(i)          = min(A);
    Phi(i)         = min(B);
    if Ntest(i) >= nmax 
        ne(i) = eta*Rt_del*(teq)*nmax;
        if flag
            iNcrit = i;
            flag = 0;
        end
    else
        ne(i) = eta*Rt_del*(Htlag(i)*tr*lambda_r+Hslag(i)*(tsr*lambda_s+(tsr-tr)*lambda_r));
    end
end

chimr       = temporalCorrection(tc,lambda_r,tau,tol);
chimrs      = temporalCorrection(tc,lambda_s+lambda_r,tau,tol);
fT          = xi*chimr + xim*chimrs;

%% Solver

Nobs_test = Ntest;
Nobs_total = (1/tc) * ET + Ntest + fT*ne;
Nobs_total = EstimDelay_num(Nobs_total);
Nreal = Gamma*Rt_vect.*Htlag'+((epsilon+nu)*R0*T').*(S/M)'+Phi;
Ncrit = Nobs_total(iNcrit);

