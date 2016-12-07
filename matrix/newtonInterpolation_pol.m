function [px]  = newtonInterpolation_pol(x, interpolations, polCoefficients)
    n = size(polCoefficients);
    px = 0;
    for i = 1:n
        temp = 1.0;
        for j = 2:i
            temp = temp .* (x - interpolations(j - 1));
        px += temp .* polCoefficients(i);
    end
end