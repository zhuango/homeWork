function [polCoefficients] = newtonInterpolation(lowerBound, upperBound, numberOfPoint)
    x = linspace(lowerBound, upperBound,numberOfPoint);
    y = newtonInterpolation_f(x);
    previusAverageDeviation = y;
    currentAverageDeviation = y;
    polCoefficients = zeros(numberOfPoint, 1);

    for i = 1:numberOfPoint
        polCoefficients(i) = previusAverageDeviation(1);
        for j = 1:numberOfPoint - i
            currentAverageDeviation(j) = (previusAverageDeviation(j + 1) - previusAverageDeviation(j)) / (x(j + i) - x(j));
        end
        previusAverageDeviation = currentAverageDeviation;
    end
end