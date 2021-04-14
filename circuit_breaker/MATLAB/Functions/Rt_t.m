function Rt = Rt_t(Rt0,Rt1,Rt2,t,t1,t2,D)
% function simulating the linear ramping between adapting the lock-down
% measures. obs: t2-t1 >> D

if t2-t1 < D && t2>t1
    Rt1 = Rt0 + (Rt1-Rt0)*(t2-t1)/D;
    D = t2-t1;
elseif t2 == t1
    Rt2 = Rt0;
    Rt1 = Rt2;
    D = 1e-3;
end

if length(t) ==1
    if t<t1
        Rt = Rt0;
    elseif t<=(t1+D)
        Rt = Rt0 + (Rt1-Rt0)*(t-t1)/D;
    elseif t<= t2
        Rt = Rt1;
    elseif t<=t2+D
        Rt = Rt1 + (Rt2-Rt1)*(t-t2)/D;
    else
        Rt = Rt2;
    end
else
    Rt = zeros(length(t),1);
    for i = 1:length(t)
        if t(i)<t1
            Rt(i) = Rt0;
        elseif t(i)<=(t1+D)
            Rt(i) = Rt0 + (Rt1-Rt0)*(t(i)-t1)/D;
        elseif t(i)<= t2
            Rt(i) = Rt1;
        elseif t(i)<=t2+D
            Rt(i) = Rt1 + (Rt2-Rt1)*(t(i)-t2)/D;
        else
            Rt(i) = Rt2;
        end
    end
end

