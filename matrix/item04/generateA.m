function [A] = generateA(n)
    A = eye(n);
    A = A - tril(ones(n), -1);
    A(:, n) = ones(n, 1);
end
