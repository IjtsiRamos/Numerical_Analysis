function y_heun = heun_method_second_order(f, x, step, initial_y, initial_v)
    num_steps = length(x);
    y_heun = zeros(1, num_steps);
    v_heun = zeros(1, num_steps);
    y_heun(1) = initial_y;
    v_heun(1) = initial_v;
    
    for k = 1:(num_steps - 1)
        f1 = v_heun(k);
        f2 = f(x(k), y_heun(k), v_heun(k));
        y_predictor = y_heun(k) + f1 * step;
        v_predictor = v_heun(k) + f2 * step;
        f3 = f(x(k + 1), y_predictor, v_predictor);
        y_heun(k + 1) = y_heun(k) + ((f1 + f3) / 2) * step;
        v_heun(k + 1) = v_heun(k) + ((f2 + f3) / 2) * step;
    end
end


