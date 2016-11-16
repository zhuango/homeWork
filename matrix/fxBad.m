function [result] = fxBad(x)
    d = 1 + x;
    if d == 1
        result = 1.0;
        return
    end
    result = log(d) / (d - 1);
end