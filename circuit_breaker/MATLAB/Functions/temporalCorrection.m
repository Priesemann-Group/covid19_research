function chi = temporalCorrection(tc,sumL,tau,tol)
% exponential pool filling and emptying, as some of the individuals that
% become infectious would have been tested by the time of tracing

rt = 1/tc;
if abs(rt-sumL)<=tol
    chi = rt*tau*exp(-rt*tau);
else
    chi = (rt/(sumL-rt))*(exp(-rt*tau)-exp(-sumL*tau));
end
    