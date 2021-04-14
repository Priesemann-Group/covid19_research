function F = dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0)
% solves the tti differential equations with a tracing delay of tau days.
% we also include a SEIR framework, with explicit compartments for traced
% and hidden pool, representing the imperfect quarantine and the
% "wild-type" of contagion occurring somewhere out there.
% Variables in x = [S ET EH T H Hs R]';

%% Approximation of the delay
S = x(1); ET  = x(2); EH = x(3); T = x(4); H = x(5); Hs = x(6);
Htlag = Z(5);
Hslag = Z(6);

%% Tracing and other pre-solver quantities

tol         = 1e-5;
Phi         = Phi_t(Phi0,Phild,Phi0,t,t1,t2,D);                                                        % solo por ahora, despu?s arreglamos este tete del PHI(t,0,2,Phi0,Phimax);   
xim         = 1-xi;

%% av Time spent in one pool

tsr = Gamma/(Gamma+lambda_s+lambda_r);
tr  = Gamma/(lambda_r+Gamma);
lambda_eq = (lambda_r*(1-phi)*tr + phi*lambda_s*tsr)/(lambda_r+lambda_s*phi);

%% eq values

Rt_del      = Rt_t(Rt,Rtld,Rtald,t-tau,t1,t2,D);
Rt          = Rt_t(Rt,Rtld,Rtald,t,t1,t2,D);
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

%% Solver
F = zeros(7,1);   
dSdt    = -Gamma*Rt*(S/M)*H - Gamma*(S/M)*(nu+epsilon)*R0*T  -Phi*(S/M);  
dETdt   =  Gamma*(S/M)*nu*R0*T                       + chi*ne  - (1/tc)*ET ;       % dETdt
dEHdt   =  Gamma*Rt*(S/M)*H+Gamma*(S/M)*epsilon*R0*T - chi*ne  - (1/tc)*EH;        % dEHdt
dTdt    = (1/tc)*ET     - Gamma*T + Ntest       + ne*fT;                    % dTdt
dHdt    = (1/tc)*EH     - Gamma*H - Ntest       - ne*fH   + Phi*(S/M);   	% dHdt
dHsdt   = (xim/tc)*EH   - Gamma*Hs- Ntest_s     - ne*fHs  + Phi*xim*(S/M); 	% dHsdt    
dRdt    = Gamma*(T+H);

F(1) = dSdt; F(2) = dETdt; F(3) = dEHdt; F(4) = dTdt; F(5) = dHdt; F(6) = dHsdt; F(7) = dRdt;