                            %Lagrange: Calcula los coeficienetes del polinomio de interpolación de
% grado n-1 para el conjunto de n datos (x,y), mediante el método de
% lagrange.
function [pol] = Lagrange(vectorx,vectory)
    disp=(vectorx);
    disp=(vectory);
    xv = str2num(vectorx);
    yv = str2num(vectory);
    n=length(xv);
    Tabla=zeros(n,n);
    for i=1:n
        Li=1;
        den=1;
        for j=1:n
            if j~=i
                paux=[1 -xv(j)];
                Li=conv(Li,paux);
                den=den*(xv(i)-xv(j));
            end
        end
        Tabla(i,:)=yv(i)*Li/den;
    end
    pol=sum(Tabla);

    syms x;
                
    polinomio_simbolico = poly2sym(pol, x);
    polinomio_string = string(polinomio_simbolico);

    tabla = table(polinomio_string, 'VariableNames', {'Polinomio'});
        
    csv_file_path = "tables/tabla_lagrange.csv";

    writetable(tabla, csv_file_path)

    % Crear un conjunto de puntos para graficar el polinomio
    x_vals = linspace(min(xv), max(xv), 1000);
    y_vals = polyval(pol, x_vals);

    % Graficar el polinomio resultante
    figure;
    plot(x_vals, y_vals, 'r', xv, yv, 'bo'); % Polinomio en rojo, puntos en azul
    title('Polinomio de Lagrange');
    xlabel('x');
    ylabel('y');
    legend('Polinomio de Lagrange', 'Puntos de entrada');
    grid on;
    img = getframe(gcf);
    imwrite(img.cdata, './media/grafica_lagrange.png');
end