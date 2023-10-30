function [n,xn,fm,E] = puntoFijoFixed(x0,Tol,niter,func, funcg)
    f=evalin(symengine,func);
    g=evalin(symengine,funcg);
    c=0;
    fm(c+1) = eval(subs(f,x0));
    fe=fm(c+1);
    E(c+1)=Tol+1;
    error=E(c+1);
    xn(c+1)=x0;
    N(c+1)=c;
    while error>Tol && fe~=0 && c<niter
        xn(c+2)=eval(subs(g,x0));
        fm(c+2)=eval(subs(f,xn(c+2)));
        fe=fm(c+2);
        E(c+2)=abs((xn(c+2)-x0));
        error=E(c+2);
        x0=xn(c+2);
        N(c+2)=c+1;
        c=c+1;
    end
    if fe==0
       s=x0;
       n=c;
       fprintf('%f es raiz de f(x)',x0)
       disp(['      n                Xn                   Fx                   Error'])
       D=[N' xn' fm' E'];
    elseif error<Tol
       s=x0;
       n=c;
       fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f',x0,Tol)
       disp(['      n                Xn                   Fx                   Error'])
       D=[N' xn' fm' E'];
        disp(D)
    else 
       s=x0;
       n=c;
       fprintf('Fracasó en %f iteraciones',niter) 
    end
end