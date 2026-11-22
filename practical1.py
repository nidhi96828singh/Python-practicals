import cmath

a=float(input("Enter a:" ))
b=float(input("Enter b:" ))
c=float(input("Enter c:" ))

if a==0:
    print("not a quadratic equation")
else:
    d=b**2-4*a*c
    r1=(-b+cmath.sqrt(d))/(2*a)
    r2=(-b-cmath.sqrt(d))/(2*a)

    if d>0:
        print("real and distinct roots:",r1.real,r2.real)
    elif d==0:
        print("real and equal roots:",r1.real)
    else:
        print("complex roots:",r1,r2)
