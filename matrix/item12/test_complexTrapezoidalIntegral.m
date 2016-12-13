lowerBound = 0;
upperBound = pi * 2.0;

ns = [50,100,200,500,1000, 2000, 3000, 30000]
for i = 1:8
    n = ns(i)
    ntegration = complexTrapezoidalIntegral(lowerBound, upperBound, n)
end