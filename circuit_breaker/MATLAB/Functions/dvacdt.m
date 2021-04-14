function v = dvacdt(t,V)
% function that calculates the daily rate of vaccination, starting at time
% t_start, ending at time t_end. we assume that effectively, a fraction
% k_eff of those individuals being vaccinated would be fully sterile to the
% virus. Vaccine logistics are parameterized by a,b,c.

t_start     = V(1); 
t_end       = V(2); 
kappa_eff   = V(3); 
a           = V(4);  
b           = V(5);
t_ref       = V(6);

t = t-t_start;
v = kappa_eff * a * 1./(1+exp(b*(t-t_ref)));
idx         = t>t_end | t<t_start;
v(idx)      = 0;
