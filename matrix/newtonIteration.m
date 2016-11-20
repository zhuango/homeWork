function [x] = newtonIteration(initialValue, precision)
    old = initialValue;
    x   = old - newtonIteration_f(old) / newtonIteration_derivative(old);
    format;old, x
    format;error = abs(x - old)
    while abs(x - old) > precision
        old = x;
        x   = old - newtonIteration_f(old) / newtonIteration_derivative(old);
        format;old, x
        format;error = abs(x - old)
    end 
end