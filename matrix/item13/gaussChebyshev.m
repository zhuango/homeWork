function [integration] = gaussChebyshev(numberOfPoint)
    integration = 0.0;
    for i = 0:numberOfPoint - 1
        integration += (pi ./ (numberOfPoint+1)) .* gaussChebyshev_f(cos( (2*i + 1) * pi / ( 2*numberOfPoint+2) ));
    end
end
