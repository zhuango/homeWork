fx(0)
fx(-1e-15)
fx(1e-15)
x = linspace(-1e-15, 1e-15, 500);
subplot(211);
axis([-1e-15 1e-15])
plot(x, fx(x));

fxBad(0)
fxBad(-1e-15)
fxBad(1e-15)
x = linspace(-1e-15, 1e-15, 500);
subplot(212);
axis([-1e-15 1e-15])
plot(x, fxBad(x));