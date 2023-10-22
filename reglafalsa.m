function T = reglafalsa(xi,xs,Tol,niter)
    syms x

    f(x)=(-7*log(x))+x-10;
    fi=eval(subs(f,xi));
    fs=eval(subs(f,xs));
    if fi==0
        E=0;
        fprintf('%f es raiz de f(x)',xi)
    elseif fs==0
        E=0;
        fprintf('%f es raiz de f(x)',xs)
    elseif fs*fi<0
        c=0;
        xm=xi-fi*((xs-xi)/(fs-fi));
        fm(c+1)=eval(subs(f,xm));
        fe=fm(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        %N(c+1)=c; si la primera iteracion se toma como 0
        N(c+1)=c+1;
        XM(c+1)=xm;
        while error>Tol && fe~=0 && c<niter
            if fi*fe<0
                xs=xm;
                fs=eval(subs(f,xs));
            else
                xi=xm;
                fi=eval(subs(f,xi));
            end
            xa=xm;
            xm=xi-fi*((xs-xi)/(fs-fi));
            XM(c+2)=xm;
            fm(c+2)=eval(subs(f,xm));
            fe=fm(c+2);
            E(c+2)=abs(xm-xa);
            error=E(c+2);
            %N(c+2)=c+1; si la primera iteracion se toma como 0
            N(c+2)=c+2;
            c=c+1;
        end
        if fe==0
           fprintf('%f es raiz de f(x) \n',xm)
        elseif error<Tol
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',xm,Tol)
        else 
           fprintf('Fracasó en %f iteraciones \n',niter)
        end
    else
       fprintf('El intervalo es inadecuado')         
    end    

    T = table(N', XM', fm', E', VariableNames=["n","Xn","Fm","Error"]);
        xplot=((xm-2):0.1:(xm+2));
        hold on
        yline(0);
        plot(xplot,eval(subs(f,xplot)));
        hold off
end