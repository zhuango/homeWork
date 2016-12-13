%interpolations = [1, 2, 3]';
interpolations = linspace(-5, 5, 10);
x = linspace(-5, 5, 100);

%subplot(211)
for i = 4:10
    interpolations = linspace(-5, 5, i);
    plot(x, lagrangeInterpolation_pol(interpolations, x))
    hold on
end

%subplot(212)
plot(x, lagrangeInterpolation_f(x), 'r')