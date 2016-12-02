function [P, L, U] = PLUDecomposes(X)
    n = size(X, 1);
    P = eye(n);
    L = eye(n);
    U = X;
    Ps = zeros(n, n, n - 1);
    Ls = zeros(n, n, n - 1);

    for k = 1:n - 1
        tempP = eye(n);
        tempL = eye(n);
        [placeHolder, index] = max(abs(X(k:end, k)));
        index = index + k - 1;
        tempP([k;index],:) = tempP([index;k],:);
        Ps(:, :, k) = tempP;
        X = tempP * X;
        for i = k + 1:n
            tempL(i, k) = - X(i, k) / X(k, k);
        end
        Ls(:, :, k) = tempL;
        X = tempL * X;
    end
    for i = 1:n - 1
        P = Ps(:, :, i) * P;
        U = Ls(:, :, i) * Ps(:, :, i) * U;
    end
    for i = 1:n - 1
        L_ = Ls(:, :, i);
        for j = i + 1:n - 1
            L_ = Ps(:, :, j) * L_ * Ps(:, :, j);
        end
        L = L_ * L;
    end
    L = L^-1;
end