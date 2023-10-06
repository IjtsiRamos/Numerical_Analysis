%% Castillo Salazar Joaquín Omar
% Analisis Númerico
% Interpolación segmentaria (lineal)
% Chapra, S. C., Canale, R. P., Ruiz, R. S. G., Mercado, V. H. I., Díaz, E. M., & Benites, G. E.
% (2011). Métodos numéricos para ingenieros (Vol. 5, pp. 154-196). New York, NY, USA: McGraw-Hill.


clear all;
close all;
clc;

%Valores de los datos
x=[3.0 4.5 7.0 9.0];
f_x=[2.5 1.0 2.5 0.5];

%Longitud de los datos
n=length(x);

%Graficamos los puntos
figure
subplot(211);plot(x,f_x,'bo','LineWidth',3);
title('Interpolación de primer orden manual')
xlabel('x');
ylabel('f(x)'); 
axis([x(1) x(n) f_x(n) f_x(1)]);
hold on

m=zeros(length(x));

for k=1:n-1
    %Calculamos la pendiente 
    m(k)=(f_x(k+1) - f_x(k))/(x(k+1)-x(k));
    
    %Aplicamos la funcion lineal
    x_aux= x(k):0.01: x(k+1);
    f_aux= f_x(k) + m(k)*(x_aux - x(k));
    
    plot(x_aux,f_aux,'r','LineWidth',3);
    grid on;
end


%% Interpolación con funcion de spline
% Puntos de evaluación
xi = linspace(min(x), max(x), 100);
% Interpolación lineal con spline de grado 1
yi = interp1(x, f_x, xi, 'linear');


subplot(212);plot(x, f_x, 'o', xi, yi, '-')
title('Interpolación Segmentaria Lineal matlab')
xlabel('x')
ylabel('f_x')
