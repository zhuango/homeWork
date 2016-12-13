lowerBound = 0;
upperBound = pi * 2.0;

ns = [50,100,200,500,1000]
for i = 1:5
    n = ns(i)
    ntegration = complexSimpson(lowerBound, upperBound, n)
end