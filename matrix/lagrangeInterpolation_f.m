function [y] = lagrangeInterpolation_f(x)
    %y = x .^ 2 - 3 .* x + 1;
    y = 1 ./ (1 + x.^ 2);
end
