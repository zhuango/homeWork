function [integration] = romberg(lowerBound, upperBound, error)
    T = [0.5 * (romberg_f(lowerBound) + romberg_f(upperBound))]
    old =T(1);
    while true
        n = max(size(T)) + 1;
        newT = zeros(n, 1);

        newT(1) = 0;
        for j = 0: 2.^(n - 2) - 1
            newT(1) += romberg_f(lowerBound + (2 .* j + 1) .* (upperBound - lowerBound) ./ 2.^(n - 1));
        end
        newT(1) = newT(1) .*(upperBound - lowerBound) / 2.^(n - 1) + 0.5 .* T(1);

        for i = 2:n
            newT(i) = (4 .^ (i - 1) .* newT(i - 1)  - T(i - 1)) ./ (4 .^ (i - 1) - 1);
        end
        if abs(newT(n) - old) < error
            integration = newT(n);
            newT

            return ;
        end
        old = newT(n);
        T = newT
    end
end
