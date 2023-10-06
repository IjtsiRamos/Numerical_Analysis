clear all;
close all;
clc;

%sen(x)=x-x^impares(3,5..)/factorial(impares) 
% Numero de terminos de la serie
n=16;
% Valor al cual se quiere aproximar la funcion de seno
x=0.645772;
% Valor verdadero
Vv=round(sin(x),4);
%Vv=0.601815164320527;
% 1a Aproximacion
sin_x=round(x,4);
% Aproximacion del valor del termino de la serie
Va=sin_x;
Aact=sin_x;
Aant=0;
% Error verdadero (Et)-> t = true
Et=abs(((Vv-Va)/Vv)*100);
% Error aproximado (Ea)->  = approximate
Ea=abs(((Aact-Aant)/Aact)*100);
Es=(0.5)*10^(2-n);
m=3;
while Va~=Vv
    Aant=Va;
    sin_x=round(sin_x-(x^m)/(factorial(m)),4);
    Va=sin_x;
    Aact=sin_x;
    Et_new=abs((Vv-Va)/Vv)*100;
    Et=[Et,Et_new];
    Ea_new=abs((Aact-Aant)/Aact)*100;
    Ea=[Ea,Ea_new];
    m=m+2;
    Aant=Va;
    sin_x=round(sin_x+(x^m)/(factorial(m)),4);
    Va=sin_x;
    Aact=sin_x;
    Et_new=abs((Vv-Va)/Vv)*100;
    Et=[Et,Et_new];
    Ea_new=abs((Aact-Aant)/Aact)*100;
    Ea=[Ea,Ea_new];
    m=m+2;
end    

figure;
plot(Ea,'LineWidth',2);
title('Grafica del error');
xlabel('Numero de terminos de la serie');
ylabel('Porcentaje del error');
grid on;
hold on;
plot(Et,'r','LineWidth',2);
 
sin_x
Vv