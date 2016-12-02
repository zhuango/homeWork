function [singleRootSections] = singleRootSection(lowerBound, upperBound, numberOfRoot)
    singleRootSections = zeros(numberOfRoot, 2);
    n = 0;
    iteration = 1;
    while(n < numberOfRoot)
        n = 0;
        numberOfSection = numberOfRoot * iteration;
        stepLength = (lowerBound + upperBound) / numberOfSection;
        tinySectionLowerBound = lowerBound;
        tinySectionUpperBound = lowerBound + stepLength;
        while tinySectionUpperBound < upperBound
            if rootByDichotomy_f(tinySectionLowerBound) * rootByDichotomy_f(tinySectionUpperBound) < 0
                singleRootSections(n + 1, :) = [tinySectionLowerBound, tinySectionUpperBound];
                n += 1;
            end
            tinySectionLowerBound += stepLength;
            tinySectionUpperBound += stepLength;
        end
        iteration += 1;
    end

end