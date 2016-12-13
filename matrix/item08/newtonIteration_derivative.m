function [y] = newtonIteration_derivative(x)
    %y = 3 .* x.^2 - 2 .* x - 1;
    y = 1.0 + exp(-x);
    %y = x.^3 + 2.*x.^2 + 10.*x - 100;
    y = 3.*x.^2 + 4.*x + 10;
end