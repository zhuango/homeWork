function [y] = newtonIteration_f(x)
    %y = x.^3 - x.^2 - x - 1;
    %y = x - exp(-x);
    y = x.^3 + 2.*x.^2 + 10.*x - 100;
end