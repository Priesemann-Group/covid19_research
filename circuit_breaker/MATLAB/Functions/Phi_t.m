function Phi = Phi_t(Phi0,Phi1,Phi2,t,t1,t2,D)
% function simulating the linear ramping between adapting the lock-down
% measures. obs: t2-t1 >> D

if t2-t1 < D && t2>t1
    Phi1 = Phi0 + (Phi1-Phi0)*(t2-t1)/D;
    D = t2-t1;
elseif t2 == t1
    Phi1 = Phi0;
end

if length(t) ==1
    if t<t1
        Phi = Phi0;
    elseif t<=(t1+D)
        Phi = Phi0 + (Phi1-Phi0)*(t-t1)/D;
    elseif t<= t2
        Phi = Phi1;
    elseif t<=t2+D
        Phi = Phi1 + (Phi2-Phi1)*(t-t2)/D;
    else
        Phi = Phi2;
    end
else
    Phi = zeros(length(t),1);
    for i = 1:length(t)
        if t(i)<t1
            Phi(i) = Phi0;
        elseif t(i)<=(t1+D)
            Phi(i) = Phi0 + (Phi1-Phi0)*(t(i)-t1)/D;
        elseif t(i)<= t2
            Phi(i) = Phi1;
        elseif t(i)<=t2+D
            Phi(i) = Phi1 + (Phi2-Phi1)*(t(i)-t2)/D;
        else
            Phi(i) = Phi2;
        end
    end
end
