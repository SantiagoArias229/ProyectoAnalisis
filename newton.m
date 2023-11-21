%Newton: 
%se ingresa el valor inicial (x0)
%la tolerancia del error (Tol) 
%el tipo de tolerancia (TypeTol) -> 0 decimales correctos - 1 cifras
%significativas
%el máximo número de iteraciones (niter)
%Devuelve una tabla con las iteraciones y una gráfica de la solución 

function T = newton(x0,Tol,TypeTol,niter,fun)
    
        f=evalin(symengine,fun);
        %hallamos la derivada de f
        df=diff(f);
        %contador en 0
        c=0;
        %agregamos al arreglo de funciones la f(x0) 
        fm(c+1) = eval(subs(f,x0));
        fe=fm(c+1);
        if fe == 0
            E(1)=0
            xn(1)=x0
            fm(1)=fe
         else
        %agregamos al arreglo de derivadas la f'(x0)
        dfm(c+1) = eval(subs(df,x0));
        dfe=dfm(c+1);
        %agregamos el primer error al arreglo de ERRORES
        E(c+1)=Tol+1;
        error=E(c+1);
        %agregamos la primera x -> x0
        xn(c+1)=x0;
        %iteramos hallando las xn de Newton mientras no se llegue a la
        %tolerancia y que ni la función ni su derivada sea 0
        while error>Tol && fe~=0 && dfe~=0 && c<niter
            xn(c+2)=x0-fe/dfe;
            fm(c+2)=eval(subs(f,xn(c+2)));
            fe=fm(c+2);
            dfm(c+2)=eval(subs(df,xn(c+2)));
            dfe=dfm(c+2);
            if TypeTol==0
                E(c+2)=abs(xn(c+2)-x0);
            else
                E(c+2)=abs((xn(c+2)-x0)/xn(c+2));
            end
            error=E(c+2);
            x0=xn(c+2);
            c=c+1;
        end
        if fe==0
           fprintf('%f es raiz de f(x) \n',x0)
           E(c+2) = 0

        elseif error<Tol
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',x0,Tol)

        elseif dfe==0
           fprintf('%f es una posible raiz múltiple de f(x) \nO simplemente un máximo o mínimo local',x0)
        else 
           fprintf('Fracasó en %f iteraciones \n',niter) 
        end
      end
        T = table((0:1:c)', xn', fm', E', VariableNames=["n","x_n","f_m","E"]);
        fig = figure('Visible', 'off');
        xplot=((x0-2):0.1:(x0+2));
        hold on
        yline(0);
        plot(xplot,eval(subs(f,xplot)));
        print(fig,'newton','-dpng')
        hold off
        close(fig);
        writetable(T,'newton.csv')
        