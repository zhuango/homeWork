function [u] = House(x)
    shape = size(x);
    n = max(shape);
    if shape(1) < shape(2)
        x = x';
    end
    
    e1 = zeros(n, 1);
    e1(1, 1) = 1;

    u = x + vectorNorm2(x) .* e1;
    u = u ./ sqrt(sum(u.*u));
end