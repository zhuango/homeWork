%A = reshape([8, 4, 2, -3, 11, 1, 2, -1, 4], 3, 3);
%b = [20, 33, 12]';

%x = gaussSeidel(A, b, [0, 0, 0]', 10)
%x = jacobi(A, b, [0, 0, 0]', 10)

A = reshape([2, 1, 1, -1, 1, 1, 1, 1, -2], 3, 3);
b = [1, 1, 1]';

gaussSeidel_x = gaussSeidel(A, b, [0, 0, 0]', 10)

A = reshape([1, -1, -2, -2, 1, -2, 2, -1, 1], 3, 3);
b = [1, 1, 1]';

jacobi_x = jacobi(A, b, [0, 0, 0]', 10)