function [result] = fxBad(x)
    result = zeros(size(x));
    for i = 1:max(size(x))
        if x(i) == 0.0
            result(i) = 1.0;
            continue;
        end
        1.0 + x(i)
        x(i)
        result(i) = log(1.0 + x(i)) ./ x(i);
    end
end