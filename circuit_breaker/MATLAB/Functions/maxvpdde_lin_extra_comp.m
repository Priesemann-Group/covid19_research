function L = maxvpdde_lin_extra_comp(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0)
[A0,A1] = linStab_tti_extra_comp(xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,R0);
N=10; n=length(A0); % Discretization nodes N and size of DDE n
D=-cheb(N-1)*2/tau;
ei1 = eig([kron(D(1:N-1,:),eye(n));[A1,zeros(n,(N-2)*n), A0]]);
L = max(real(ei1));
end