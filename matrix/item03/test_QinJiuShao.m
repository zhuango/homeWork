QinJiuShao([1, -6.1, 3.2, 1.5], 4.71) % -14.264

% x9 − 18 x8 + 144 x7 − 672 x6 + 2016 x5 − 4032 x4 + 5376 x3 − 4608 x2 + 2304 x − 512
x = linspace(1.95, 20.5, 200);
results = QinJiuShao([1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512], x);
subplot(211)
plot(x,results);
subplot(212)
plot(x, (x-2).^9)
