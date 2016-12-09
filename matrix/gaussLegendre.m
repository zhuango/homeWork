function [integration] = gaussLegendre(coefficients, x)
    integration = 0.0;
    n = max(size(coefficients))
    for i = 1:n
        integration += coefficients(i) .* gaussLegendre_f(x(i));
    end
end
