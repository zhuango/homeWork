function [x] = rootByDichotomy(lowerBound, upperBound, precision)
    f0 = rootByDichotomy_f(lowerBound);
    f1 = rootByDichotomy_f(upperBound);
    if f0 * f1 > 0
        root = lowerBound;
    end
    x = lowerBound;

    while true
        old = x;
        x  = (lowerBound + upperBound) / 2;
        f  = rootByDichotomy_f(x);
        f0 = rootByDichotomy_f(lowerBound);
        f1 = rootByDichotomy_f(upperBound);
        if abs(old -x) < precision
            break;
        end
        if f * f0 < 0
            upperBound = x
        end
        if f * f1 < 0
            lowerBound = x
    end

end