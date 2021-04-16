function F = dde_vaccine_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,T1,D_LD,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0,V)
% solves the tti differential equations with a tracing delay of tau days.
% we also include a SEIR framework, with explicit compartments for traced
% and hidden pool, representing the imperfect quarantine and the
% "wild-type" of contagion occurring somewhere out there.
% Variables in x = [S ET EH T H Hs R]';

%% Identification of critical points

A = [];
A_del = [];
B = [];
for i = 1:length(T1)
    A          = [A ; Rt_t(Rt,Rtld,Rtald,t,T1(i),T1(i)+D_LD,D)];
    A_del      = [A_del ; Rt_t(Rt,Rtld,Rtald,t-tau,T1(i),T1(i)+D_LD,D)];
    B          = [B ; Phi_t(Phi0,Phild,Phi0,t,T1(i),T1(i)+D_LD,D)];
end
Rt_del      = min(A_del);
Rt          = min(A);
Phi         = min(B);

%% Approximation of the delay
S = x(1); ET  = x(2); EH = x(3); T = x(4); H = x(5); Hs = x(6);
Htlag = Z(5);
Hslag = Z(6);
   

%% Tracing and other pre-solver quantities

tol         = 1e-5;
xim         = 1-xi;

%% av Time spent in one pool

tsr = Gamma/(Gamma+lambda_s+lambda_r);
tr  = Gamma/(lambda_r+Gamma);
lambda_eq = (lambda_r*((1-phi)*tr +phi*tsr)+ phi*lambda_s*tsr)/(lambda_r+lambda_s*phi);

%% eq values

Hsinf       = phi*nmax/(lambda_s*phi + lambda_r);
Hinf        = nmax/(lambda_s*phi + lambda_r);

Ntest = lambda_r*min(H,Hinf)      + lambda_r2*max(0,H-Hinf)... 
    + lambda_s*min(Hs,Hsinf)    + lambda_s2*max(0,Hs-Hsinf);
Ntest_s = lambda_r*min(Hs,Hsinf)    + lambda_r2*max(0,Hs-Hsinf) + ...
    lambda_s*min(Hs,Hsinf)    + lambda_s2*max(0,Hs-Hsinf);
%% correction for tracing capacity (i guess)

if Ntest >= nmax
    ne = eta*Rt_del*(lambda_eq)*nmax;
else
    ne = eta*Rt_del*(Htlag*tr*lambda_r+Hslag*(tsr*lambda_s+(tsr-tr)*lambda_r));
end

chi         = exp(-tau/tc);
chimr       = temporalCorrection(tc,lambda_r,tau,tol);
chimrs      = temporalCorrection(tc,lambda_s+lambda_r,tau,tol);
fT          = xi*chimr + xim*chimrs;
fH          = fT;
fHs         = xim*chimrs;

%% vaccination

v = dvacdt(t,V);

%% Solver
F = zeros(7,1);   
dSdt    = -Gamma*Rt*(S/M)*H - Gamma*(S/M)*(nu+epsilon)*R0*T  -Phi*(S/M)-v;  
dETdt   =  Gamma*(S/M)*nu*R0*T                       + chi*ne  - (1/tc)*ET ;       % dETdt
dEHdt   =  Gamma*Rt*(S/M)*H+Gamma*(S/M)*epsilon*R0*T - chi*ne  - (1/tc)*EH;        % dEHdt
dTdt    = (1/tc)*ET     - Gamma*T + Ntest       + ne*fT;                    % dTdt
dHdt    = (1/tc)*EH     - Gamma*H - Ntest       - ne*fH   + Phi*(S/M);   	% dHdt
dHsdt   = (xim/tc)*EH   - Gamma*Hs- Ntest_s     - ne*fHs  + Phi*xim*(S/M); 	% dHsdt    
dRdt    = Gamma*(T+H)+v;

F(1) = dSdt; F(2) = dETdt; F(3) = dEHdt; F(4) = dTdt; F(5) = dHdt; F(6) = dHsdt; F(7) = dRdt;