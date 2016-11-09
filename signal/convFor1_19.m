function [ut] = u(n)
    ut = double(n >= 0)
end
function [xt] = x(n)
    xt = exp(-3 * n) .* u(n)
end
n = linspace(-8, 8, 17)
ut = u(n)
xt = x(n)
result = conv2(xt, ut)
plot(result)