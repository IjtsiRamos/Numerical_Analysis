dydx = @(x, y, v) 4 * v + 3 * y - exp(x);
y_x = @(x) (1/2) * exp(x) - (1/2) * exp(3 * x);

% Initial values
step = 0.05;
x_vals = 0:step:0.4;

Y_v = y_x(x_vals);
% Solve the second-order ODE using Heun's method
Y_H = heun_method_second_order(dydx, x_vals, step, 0, -0.03);

% Global Error
E_GE = zeros(size(x_vals));
for k = 1:length(x_vals)
    E_GE(k) = round(((Y_v(k) - Y_H(k)) / Y_v(k)) * 100, 1);
end

% Local Error
E_LE = zeros(size(x_vals));
for k = 1:(length(x_vals) - 1)
    E_LE(k + 1) = round((((Y_v(k) - Y_H(k)) - (Y_v(k + 1) - Y_H(k + 1))) / Y_v(k + 1)) * -100, 2);
end

% Print the exact solution table
df_heun = table(x_vals', Y_v', Y_H', E_GE', E_LE', 'VariableNames', {'x', 'y_verd', 'y_heun', 'Error_Global_Heun', 'Error_Local_Heun'});
disp(df_heun);

subplot(1, 2, 1);
plot(x_vals, Y_v, 'LineWidth', 1.5, 'DisplayName', 'True');
hold on;
plot(x_vals, Y_H, 'o--', 'DisplayName', 'Heun');
xlabel('x');
ylabel('y');
title('Example 1');
legend();
grid on;
hold off;


dydx = @(x, y, v) x^2 - 2*v - y;
y_x = @(x) x.*(1 - x) + 1;

% Initial values
step = 0.05;
x_vals = 0:step:0.5;

Y_v = y_x(x_vals);
% Solve the second-order ODE using Heun's method
Y_H = heun_method_second_order(dydx, x_vals, step, 1, -3.4);

% Global Error
E_GE = zeros(size(x_vals));
for k = 1:length(x_vals)
    E_GE(k) = round(((Y_v(k) - Y_H(k)) / Y_v(k)) * 100, 1);
end

% Local Error
E_LE = zeros(size(x_vals));
for k = 1:(length(x_vals) - 1)
    E_LE(k + 1) = round((((Y_v(k) - Y_H(k)) - (Y_v(k + 1) - Y_H(k + 1))) / Y_v(k + 1)) * -100, 2);
end

% Print the exact solution table
df_heun = table(x_vals', Y_v', Y_H', E_GE', E_LE', 'VariableNames', {'x', 'y_verd', 'y_heun', 'Error_Global_Heun', 'Error_Local_Heun'});
disp(df_heun);

subplot(1, 2, 2);
plot(x_vals, Y_v, 'LineWidth', 1.5, 'DisplayName', 'True');
hold on;
plot(x_vals, Y_H, 'o--', 'DisplayName', 'Heun');
xlabel('x');
ylabel('y');
title('Example 2');
legend();
grid on;
hold off;