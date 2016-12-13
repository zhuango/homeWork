[x, errors] = newtonIteration(3.4, 1e-10)
plot(errors, 'r')
hold on
[x, errors] = newtonSecant(3.4, 3.6, 1e-10)
plot(errors,'b')

