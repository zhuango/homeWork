function [x] = newtonIteration(initialValue, precision, lambda = 1.0)
    old = initialValue;
    x   = old - lambda * newtonIteration_f(old) / newtonIteration_derivative(old);
    format;old, x
    format;error = abs(x - old)
    while abs(x - old) > precision
        old = x;
        x   = old - lambda * newtonIteration_f(old) / newtonIteration_derivative(old);
        format;old, x
        format;error = abs(x - old)
    end 
end