function [px]  = newtonInterpolation_pol(x, interpolations, polCoefficients)
    n = max(size(polCoefficients));
    px = 0.0;
    for i = 1:n
        temp = 1.0;
        for j = 2:i
            temp = temp .* (x - interpolations(j - 1));
        end
        px += temp .* polCoefficients(i);
    end
end