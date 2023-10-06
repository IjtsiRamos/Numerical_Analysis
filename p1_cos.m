clear all;
close all;
clc;

%sen(x)=1-x^pares/factorial(pares)+ 
% Numero de terminos de la serie
n=16;
% Valor al cual se quiere aproximar la funcion de seno
x=0.78539816339;
% Valor verdadero
Vv=round(cos(x),4);
%Vv=0.0137073546;
% 1a Aproximacion
cos_x=(x^0)/factorial(0);
% Aproximacion del valor del termino de la serie
Va=round(cos_x,4);
Aact=cos_x;
Aant=0;
% Error verdadero (Et)-> t = true
Et=abs(((Vv-Va)/Vv)*100);
% Error aproximado (Ea)->  = approximate
Ea=abs(((Aact-Aant)/Aact)*100);
Es=(0.5)*10^(2-n);
m=2;
while Va~=Vv
    Aant=Va;
    cos_x=cos_x-(x^m)/(factorial(m));
    Va=round(cos_x,4);
    Aact=cos_x;
    Et_new=abs((Vv-Va)/Vv)*100;
    Et=[Et,Et_new];
    Ea_new=abs((Aact-Aant)/Aact)*100;
    Ea=[Ea,Ea_new];
    m=m+2;
    Aant=Va;
    Aant=Va;
    cos_x=cos_x+(x^m)/(factorial(m));
    Va=round(cos_x,4);
    Aact=cos_x;
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
 
cos_x
Vv