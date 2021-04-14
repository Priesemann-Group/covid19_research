function [Dopt,x,t] = LD_SEIR(M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,ti,tf,tap,t1,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,x0,tol,R0,Neqcrit)

tspan = [ti tf];
lags = 1;
dlim = tf-t1-2*D;
for d = 1:dlim
    t2 = t1+d;
    sol = dde23(@(t,x,Z) dde_tti_SEIR(t,x,Z,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0), lags, @(t) history(t,x0), tspan);
    x = sol.y; t = sol.x;
    [~,Nobs1,~,~,ts,~] = dailyCases_SEIR(sol,M,xi,tc,tau,nu,Rt,Gamma,lambda_s,lambda_r,eta,epsilon,nmax,Phi0,Phild,t1,t2,D,Rtld,Rtald,phi,lambda_s2,lambda_r2,R0);
    if d>=10*7
        Dopt = NaN;
        break
    end
    if Nobs1(ts==t1+d)<=Neqcrit %(Nobs1(ts==tap)-Nobs1(ts==(tap-1)))<-tol
        Dopt = d;
        %nref = Nobs1(ts==t2+3*D);
        break
    end
end


