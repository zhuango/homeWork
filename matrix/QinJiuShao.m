function [result] = QinJiuShao(coefficients, x)
    order = size(coefficients, 2)
    result = coefficients(1)
    for i = 2:order
        result = result .* x + coefficients(i)
    end
end