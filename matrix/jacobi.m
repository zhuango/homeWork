function [x] = jacobi(A, b, initialValues, steps)
    order = size(A, 1);
    D = eye(order) .* A;
    L = -tril(A, -1);
    U = -triu(A,  1);

    BJ = D ^ -1 * (L + U);
    f  = D ^ -1 * b;

    x = initialValues;
    for i = 1:steps
        x = BJ * x + f;
    end
end
