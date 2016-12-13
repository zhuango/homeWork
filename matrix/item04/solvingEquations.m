format long
for i = 5:30
    n = i
    A = generateA(i);
    x = rand(i, 1)
    b = A * x;

    [P, L, U] = PLUDecomposes(A);
    x_plu = U^-1 * L^-1 * P * b
    A_Ni_plu = U^-1 * L^-1 * P

    [L, U] = LUDecomposes(A);
    x_lu = U^-1 * L^-1 * b
    A_Ni_lu = U^-1 * L^-1
end
