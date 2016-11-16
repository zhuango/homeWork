n = linspace(-8, 8, 17)
N = 17
M = 17
ut = double(n >= 0.0);
ht = exp(-3.0 .* n) .* double(n >= 0.0);

ut=[ut,zeros(1,N-1)];
ht=[ht,zeros(1,M-1)];

sum = 0;
for m=1:M+N-1
    for n=1:m
        sum = sum + ut(n)*ht(m+1-n);
    end
    result(m)=sum;
    sum=0;
end
plot(result)