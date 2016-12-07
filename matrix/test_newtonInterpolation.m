lowerBound = 0;
upperBound = 1;
numberOfPoint = 10;
polCoefficients = newtonInterpolation(lowerBound, upperBound, numberOfPoint)
interpolations = linspace(lowerBound, upperBound, numberOfPoint);
x = linspace(lowerBound, upperBound, 100);
subplot(211)
plot(x, newtonInterpolation_pol(x, interpolations, polCoefficients));
subplot(212)
plot(x, newtonInterpolation_f(x))