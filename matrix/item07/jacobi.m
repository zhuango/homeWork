function [x] = jacobi(A, b, initialValues, precision, maxSteps = 100)
    order = size(A, 1);
    D = eye(order) .* A;
    L = -tril(A, -1);
    U = -triu(A,  1);

    BJ = D ^ -1 * (L + U);
    f  = D ^ -1 * b;

    x    = initialValues;
    oldx = x;
    for i = 1:maxSteps
        x = BJ * x + f;

        error = abs(x - oldx)
        if max(error) < precision
            break
        end

        oldx = x;
    end
end
