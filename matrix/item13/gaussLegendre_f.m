function [y] = gaussLegendre_f(x)
    y = sin(pi / 4 + pi / 4 .* x) ./ (1 + x);
    %y = x.^ 2 / ((1-x.^2).^0.5);
    %y = sin(0.5 + 0.5 .* x) ./ (1 + x);
end