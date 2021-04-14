function [A,B] = linStab_tti_cb(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0)
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
chi         = exp(-tau/tc);
chimr       = temporalCorrection(tc,lambda_r,tau,tol);
chimrs      = temporalCorrection(tc,lambda_s+lambda_r,tau,tol);
fT          = xi*chimr + xim*chimrs;
fH          = fT;
fHs         = xim*chimrs;


%% Calculo de las matrices
A = zeros(5); B = A;
%(1,:) : ET; 
A(1,1) = -1/tc; A(1,3) = nu*Gamma*R0; 
B(1,[4 5]) = chi; 

%(2,:) : EH;
A(2,2) = -1/tc; A(2,3) = epsilon*Gamma*R0; A(2,4) = Gamma*Rt; 
B(2,[4 5]) = -chi; 

%(3,:) : T;
A(3,1) = 1/tc; A(3,3) = -Gamma;  A(3,4) = lambda_r; A(3,5) = lambda_s; 
B(3,[4 5]) = fT; 

%(4,:) :  H; 
A(4,2) = 1/tc; A(4,4) = -Gamma-lambda_r;  A(4,5) = -lambda_s; 
B(4,[4 5]) = -fH; 

%(5,:) : Hs; 
A(5,2) = xim/tc;  A(5,5) = -lambda_s-Gamma-lambda_r;
B(5,[4 5]) = -fHs; 


%B-Scaling eta*Rt*(Htlag*Lreff+Hslag*Lseff)
B(:,4) = eta*Rt*Lreff*B(:,4);
B(:,5) = eta*Rt*Lseff*B(:,5);
