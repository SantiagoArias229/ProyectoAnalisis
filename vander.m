function [respuesta] = vander(xin, yin)
    x = xin;
    y = yin;
    V = vander(x);

    Polinomio = V\y;
    Polinomio = Polinomio';
    T = array2table(Polinomio);

    x_plot = 1:0.01:5;
    y_plot = polyval(Polinomio, x_plot);
    plot(x,y,'r*',x_plot, y_plot,'b-')
    xlabel('x');
    ylabel('y');
    img = getframe(gcf);
    imwrite(img.cdata, './media/grafica_vander.png');
    respuesta=sprintf('Estos son los polinomios generados:');
    writetable(T, 'tables/tabla_vander.csv');
end