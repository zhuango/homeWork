function[L, U] = LUDecomposes(X)
    n = size(X, 1);
    L = eye(n);
    U = zeros(size(X));

    for j = 1:n
        U(1, j) = X(1, j);
        if j > 1
            L(j, 1) = X(j, 1) / U(1, 1);
        end
    end

    for i = 2:n
        for j = i:n
            sum = 0;
            for k = 1:i - 1
                sum = sum + L(i, k) * U(k, j);
            end
            U(i, j) = X(i, j) - sum;
        end
        if i < n
            for j = i + 1:n
                sum = 0;
                for k = 1:i - 1
                    sum = sum + L(j, k) * U(k, i);
                end
                L(j, i) = (X(j, i) - sum) / U(i, i);
            end
        end
    end
end
