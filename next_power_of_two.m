function n = next_power_of_two(i)
    n = 2;
    while n < i
        n = n * 2;
    end
end