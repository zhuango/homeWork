function[L] = choleskyDecomposes(X)
    n = size(X, 1);
    L = zeros(n, n);
    L(1, 1) = sqrt(X(1, 1));
    for i = 1:n
        sumSquare = 0.0;
        for k = 1:i - 1
            sumSquare += L(i, k) * L(i, k);
        end
        L(i, i) = sqrt(X(i, i) - sumSquare);
        
        for j = i + 1:n
            sumMul = 0.0;
            for k = 1:i - 1;
                sumMul += L(j, k) * L(i, k);
            end
            L(j, i) = (X(j, i) - sumMul) / L(i, i);
        end
    end
end