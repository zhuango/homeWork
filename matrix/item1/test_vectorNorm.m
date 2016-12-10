x = [4, 4, -4, 4];
vectorNorm1(x)
vectorNorm2(x)
vectorNormInfinite(x)

order = 7;
n = 1;
for i = 1:order
    n = 10 * n;
    x = 1 ./ linspace(1, n, n);
    norm(x, 1)
    vectorNorm1(x)
    norm(x, 2)
    vectorNorm2(x)
    norm(x, inf)
    vectorNormInfinite(x)
end
