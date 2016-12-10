function [u] = classicRungeKutta(startPoint, initialValue, endPoint, stepLength)
    stepCount = (endPoint - startPoint) / stepLength;
    u = zeros(stepCount + 1, 1);
    u(1) = initialValue;

    currentPoint = startPoint;
    
    for i = 1:stepCount
        k1 = classicRungeKutta_f(currentPoint, u(i));
        k2 = classicRungeKutta_f(currentPoint + 0.5 .* stepLength, u(i) + 0.5 .* stepLength .* k1);
        k3 = classicRungeKutta_f(currentPoint + 0.5 .* stepLength, u(i) + 0.5 .* stepLength .* k2);
        k4 = classicRungeKutta_f(currentPoint + stepLength, u(i) + stepLength .* k3);
        u(i + 1) = u(i) + stepLength ./ 6 .* (k1 + 2.*k2 + 2.*k3 + k4);
        currentPoint += stepLength;
    end
end