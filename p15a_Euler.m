dydx = @(x, y) 2 - exp(-4 * x) - 2 * y;
y_x = @(x) 1 + 0.5 * exp(-4 * x) - 0.5 * exp(-2 * x);

% Initial values
step = 0.1;
x_vals = 0:step:4;

% Exact solution table
Y_v = y_x(x_vals);
Y_E = euler_method(dydx, x_vals, step,1);

% Global Error
E_GE = zeros(size(x_vals));
for k = 1:length(x_vals)
    E_GE(k) = round(((Y_v(k) - Y_E(k)) / Y_v(k)) * 100, 1);
end

% Local Error
E_LE = zeros(size(x_vals));
for k = 1:(length(x_vals) - 1)
    E_LE(k + 1) = round((((Y_v(k) - Y_E(k)) - (Y_v(k + 1) - Y_E(k + 1))) / Y_v(k + 1)) * -100, 2);
end

% Print the exact solution table
df_euler = table(x_vals', Y_v', Y_E', E_GE', E_LE', 'VariableNames', {'x', 'y_verd', 'y_euler', 'Error_Global_Euler', 'Error_Local_Euler'});
disp(df_euler);

subplot(1, 2, 1);
plot(x_vals, Y_v, 'LineWidth', 1.5, 'DisplayName', 'True');
hold on;
plot(x_vals, Y_E, 'o--', 'DisplayName', 'Euler');
xlabel('x');
ylabel('y');
title('Example 1');
legend();
grid on;
hold off;


dydx = @(x, y) -0.5 * exp(x/2) .* sin(5 * x) + 5 * exp(x/2) .* cos(5 * x);
y_x = @(x) exp(x/2) .* sin(5 * x);

% Initial values
step = 0.1;
x_vals = 0:step:4;

% Exact solution table
Y_v = y_x(x_vals);
Y_E = euler_method(dydx, x_vals, step, 0);

% Global Error
E_GE = zeros(size(x_vals));
for k = 1:length(x_vals)
    E_GE(k) = round(((Y_v(k) - Y_E(k)) / Y_v(k)) * 100, 1);
end

% Local Error
E_LE = zeros(size(x_vals));
for k = 1:(length(x_vals) - 1)
    E_LE(k + 1) = round((((Y_v(k) - Y_E(k)) - (Y_v(k + 1) - Y_E(k + 1))) / Y_v(k + 1)) * -100, 2);
end

% Print the exact solution table
df_euler = table(x_vals', Y_v', Y_E', E_GE', E_LE', 'VariableNames', {'x', 'y_verd', 'y_euler', 'Error_Global_Euler', 'Error_Local_Euler'});
disp(df_euler);

subplot(1, 2, 2);
plot(x_vals, Y_v, 'LineWidth', 1.5, 'DisplayName', 'True');
hold on;
plot(x_vals, Y_E, 'o--', 'DisplayName', 'Euler');
xlabel('x');
ylabel('y');
title('Example 2');
legend();
grid on;
hold off;