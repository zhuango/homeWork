function [HxA] = HA(A)
    u = House(A(:,1));
    HxA = A - 2 * (u * u') * A;
end
