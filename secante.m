
function [n,xn,fm, E] = secante(func,x0,x1,Tol,niter)
    syms x

        f= str2sym(func);
        %f =((exp(-x))*(-1+x))+(x^(2/3))-92;
        %f = log(sin(x)^2 + 1)-(1/2);
        %f=sin(2*x)-(x/(3))^3+0.1;

        fi = eval(subs(f, x0));
        fs = eval(subs(f, x1));
        
        c=0;
        fm(c+1) = eval(subs(f,x0));
        fe=fm(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        xn= x1 - ((fs * (x1 - x0)) / (fs - fi));
        fn= eval(subs(f, xn));

       if fi==0
        s=xi;
        E=0;
        fprintf('%f es raiz de f(x)',x0)
        return
       elseif fs==0
        s=xs;
        E=0;
        fprintf('%f es raiz de f(x)',x1)
        return
       elseif fn ==0
        s=xn;
        E=0;
        fprintf('%f es raiz de f(x)',xn)

       end 

       Iteration = [];
       Xn  = [];
       Fxn = [];
       Error = []; 


        while error>Tol && fn ~= 0 && c<niter
   
            Iteration = [Iteration,c]; %#ok<AGROW>
            Xn  = [Xn, xn]; %#ok<AGROW>
            %Fxn = [Fxn, fi];  %#ok<AGROW>
            Error = [Error, error]; %#ok<AGROW>
        


            x0 = x1;
            x1 = xn;
            fi = eval(subs(f, x0));
            fs = eval(subs(f, x1));
            xn = x1 - ((fs * (x1 - x0)) / (fs - fi));
            fn = eval(subs(f, xn));
            
            fm(c+2)=eval(subs(f,xn));
            fe=fm(c+2);
            E(c+2)=abs(xn-x1);
            error=E(c+2);
            c=c+1;

            Fxn = [Fxn, fs];  %#ok<AGROW>

            if (fs - fi) == 0
               s=x0;
               n=c;
               printf('Cannot continue with the method given that the denominator is zero.  %f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',xn,Tol)
            end 

        end


        tabla = table(Iteration', Xn', Fxn', Error', 'VariableNames', {'Iteration', 'xn', 'f(xn)', 'E'});
        disp(tabla)
        matriz = table2array(tabla);
        csvwrite('tabsecante.csv', matriz);

        xplot=((xn-2):0.1:(xn+2));
        hold on
        yline(0);
        plot(xplot,eval(subs(f,xplot)));
        img = getframe(gcf);
        imwrite(img.cdata, 'grafsecante.png');
        hold off

      

      
        

        if fn==0
           s=x0;
           n=c;
           fprintf('%f es raiz de f(x) \n',xn)

        elseif error<Tol
           s=x0;
           n=c;
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %.10f \n',xn,Tol)

        % elseif fn==0
        %    s=x0;
        %    n=c;
        %    fprintf('%f es una posible raiz múltiple de f(x) \n',x0)
        else 
           s=x0;
           n=c;
           fprintf('Fracasó en %f iteraciones \n',niter) 
        
        end
        
end