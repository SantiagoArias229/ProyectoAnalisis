%Newton: se ingresa el valor inicial (x0), la tolerancia del error (Tol) y el màximo nùmero de iteraciones (niter) 

function [result, n,xn,fm,dfm,E] = newton(x0,Tol,niter)
    syms x


        result= "Error sigue intentando"
        f=str2sym(func);
        df=diff(f);
        c=0;
        fm(c+1) = eval(subs(f,x0));
        fe=fm(c+1);
        dfm(c+1) = eval(subs(df,x0));
        dfe=dfm(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        xn=x0;
        N(c+1)=c;
        XN(c+1)=xn;
        
        Iteration = [];
        X0 = [];
        xn=[]
        func = [];
        Error = [];



     

        while error>Tol && fe~=0 && c<niter
            Iteration = [Iteration,c]; 
            xn1 = [xn1,xn];
            X0 = [X0, x0]
            func = [func, fe]; 
            Error = [Error, error];
            
            xn = x0-fe/dfe;
            XN(c+2)=xn;
            fm(c+2)=eval(subs(f,xn));
            fe=fm(c+2);
            dfm(c+2)=eval(subs(df,xn));
            dfe=dfm(c+2);
            E(c+2)=abs(xn-x0);
            error=E(c+2);
            x0=xn;
            N(c+2)=c+1;
            c=c+1;
        end

        tabla = table(Iteration', xn1', X0', func', Error', 'VariableNames', {'Iteration', 'xn', 'x0', 'fxi', 'Error'});
        
        csv_file_path = "tables/tabla_newton.csv";

        writetable(tabla, csv_file_path)

        xplot=((xm-2):0.1:(xm+2));
        hold on
        yline(0);
        plot(xplot,eval(subs(f,xplot)));
        img = getframe(gcf);
        imwrite(img.cdata, './media/grafica_newton.png');
        hold off

        if fe==0
           s=x0;
           n=c;
           result=sprintf('%f es raiz de f(x) \n',x0)
           disp(['      n                Xn                   Fx                   DFx                Error'])
           D=[N' XN' dfm' fm' E'];
            disp(D)

        elseif error<Tol
           s=x0;
           n=c;
           result = sprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',x0,Tol)
           disp(['      n                Xn                   Fx                   DFx                Error'])
           D=[N' XN' dfm' fm' E'];
            disp(D)

        elseif dfe==0
           s=x0;
           n=c;
           result = sprintf('%f es una posible raiz múltiple de f(x) \n',x0)
           disp(['      n                Xn                   Fx                   DFx                Error'])
           D=[N' XN' dfm' fm' E'];
            disp(D)
        else 
           s=x0;
           n=c;
           result = sprintf('Fracasó en %f iteraciones \n',niter)
           disp(['      n                Xn                   Fx                   DFx                Error'])
           D=[N' XN' dfm' fm' E'];
            disp(D)
        end
        
end