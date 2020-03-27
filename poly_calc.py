from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import sys

f = None
f_prime = None

def main():
    x = Symbol('x')

    # polynomial to evaluate
    global f
    f = parse_expr('x**2-2') #you can also read from terminal using sys.agrv

    global f_prime
    f_prime = f.diff(x)  # symbolic derivative with respect to x
    
    f = lambdify(x, f)  # pass evaulation f to f
    f_prime = lambdify(x, f_prime)

    secant(1,2,10**-4,100) #method to use

def bisec(a, b, error, N):
    # Initialization
    a = float(a)
    b = float(b)
    error = float(error)  # error tolerance

    for i in range(0, N):
        print("iteration", i + 1)
        c = (a + b) / 2

        print("a=", a, " b=", b, "c=", c)

        print("f(a)=", f(a), " f(c)=", f(c))

        if(f(c) == 0):
            print("the solution is", c)
            break
        elif(f(a)*f(c)<0):
            print("sign negative")
            b = c
        else:
            print("sign positive")
            a = c
        
        print("error=",abs(b-a))
        print("the root is in between",a ,b)

        if(abs(b-a)<error):
            print("the solution is ~",c)
            break
        print()


def newton(x0, error, N):
    x0 = float(x0)
    error = float(error)

    for i in range (0, N):
        print("iteration", i+1)
        print("x0=", x0)

        x1 = (x0)-f(x0)/f_prime(x0)
        print("x1=", x1)

        e = abs(x1-x0)
        print("|x0-x1|=", e)
        print("f(x)=", f(x0))
        print("f'(x)=",f_prime(x0))
        x0 = x1
        
        if(e<=error):
            print("the solution is ~", x0)
            break
        print()


def secant(x0, x1, error, N):
    x0 = float(x0)
    error = float(error)

    for i in range (0, N):
        print("iteration", i+1)
        print("x0=", x0)
        print("x1=", x1)
        
        x2 = x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
        print("f(x0)=", f(x0))
        print("f(x1)=", f(x1))
        print("x2=", x2)
        
        e = abs(x2-x1)
        print("error=", e)
        print()
        x0 = x1
        x1 = x2
        
        if(e<=error):
            print(" the solution is ~", x1)
            break

main()