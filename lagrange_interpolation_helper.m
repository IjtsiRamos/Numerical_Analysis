function result = lagrange_interpolation_helper(t, points)
    n = size(points, 1);
    result = zeros(size(t));

    for i = 1:n
        numerator = ones(size(t));
        denominator = ones(size(t));

        for j = 1:n
            if i ~= j
                numerator = numerator .* (t - points(j, 1));
                denominator = denominator .* (points(i, 1) - points(j, 1));
            end
        end

        result = result + (numerator ./ denominator) .* points(i, 2);
    end

end