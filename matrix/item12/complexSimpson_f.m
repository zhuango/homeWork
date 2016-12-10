function [y] = complexSimpson_f(x)
    %y = 1.0 / (1.0 + x);
    y = exp(3 .* x) .* cos(pi .* x);
end
