function [x] = newtonSecant(initialValue0, initialValue1, precision)
    old0 = initialValue0;
    old1 = initialValue1;
    approxDerivative = (newtonSecant_f(old1) - newtonSecant_f(old0)) / (old1 - old0);
    x   = old1 - newtonSecant_f(old1) / approxDerivative;
    % format;old0, old1, x
    % format;error = abs(x - old1)
    while abs(x - old1) > precision
        old0 = old1;
        old1 = x;
        approxDerivative = (newtonSecant_f(old1) - newtonSecant_f(old0)) / (old1 - old0);
        x   = old1 - newtonSecant_f(old1) / approxDerivative;
        % format;old0, old1, x
        % format;error = abs(x - old1)
    end 
end