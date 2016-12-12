function [result] = fx(x)
    result = zeros(size(x));
    for i = 1:max(size(x))
        if x(i) == 0.0
            result(i) = 1.0;
            continue;
        end
        result(i) = log(1.0 + x(i)) ./ x(i);
    end
end