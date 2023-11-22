function [radio, E, s] = SOR(x0,A,b,Tol,niter,w, error)
    
    A = str2num(A);
    b = str2num(b);
    x0 = str2num(x0);
    c=0;
    error=Tol+1;
    D=diag(diag(A));
    L=-tril(A,-1);
    U=-triu(A,+1);

    n(1)=c;
    E(c+1)=error;
    Xt(:,c+1)=x0;
    while error>Tol && c<niter
        T=inv(D-w*L)*((1-w)*D+w*U);
        C=w*inv(D-w*L)*b;
        x1=T*x0+C;
        if error ==1
            E(c+1)=norm((x1-x0)./x1,'inf');
        else
            E(c+1)=norm((x1-x0),'inf');
        end
        error=E(c+1);
        n(c+1)=c;
        x0=x1;
        Xt(:,c+1)=x0;
        c=c+1;
       
    end 

    % Calcula el radio espectral
    radio = max(abs(eig(T)));
      
    if error < Tol
        s=x0;
        t=c;
        s
        fprintf('es una aproximación de la solución del sistmea con una tolerancia= %f',Tol)
    else 
        s=x0;
        t=c;
        fprintf('Fracasó en %f iteraciones',niter) 
    end   

    D=[n' Xt' E'];
    tabla = table(n', Xt', E', 'VariableNames', {'Iteracion', 'x' 'Error'});

    % tabla = table(s, 'VariableNames', {'solucion'});
        
    csv_file_path = "tables/tabla_sor.csv";

    writetable(tabla, csv_file_path)
end