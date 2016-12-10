function [px] = lagrangeInterpolation_pol(interpolations, x)
    n = max(size(interpolations));
    y = lagrangeInterpolation_f(interpolations);
    px = zeros(size(x));
    for i = 1:n
        numerator   = 1.0;
        denominator = 1.0;
        for j = 1:i - 1
            numerator = numerator .* (x - interpolations(j));
            denominator = denominator .* (interpolations(i) - interpolations(j));
        end
        for j = i + 1: n
            numerator = numerator .* (x - interpolations(j));
            denominator = denominator .* (interpolations(i) - interpolations(j));
        end
        px += y(i) .* (numerator ./ denominator);
    end
end