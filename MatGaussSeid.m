%MatJacobiSeid: Calcula la solución del sistema
%Ax=b con base en una condición inicial x0,mediante el método de Jacobi o
%de Gauss Seidel (Matricial), depende del método elegido, se elige 0 o 1 en met
%respectivamente

function [E,s] = MatGaussSeid(x0,A,b,Tol,niter)

    A = str2num(A);
    b = str2num(b);
    x0 = str2num(x0);

    met = 1;
    c=0;
    error=Tol+1;
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);

    Xt(:,c+1)=x0;
    n(1)=c;
    E(c+1)=error;

    while error>Tol && c<niter
        if met==0
            T=inv(D)*(L+U);
            C=inv(D)*b;
            x1=T*x0+C;
        end
        if met==1
            T=inv(D-L)*(U);
            C=inv(D-L)*b;
            x1=T*x0+C;
        end
        E(c+1)=norm((x1-x0)/x1,'inf');
        error=E(c+1);
        x0=x1
        c=c+1;

        n(c+1)=c;
        Xt(:,c+1)=x0;
    end

    %D=[n' Xt' E'];
    %table(D);

    if error < Tol
        s=x0;
        n=c;
        s
        fprintf('es una aproximación de la solución del sistmea con una tolerancia= %f',Tol)
    else 
        s=x0;
        n=c;
        fprintf('Fracasó en %f iteraciones',niter) 
    end
end