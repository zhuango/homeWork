function [u] = euler(startPoint, initialValue, endPoint, stepLength)
    stepCount = (endPoint - startPoint) / stepLength;
    u = zeros(stepCount + 1, 1);
    u(1) = initialValue;

    currentPoint = startPoint;

    for i = 1:stepCount
        u(i+1) = u(i) + stepLength .* euler_f(currentPoint, u(i));
        currentPoint += stepLength;
    end
end
