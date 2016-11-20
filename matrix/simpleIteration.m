function [x] = simpleIteration(initialValue, precision)
    old   = initialValue;
    x     = simpleIteration_phi(old);
    format;old
    format;error = abs(x - old)
    while abs(x - old) > precision
        old = x;
        x = simpleIteration_phi(x);
        format;old
        format;error = abs(x - old)
    end 
end