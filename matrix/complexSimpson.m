function [integration] = complexSimpson(lowerBound, upperBound, numberOfSections)
    x = linspace(lowerBound, upperBound, numberOfSections + 1);
    integration = 0.0;
    integration += complexSimpson_f(lowerBound);
    integration += complexSimpson_f(upperBound);
    for i = 2:numberOfSections
        integration += 2 .* complexSimpson_f(x(i));
    end
    for i = 1:numberOfSections
        integration += 4 .* complexSimpson_f((x(i + 1) + x(i)) ./ 2.0);
    end
    integration = integration .*  (upperBound - lowerBound) / (6 .* numberOfSections);
end