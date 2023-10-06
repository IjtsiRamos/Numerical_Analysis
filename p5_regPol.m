% Polynomial Regression Example
x = [1, 2, 3, 4, 5, 6, 7];
y = [0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5];


n = length(x);
sum_xi = sum(x);
sum_xi2 = sum(x.^2);
sum_xi3 = sum(x.^3);
sum_xi4 = sum(x.^4);
sumyi = sum(y);
sum_xiyi = sum(x .* y);
sum_xi2yi = sum((x.^2) .* y);

M = [n, sum_xi, sum_xi2;
     sum_xi, sum_xi2, sum_xi3;
     sum_xi2, sum_xi3, sum_xi4];

b = [sumyi; sum_xiyi; sum_xi2yi];

Res = inv(M) * b;
a0_quad = Res(1);
a1_quad = Res(2);
a2_quad = Res(3);

x_aprox_quad = linspace(x(1), x(end), 100);
y_aprox_quad = a0_quad + a1_quad * x_aprox_quad + a2_quad * (x_aprox_quad.^2);

% Fourth-degree Polynomial Regression
sum_xi5 = sum(x.^5);
sum_xi6 = sum(x.^6);
sum_xi7 = sum(x.^7);
sum_xi8 = sum(x.^8);
sum_xi3yi = sum((x.^3) .* y);
sum_xi4yi = sum((x.^4) .* y);

M = [n, sum_xi, sum_xi2, sum_xi3, sum_xi4;
     sum_xi, sum_xi2, sum_xi3, sum_xi4, sum_xi5;
     sum_xi2, sum_xi3, sum_xi4, sum_xi5, sum_xi6;
     sum_xi3, sum_xi4, sum_xi5, sum_xi6, sum_xi7;
     sum_xi4, sum_xi5, sum_xi6, sum_xi7, sum_xi8];

b = [sumyi; sum_xiyi; sum_xi2yi; sum_xi3yi; sum_xi4yi];

Res = inv(M) * b;
a0_poly4 = Res(1);
a1_poly4 = Res(2);
a2_poly4 = Res(3);
a3_poly4 = Res(4);
a4_poly4 = Res(5);

x_aprox_poly4 = linspace(min(x), max(x), 100);
y_aprox_poly4 = a0_poly4 + a1_poly4 * x_aprox_poly4 + a2_poly4 * (x_aprox_poly4.^2) + a3_poly4 * (x_aprox_poly4.^3) + a4_poly4 * (x_aprox_poly4.^4);

% Plotting the results
figure('Position', [0, 0, 1000, 400]);

subplot(1, 2, 1);
plot(x, y, 'o', 'LineWidth', 3);
hold on;
plot(x_aprox_quad, y_aprox_quad, 'r', 'LineWidth', 2);
title('Polynomial calculated');
xlabel('x');
ylabel('y');
legend('Data Points', ['y = ', num2str(a0_quad, '%.2f'), ' + ', num2str(a1_quad, '%.2f'), 'x + ', num2str(a2_quad, '%.2f'), 'x^2'], 'Location', 'northwest');
grid on;

subplot(1, 2, 2);
plot(x, y, 'o', 'LineWidth', 3);
hold on;
plot(x_aprox_poly4, y_aprox_poly4, 'r', 'LineWidth', 2);
title('Polynomial Regression');
xlabel('x');
ylabel('y');
legend('Data Points', ['y = ', num2str(a0_poly4, '%.2f'), ' + ', num2str(a1_poly4, '%.2f'), 'x + ', num2str(a2_poly4, '%.2f'), 'x^2 + ', num2str(a3_poly4, '%.2f'), 'x^3 + ', num2str(a4_poly4, '%.2f'), 'x^4'], 'Location', 'northwest');
grid on;

sgtitle('Polynomial Regression Example', 'FontSize', 16);
