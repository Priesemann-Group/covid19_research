function [a,b] = findBparam(mu,var)

x = (mu*(1-mu)/var)-1;
a = mu*x;
b = (1-mu)*x;