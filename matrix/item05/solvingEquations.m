for n = 10:20
    A = generateA(n);
    b = rand(n, 1)
    L = choleskyDecomposes(A);
    x = (L') ^ -1 * L ^-1 * b;
    A * x
end
