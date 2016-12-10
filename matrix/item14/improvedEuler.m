function [u] = improvedEuler(startPoint, initialValue, endPoint, stepLength)
    stepCount = (endPoint - startPoint) / stepLength;
    u = zeros(stepCount + 1, 1);
    u(1) = initialValue;

    currentPoint = startPoint;

    for i = 1:stepCount
        k1 = improvedEuler_f(currentPoint, u(i));
        k2 = improvedEuler_f(currentPoint + stepLength, u(i) + stepLength .* k1);
        u(i + 1) = u(i) + 0.5 .* stepLength .* (k1 + k2);
        currentPoint += stepLength;
    end
    
end