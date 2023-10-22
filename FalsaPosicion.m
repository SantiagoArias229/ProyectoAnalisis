%Bisección: se ingresa el valor inicial y final del intervalo (xi, xs), la tolerancia del error (Tol) y el màximo nùmero de iteraciones (niter) 

function [s,E,fm] = FalsaPosicion(xi,xs,Tol,niter)
    syms x
    
    f(x)=-7*log(x)+x-8;
    %f(x)=log(sin(x)^2 + 1)-(1/2);
    %f(x)=x^2-5*x+6*sin(x);
    %f(x)=exp(-x-2)-2*x-2;

    fi=eval(subs(f,xi));
    fs=eval(subs(f,xs));
    if fi==0
        s=xi;
        E=0;
        fprintf('%f es raiz de f(x)',xi)
    elseif fs==0
        s=xs;
        E=0;
        fprintf('%f es raiz de f(x)',xs)
    elseif fs*fi<0
        c=0;
        xm= xi - (fi * (xi - xs)) / (fi - fs);
        fm(c+1)=eval(subs(f,xm));
        fe=fm(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        
        Iteration = [];
        a = [];
        b = [];
        Xm = [];
        func = [];
        Error = [];


        while error>Tol && fe~=0 && c<niter
            Iteration = [Iteration,c];
            a = [a,xi];
            b = [b, xs]; 
            Xm = [Xm, xm]; 
            func = [func, fe]; 
            Error = [Error, error];
   


            if fi*fe<0
                xs=xm;
                fs=eval(subs(f,xs));
            else
                xi=xm;
                fi=eval(subs(f,xi));
            end
            xa=xm;
            xm=xi - (fi * (xi - xs)) / (fi - fs);
            fm(c+2)=eval(subs(f,xm));
            fe=fm(c+2);
            %E(c+2)=abs(xa-xm);
            error=abs(xa-xm);
            c=c+1;


        end

        tabla = table(Iteration', a', Xm', b', func', Error', 'VariableNames', {'Iteration', 'a', 'xm', 'b', 'f(xm)', 'Error'});
        %T = table(Iteration, a, b, Xm, func, Error);
        disp(tabla)

        if fe==0
           s=xm;
           fprintf('%f es raiz de f(x)',xm) 
        elseif error<Tol
           s=xm;
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f',xm,Tol)
        else 
           s=xm;
           fprintf('Fracasó en %f iteraciones',niter) 
        end
    else
       fprintf('El intervalo es inadecuado')         
    end 

    
end