function [result] = fxBad(x)
    result = zeros(size(x));
    d = 1 + x;
    for i = 1:max(size(x))
        if d(i) == 1
            result(i) = 1.0;
            continue
        end
        result(i) = log(d(i)) ./ (d(i) - 1);
    end
end