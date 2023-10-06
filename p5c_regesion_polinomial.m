%% Regresión Polinomial
% Castillo Sazar Joaquín Omar
% En este programa se encuentran las regresiones lineales de tercer, cuarto
% y quinto grado.

%% 
clc
clear all 
close all

%% Datos para hacer la regresión
x= [1 2 3 4 5 6 7];
y=[0.5 2.5 2.0 4.0 3.5 6.0 5.5];
n=length(x);

%% Regresión tercer grado
% Cálculo de los coeficientes utilizando el método de mínimos cuadrados
sum_xi = sum(x);
sum_xi2 = sum(x.^2);
sum_xi3 = sum(x.^3);
sum_xi4 = sum(x.^4);
sum_xi5 = sum(x.^5);
sum_xi6 = sum(x.^6);

sum_yi = sum(y);
sum_xiyi = sum(x.*y);
sum_xi2yi = sum((x.^2).*y);
sum_xi3yi = sum((x.^3).*y);



M = [n       sum_xi   sum_xi2    sum_xi3
     sum_xi  sum_xi2  sum_xi3    sum_xi4
     sum_xi2 sum_xi3  sum_xi4    sum_xi5
     sum_xi3 sum_xi4  sum_xi5    sum_xi6];

b = [sum_yi
     sum_xiyi
     sum_xi2yi
     sum_xi3yi];

Res = inv(M) * b;
a0 = Res(1);
a1 = Res(2);
a2 = Res(3);
a3 = Res(4);

% Cálculo de los puntos de la curva de regresión
x_aprox=x(1):(x(n)-x(1))/100:x(n);
y_aprox = a0 + a1*x_aprox + a2*(x_aprox.^2) + a3*(x_aprox.^3);


% Coeficiente de correlación
media_y = sum(y) / n;
St = sum((y - media_y).^2);
Sr = sum((y - (a0 + a1*x + a2*(x.^2) + a3*(x.^3))).^2);
r2 = (St - Sr) / St;
r = sqrt(r2);



figure()
subplot(1,2,1);plot(x,y,'o','Linewidth',3)
title('Regresión cubica manual');
xlabel('x')
ylabel('y')
grid on;
hold on;
plot(x_aprox,y_aprox,'r','Linewidth',2);
xlabel('x');
ylabel('y')
legend({'Puntos', 'y = ' + string(a0) + '+' + string(a1) + 'x' + string(a2) + 'x^2' + string(a3) + 'x^3' }, 'Location', 'northwest')

% Usando la función polyfit
p = polyfit(x, y, 3);
x_aux = x(1):0.01:x(end);
y_aux = polyval(p, x_aux);

subplot(1,2,2);plot(x, y, 'o', 'LineWidth', 2)
grid on
hold on
plot(x_aux, y_aux, 'r', 'LineWidth', 3)
title('Regresión cubica con Polyfit');
xlabel('x');
ylabel('y');
legend({'Puntos', 'y = ' + string(a0) + '+' + string(a1) + 'x' + string(a2) + 'x^2' + string(a3) + 'x^3' }, 'Location', 'northwest')


%% Regresión cuarto grado
% Puntos aleatorios
x = [1 2 3 4 5 6 7];
y = [0.5 2.5 2.0 4.0 3.5 6.0 5.5];
n = length(x);

% Cálculo de los coeficientes utilizando el método de mínimos cuadrados
sum_xi = sum(x);
sum_xi2 = sum(x.^2);
sum_xi3 = sum(x.^3);
sum_xi4 = sum(x.^4);
sum_xi5 = sum(x.^5);
sum_xi6 = sum(x.^6);
sum_xi7 = sum(x.^7);
sum_xi8 = sum(x.^8);

sum_yi = sum(y);
sum_xiyi = sum(x.*y);
sum_xi2yi = sum((x.^2).*y);
sum_xi3yi = sum((x.^3).*y);
sum_xi4yi = sum((x.^4).*y);

M = [n       sum_xi   sum_xi2    sum_xi3    sum_xi4
     sum_xi  sum_xi2  sum_xi3    sum_xi4    sum_xi5
     sum_xi2 sum_xi3  sum_xi4    sum_xi5    sum_xi6
     sum_xi3 sum_xi4  sum_xi5    sum_xi6  sum_xi7
     sum_xi4 sum_xi5  sum_xi6  sum_xi7  sum_xi8];

b = [sum_yi
     sum_xiyi
     sum_xi2yi
     sum_xi3yi
     sum_xi4yi];

Res = inv(M) * b;
a0 = Res(1);
a1 = Res(2);
a2 = Res(3);
a3 = Res(4);
a4 = Res(5);

% Cálculo de los puntos de la curva de regresión
x_aprox = linspace(min(x), max(x), 100);
y_aprox = a0 + a1*x_aprox + a2*(x_aprox.^2) + a3*(x_aprox.^3) + a4*(x_aprox.^4);

figure()
subplot(1,2,1);plot(x,y,'o','Linewidth',3)
title('Regresión de cuarto orden manual');
xlabel('x')
ylabel('y')
grid on;
hold on;
plot(x_aprox,y_aprox,'r','Linewidth',2);
xlabel('x');
ylabel('y')
legend({'Puntos', 'y = ' + string(a0) + '+' + string(a1) + 'x' + string(a2) + 'x^2' + string(a3) + 'x^3' }, 'Location', 'northwest')

% Usando la función polyfit
p = polyfit(x, y, 4);
x_aux = x(1):0.01:x(end);
y_aux = polyval(p, x_aux);

subplot(1,2,2);plot(x, y, 'o', 'LineWidth', 2)
grid on
hold on
plot(x_aux, y_aux, 'r', 'LineWidth', 3)
title('Regresión de cuarto orden con Polyfit');
xlabel('x');
ylabel('y');
legend({'Puntos', 'y = ' + string(a0) + '+' + string(a1) + 'x' + string(a2) + 'x^2' + string(a3) + 'x^3' }, 'Location', 'northwest')
