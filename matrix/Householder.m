function[H] = House(w)
    shape = size(w);
    n = max(shape);
    if shape(1) < shape(2)
        w = w';
    end
    H = eye(n) - 2 .* ( (w * w') ./ sum(w.*w) );
end