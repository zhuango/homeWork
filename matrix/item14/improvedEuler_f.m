function [yt] = improvedEuler_f(t, y)
    yt = (t .* y - y .* 2) ./ ((t + 1) .^ 2);
    %yt = 1 - (2 .* t .* y) / (1 + t.^2);
end
