function [A,B] = linStab_tti_extra_comp(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0)
% Funci?n que calcula las matrices A y B del sistema y' = Ay(t)+By(t-tau),
% donde y = [ET; EH; EHs; Enc; T ; H; Hs; Hnc]. Cuando mode = 1, entrega
% ambas matrices. Si mode=0, entrega solamente una matrix A+ = A+B, pues
% corresponde al caso en que tau = 0 (solamente para ese concepto).
% Hip?tesis subyacentes:
%   - (S/M) \approx 1; otherwise the system would be always stable (in S=0)
%   - nmax = \infty: In the considered scenario, the tracing capacity would
%   never be overwhelmed. y = [ET EH T H Hs]

tol         = 1e-5;
xim         = 1-xi;
Lseff       = Gamma*(((lambda_s+lambda_r)/(Gamma+lambda_s+lambda_r))-(lambda_r/(lambda_r+Gamma)));
Lreff       = Gamma*(lambda_r/(lambda_r+Gamma));
%op1
rho         = 1/tc;
chi1        = exp(-3*tau*rho);
chi2        = (3*rho*tau)   * exp(-3*rho*tau);
chi3        = (3*rho*tau)^2 * (1/2) * exp(-3*rho*tau);
alpha_r     = lambda_r-3*rho;
alpha_rs     = lambda_r+lambda_s-3*rho;
chimr       = (3*rho)^3 * (1/2) * exp(-3*rho*tau) * (1/alpha_r) * (tau^2 - 2*tau/alpha_r + (2/(alpha_r)^2)*(1-exp(-alpha_r*tau)));
if alpha_rs == 0
    chimrs      = (3*rho)^3 * (1/6) * exp(-3*rho*tau) * tau^3;
else
    chimrs      = (3*rho)^3 * (1/2) * exp(-3*rho*tau) * (1/alpha_rs) * (tau^2 - 2*tau/alpha_rs + (2/(alpha_rs)^2)*(1-exp(-alpha_rs*tau)));
end
fT          = xi*chimr + xim*chimrs;
fH          = fT;
fHs         = xim*chimrs;


%% Calculo de las matrices
A = zeros(9); B = A;
%(1,:) : ET1; 
A(1,1) = -3*rho; A(1,7) = nu*Gamma*R0; 
B(1,[8 9]) = chi1; 

%(2,:) : ET2; 
A(2,2) = -3*rho;  A(2,1) = 3*rho;  
B(2,[8 9]) = chi2; 

%(3,:) : ET3; 
A(3,3) = -3*rho;  A(3,2) = 3*rho; 
B(3,[8 9]) = chi3; 

%(4,:) : EH1;
A(4,4) = -3*rho; A(4,7) = epsilon*Gamma*R0; A(4,8) = Gamma*Rt; 
B(4,[8 9]) = -chi1; 

%(5,:) : EH2;
A(5,5) = -3*rho; A(5,4) = 3*rho; 
B(5,[8 9]) = -chi2; 

%(6,:) : EH3;
A(6,6) = -3*rho; A(6,5) = 3*rho; 
B(6,[8 9]) = -chi3; 

%(7,:) : T;
A(7,3) = 3*rho; A(7,7) = -Gamma;  A(7,8) = lambda_r; A(7,9) = lambda_s; 
B(7,[8 9]) = fT; 

%(8,:) :  H; 
A(8,6) = 3*rho; A(8,8) = -Gamma-lambda_r;  A(8,9) = -lambda_s; 
B(8,[8 9]) = -fH; 

%(9,:) : Hs; 
A(9,6) = xim*3*rho;  A(9,9) = -lambda_s-Gamma-lambda_r;
B(9,[8 9]) = -fHs; 


%B-Scaling eta*Rt*(Htlag*Lreff+Hslag*Lseff)
B(:,8) = eta*Rt*Lreff*B(:,8);
B(:,9) = eta*Rt*Lseff*B(:,9);
