% Numero de terminos de la serie
n = 16;
% Valor al cual se quiere aproximar la funcion exponencial
x = 1.0;
% Valor verdadero
Vv = exp(x);
% 1a Aproximacion
exp_x = 1;
% Aproximacion del valor del termino de la serie
Va = exp_x;
Aact = exp_x;
Aant = 0;
% Error verdadero (Et)-> t = true
Et = abs(((Vv - Va) / Vv) * 100);
% Error aproximado (Ea)-> a = approximate
Ea = abs(((Aact - Aant) / Aact) * 100);
Es = (0.5) * (10^(2 - n));
m = 1;
Ea_array = Ea;
Et_array = Et;

while Ea > Es
    Aant = Va;
    exp_x = exp_x + (x^m) / factorial(m);
    Va = exp_x;
    Aact = exp_x;
    Et = abs((Vv - Va) / Vv) * 100;
    Et_array = [Et_array, Et];
    Ea = abs((Aact - Aant) / Aact) * 100;
    Ea_array = [Ea_array, Ea];
    m = m + 1;
end

plot(Ea_array);
hold on;
plot(Et_array);
ylabel('Porcentaje del error');
xlabel('Numero de terminos de la serie');
title('Grafica del error');
grid on;

disp(exp_x);
disp(Vv);
