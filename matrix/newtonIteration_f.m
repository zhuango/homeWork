function [y] = newtonIteration_f(x)
    %y = x.^3 - x.^2 - x - 1;
    y = x - exp(-x);
end