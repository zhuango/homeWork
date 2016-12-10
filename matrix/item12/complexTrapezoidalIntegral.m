function [integration] = complexTrapezoidalIntegral(lowerBound, upperBound, numberOfSections)
    x = linspace(lowerBound, upperBound, numberOfSections + 1);
    integration = 0.0;
    integration += complexTrapezoidalIntegral_f(lowerBound);
    integration += complexTrapezoidalIntegral_f(upperBound);

    for i = 2:numberOfSections
        integration += 2 .* complexTrapezoidalIntegral_f(x(i));
    end
    integration = integration .*  (upperBound - lowerBound) / (2 .* numberOfSections);
end