function y_euler = euler_method(dydx, x, step, initial_y)
    num_steps = length(x);
    y_euler = zeros(1, num_steps);
    y_euler(1) = initial_y;
    for k = 1:num_steps-1
        f = dydx(x(k), y_euler(k));
        y_euler(k + 1) = y_euler(k) + f * step;
    end
end

