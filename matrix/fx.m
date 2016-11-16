function [result] = fx(x)
    if x == 0
        result = 1.0;
        return
    end
    result = log(1 + x) / x;
end