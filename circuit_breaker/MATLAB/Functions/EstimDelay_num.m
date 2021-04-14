function Xdel = EstimDelay_num(X)
%default parameters X:N; a = 4; b = 1; umbral = 0.75;
Pk = [0 0 0.5 0.3 0.1 0.1]';
K = linspace(0,5,6); K = K'; 
n = length(K)-1;
Xdel = zeros(n+length(X),1);
for i = 1:length(X)
    dIi = X(i);
    ind = i+K;
    Xdel(ind) = Xdel(ind) +dIi*Pk; 
end
Xdel(end-n+1:end) = [];
