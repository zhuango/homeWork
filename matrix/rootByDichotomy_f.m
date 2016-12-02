function [y] = rootByDichotomy_f(x)
    y = exp(x) .* cos(x) + 2;
end