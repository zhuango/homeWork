function [x] = gaussSeidel(A, b, initialValues, steps)
    order = size(A, 1);
    D = eye(order) .* A
    L = -tril(A, -1);
    U = -triu(A,  1);

    BG = (D - L) ^ -1 * U;
    f  = (D - L) ^ -1 * b;

    x = initialValues;
    for i = 1:steps
        x = BG * x + f;
    end
end
