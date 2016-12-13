%improvedEuler(0, 0, 2, 0.5)
result = improvedEuler(0, 2, 1, 0.1)
size(result)
subplot(311)
plot(result, '.')

result = improvedEuler(0, 2, 1, 0.01)
subplot(312)
plot(result, '.')

result = improvedEuler(0, 2, 1, 0.001)
subplot(313)
plot(result, '.')
