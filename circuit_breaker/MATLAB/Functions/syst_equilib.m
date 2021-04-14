function F = syst_equilib(x,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,epsilon,nmax,Phi)
% numerically solves the "equilibrium" equations, for the case of limited
% tracing capacities

%% Tracing and other pre-solver quantities

tol         = 1e-5;
xim         = 1-xi;
chi         = exp(-tau/tc);
ne          = nmax;
chimr       = temporalCorrection(tc,lambda_r,tau,tol);
chimrs      = temporalCorrection(tc,lambda_s+lambda_r,tau,tol);
fT          = xi*chimr + xim*chimrs;
fH          = fT;
fHs         = xim*chimrs;

%% Solver
F = zeros(5,1);   

ET  = x(1); EH = x(2); T = x(3); H = x(4); Hs = x(5);

Test_Hs = lambda_s*Hs;
Test_Hsr = lambda_r*Hs;
Test_H  = lambda_r*H;

dETdt   =  Gamma*Rt*nu*T                 + chi*ne         - (1/tc)*ET ;         % dETdt
dEHdt   =  Gamma*Rt*(H+epsilon*T)        - chi*ne         - (1/tc)*EH;          % dEHdt
dTdt    = (1/tc)*ET     - Gamma*T + Test_H  + Test_Hs   + ne*fT;                % dTdt
dHdt    = (1/tc)*EH     - Gamma*H - Test_H  - Test_Hs   - ne*fH   + Phi;        % dHdt
dHsdt   = (xim/tc)*EH   - Gamma*Hs- Test_Hs - Test_Hsr  - ne*fHs  + Phi*xim; 	% dHsdt    

F(1) = dETdt; F(2) = dEHdt; F(3) = dTdt; F(4) = dHdt; F(5) = dHsdt; 