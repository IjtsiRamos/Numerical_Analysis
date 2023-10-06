% Definici�n de las funciones
func1 = @(x) log(x);
func2 = @(x) sin(x);

% N�mero de t�rminos para la serie de Taylor
N = 10;

% Rango de x
x = 0.01:0.01:(2*pi);

% C�lculo de la serie de Taylor y el error para la funci�n ln(x)
taylor1 = zeros(size(x));
for n = 1:N
    taylor1 = taylor1 + ((-1)^(n+1)) * ((x - 1).^n) / n;
end
exact1 = func1(x);
error1 = abs(exact1 - taylor1);

% C�lculo de la serie de Taylor y el error para la funci�n seno
taylor2 = zeros(size(x));
for n = 0:N
    taylor2 = taylor2 + ((-1)^n) * func2((2 * n + 1) * x) / factorial(2 * n + 1);
end
exact2 = func2(x);
error2 = abs(exact2 - taylor2);

% Tabla
table = [x', exact1', taylor1', error1', exact2', taylor2', error2'];
headers = {'x', 'ln(x) (Exact)', 'ln(x) (Approximation)', 'Error', 'sin(x) (Exact)', 'sin(x) (Approximation)', 'Error'};
fprintf('%-10s%-20s%-25s%-15s%-20s%-25s%-15s\n', headers{:});
fprintf('%-10.2f%-20.6f%-25.6f%-15.6f%-20.6f%-25.6f%-15.6f\n', table');

% Gr�ficos
figure;

subplot(2, 2, 1);
plot(x, arrayfun(func1, x), x, taylor1);
title('Funci�n exponencial y aproximaci�n');
xlabel('x');
ylabel('y');

subplot(2, 2, 2);
plot(x, error1);
title('Error en la aproximaci�n de la funci�n exponencial');
xlabel('x');
ylabel('Error');

subplot(2, 2, 3);
plot(x, arrayfun(func2, x), x, taylor2);
title('Funci�n seno y su aproximaci�n');
xlabel('x');
ylabel('y');

subplot(2, 2, 4);
plot(x, error2);
title('Error en la aproximaci�n de la funci�n seno');
xlabel('x');
ylabel('Error');

sgtitle('Aproximaciones de funciones utilizando series de Taylor');

