%interpolations = [1, 2, 3]';
interpolations = linspace(-5, 5, 10);
x = linspace(-5, 5, 100);

subplot(211)
plot(x, lagrangeInterpolation_pol(interpolations, x))
subplot(212)
plot(x, lagrangeInterpolation_f(x))