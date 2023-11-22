%Newtonint: Calcula los coeficienetes del polinomio de interpolación de
% grado n-1 para el conjunto de n datos (x,y), mediante el método de Newton
% con diferencias divididas.
function [Tabla] = test(x,y)

format short

    %number of points
    n=length(x);

    Tabla=zeros(n,n+1);
    Tabla(:,1)=x;
    Tabla(:,2)=y;
    for j=3:n+1
        for i=j-1:n
            Tabla(i,j)=(Tabla(i,j-1)-Tabla(i-1,j-1))/(Tabla(i,1)-Tabla(i-j+2,1));
        end
    end

    %la convertimos en los coeficientes
    coef= diag(Tabla,+1);

    pol=1;
    acum=pol;
    pol=coef(1)*acum;
    for i=1:n-1
        pol=[0 pol];
        acum=conv(acum,[1 -x(i)]);
        pol=pol+coef(i+1)*acum;
    end

% Generar valores de x
xpol=x(1):0.001:x(end);

p =zeros(size(x));
p = p';


% Calcular el polinomio para cada grado
for i = 1:length(pol)
    p = p+pol(i) * xpol.^(length(pol)-i);

end



    figure
    plot(x,y,'r*',xpol,p,'b')

    csv_file_path = "tables\tabla_newtonInt.csv";

    writematrix(Tabla, csv_file_path)

    writematrix(pol,'pol_newtonInter.csv')
end