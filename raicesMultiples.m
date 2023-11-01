%Newton: se ingresa el valor inicial (x0), la tolerancia del error (Tol) y el màximo nùmero de iteraciones (niter) 

function [respuesta,n,s, rn, fm,dfm,df2m,E] = raicesMultiples(x0,Tol,niter, func)
    syms x

    respuesta = "Error: No se encontró una raíz en la función"

        f=evalin(symengine,func);
        df=diff(f);
        df2=diff(df);
        c=0;
        fm(c+1) = eval(subs(f,x0));
        fe=fm(c+1);
        dfm(c+1) = eval(subs(df,x0));
        df2m(c+1) = eval(subs(df2,x0));
        dfe=dfm(c+1);
        dfe2=df2m(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        xn=x0;
        n(c+1)=c;
        s(c+1)=x0;
        rn(c+1)=x0;
        while error>Tol && c < niter && fe~=0
            xn=x0-((fe*dfe)/(dfe^2-(fe*dfe2)));
            fm(c+2)=eval(subs(f,xn));
            fe=fm(c+2);
            dfm(c+2)=eval(subs(df,xn));
            dfe=dfm(c+2);
            df2m(c+2)=eval(subs(df2,xn));
            dfe2=df2m(c+2);
            E(c+2)=abs(xn-x0);
            error=E(c+2);
            s(c+2)=x0;
            rn(c+2)=xn;
            x0=xn;            
            n(c+2)=c;
            c=c+1;
        end
        
        tabla = table(n', s', fm', E', 'VariableNames', {'Iteration', 'xi', 'fxi', 'Error'});
        
        csv_file_path = "tables/tabla_raicesMultiples.csv";

        writetable(tabla, csv_file_path)

        xplot=((xn-2):0.1:(xn+2));
        hold on
        yline(0);
        plot(xplot,eval(subs(f,xplot)));
        img = getframe(gcf);
        imwrite(img.cdata, './media/grafica_rm.png');
        hold off

        if fe==0
           respuesta = sprintf('%f es raiz de f(x) \n',x0)
           disp(['      i        Xn       Xn+1     F(Xn)     dF(Xn)      ddf(Xn)    Error'])
           D=[n' s' rn' fm' dfm' df2m' E'];
           disp(D)  
        elseif error<Tol
          respuesta = sprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',x0,Tol)
           disp(['      i        Xn       Xn+1     F(Xn)     dF(Xn)      ddf(Xn)    Error'])
           D=[n' s' rn' fm' dfm' df2m' E'];
           disp(D) 
        elseif dfe==0
           respuesta = sprintf('%f es una posible raiz múltiple de f(x) \n',x0)
           disp(['      i        Xn       Xn+1     F(Xn)     dF(Xn)      ddf(Xn)    Error'])
           D=[n' s' rn' fm' dfm' df2m' E'];
           disp(D) 
        else 
           respuesta = sprintf('Fracasó en %f iteraciones \n',niter) 
           disp(['      i        Xn       Xn+1     F(Xn)     dF(Xn)      ddf(Xn)    Error'])
            D=[n' s' rn' fm' dfm' df2m' E'];
           disp(D) 
        end
        
end