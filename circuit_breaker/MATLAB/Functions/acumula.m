function F = acumula(t,f)
F = zeros(size(t));
for i = 2:length(t)
    F(i) = trapz(t(1:i),f(1:i));
end