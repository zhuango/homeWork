for n = 10:20
    A = generateA(n);
    b = rand(n, 1)
    L = choleskyDecomposes(A);
    % x = (L') ^ -1 * L ^-1 * b;
    y = zeros(n, 1);
    
    y(1) = b(1) / L(1, 1) ;
    for i = 2:n
        sumLY = 0.0;
        for k = 1:i-1
            sumLY += L(i, k) * y(k);
        end
        y(i) = (b(i) - sumLY) / L(i, i);
    end

    x = zeros(n, 1);
    x(n) = y(n) / L(n, n) ;
    i = n -1 ;
    while i > 0
        sumLX = 0.0;
        for k = i + 1:n
            sumLX += L(k, i) * x(k);
        end
        x(i) = (y(i) - sumLX) / L(i, i);
        i -= 1;
    end
    b = A * x
end
