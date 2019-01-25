#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math
op = "t"
while op != "n":
    dane = input("Podaj trzy boki trójkąta (rozdziel to przecinkami):")

    lista = []
    for x in dane.split(","):
        lista.append(int(x))
    a,b,c = lista

    print("Podano boki: ",a,b,c)

    if a+b>c and a+c>b and b+c>a:
        print("Z podanych boków mozna zbudować trójkat.")
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Do tego prostokątny!")
        
        print("Obwód wynosi:",(a+b+c))
        p=0.5*(a+b+c)
        P=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Pole wynosi:",P)
        op = "n"
    else:
        print("Z podanych odcinkow nie mozna utworzyc trojkata prostokatnego")
        op=input("t/n")
print ("Do zoba!")