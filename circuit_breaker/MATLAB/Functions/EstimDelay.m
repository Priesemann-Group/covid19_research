function Xdel = EstimDelay(X,a,b,umbral)
%default parameters X:N; a = 4; b = 1; umbral = 0.75;
[Pk,~,F] = GammaProbMass(a,b);
K = linspace(0,99,100); K = K';
idx = F>=umbral; idx = logical(1-idx);
K = K(idx); Pk = Pk(idx)*(1/sum(Pk(idx)));
n = length(K)-1;
Xdel = zeros(n+length(X),1);
for i = 1:length(X)
    dIi = X(i);
    ind = i+K;
    Xdel(ind) = Xdel(ind) +dIi*Pk; 
end
Xdel(end-n+1:end) = [];
