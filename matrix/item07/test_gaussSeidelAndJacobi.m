%A = reshape([8, 4, 2, -3, 11, 1, 2, -1, 4], 3, 3);
%b = [20, 33, 12]';

%x = gaussSeidel(A, b, [0, 0, 0]', 1e-3)
%x = jacobi(A, b, [0, 0, 0]', 1e-3)

A = reshape([2, 1, 1, -1, 1, 1, 1, 1, -2], 3, 3);
b = [1, 1, 1]';
gaussSeidel_x = gaussSeidel(A, b, [0, 0, 0]', 1e-3)

A = reshape([1, -1, -2, -2, 1, -2, 2, -1, 1], 3, 3);
b = [1, 1, 1]';
jacobi_x = jacobi(A, b, [0, 0, 0]', 1e-3)


A = reshape([5, -1, -3, -1, 2, 4, -3, 4, 15], 3, 3);
b = [-2, 1, 10]';
gaussSeidel_x = gaussSeidel(A, b, [0, 0, 0]', 1e-3)


A = reshape([5, -1, -3, -1, 2, 4, -3, 4, 15], 3, 3);
b = [-2, 1, 10]';
jacobi_x = jacobi(A, b, [0, 0, 0]', 1e-3, 1000)