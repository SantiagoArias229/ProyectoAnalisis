%Newtonint: Calcula los coeficienetes del polinomio de interpolación de
% grado n-1 para el conjunto de n datos (x,y), mediante el método de Newton
% con diferencias divididas.
function [Tabla] = Newtonint(x,y)

format short

    x = cell2mat(x);
    y = cell2mat(y);

    %number of points
    n=length(x);

    Tabla=zeros(n,n+1);
    Tabla(:,1)=x;
    Tabla(:,2)=y;
    for j=3:n+1
        for i=j-1:n
            Tabla(i,j)=(Tabla(i,j-1)-Tabla(i-1,j-1))/(Tabla(i,1)-Tabla(i-j+2,1)); %n-esima diferencia divida 
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
        pol=pol+coef(i+1)*acum; %subtermino de polinomio de newton: pn(x) = b0 + b1(x-x0)+...+bn(x-x0)(x-x1)...(x-xn-1) 
    end

        % Generar valores de x
        xpol=min(x):0.001:max(x);
        
        p =zeros(size(x));
        p = p';
        
        
        % Calcular el polinomio para cada grado
        for i = 1:length(pol)
            p = p+pol(i) * xpol.^(length(pol)-i);
        
        end



    figure
    hold on
    plot(x,y,'r*',xpol,p,'b')

    img = getframe(gcf);
    imwrite(img.cdata, './media/grafica_newtonInter.png');
    hold off

    csv_file_path = "tables\tabla_newtonInt.csv";

    writematrix(Tabla, csv_file_path)

    writematrix(pol,'pol_newtonInter.csv')
end