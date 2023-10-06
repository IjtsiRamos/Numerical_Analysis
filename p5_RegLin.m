% Define data points
x = [1, 2, 3, 4, 5];
y = [1, 4, 7, 8, 11];

% Calculate the coefficients
n = length(x);
sum_xi = sum(x);
sum_yi = sum(y);
sum_xi2 = sum(x.^2);
sum_xiyi = sum(x.*y);

A = [n, sum_xi; sum_xi, sum_xi2];
b = [sum_yi; sum_xiyi];

r = inv(A) * b;  % Coefficients of the linear regression a0 and a1

a0 = r(1);
a1 = r(2);

% Calculate the points of the line using the coefficients
x_aux = x(1):0.01:x(end);
y_aux = a0 + a1 * x_aux;

% Plot the data points and the line
figure;
plot(x, y, 'o', 'LineWidth', 2);
grid on;
hold on;
plot(x_aux, y_aux, 'r', 'LineWidth', 3);
title('Linear Regression');
xlabel('x');
ylabel('y');
legend('Data Points', ['y = ' num2str(a0) ' + ' num2str(a1) 'x'], 'Location', 'best');

% Calculate the coefficient of determination (R-squared)
mean_y = mean(y);
St = sum((y - mean_y).^2);
Sr = sum((y - a0 - a1*x).^2);
r2 = (St - Sr) / St;
r = sqrt(r2);  % Percentage of approximation to the overall data behavior

% Display the equation of the line
equation = ['y = ' num2str(a0) ' + ' num2str(a1) 'x'];
disp(equation);

% Fit the line using polyfit
p = polyfit(x, y, 1);
ap1 = p(1);
ap0 = p(2);

y_aux_poly = polyval(p, x_aux);

% Plot the data points and the line fitted using polyfit
figure;
plot(x, y, 'o', 'LineWidth', 2);
grid on;
hold on;
plot(x_aux, y_aux_poly, 'r', 'LineWidth', 3);
title('Linear Regression with polyfit');
xlabel('x');
ylabel('y');
legend('Data Points', ['y = ' num2str(ap0) ' + ' num2str(ap1) 'x'], 'Location', 'best');
