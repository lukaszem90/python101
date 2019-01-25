#! /usr/bin/env python3
# -*- codning: utf-8 -*-

#Dane
AktRok=int(input('Hej, jaki mam teraz roook!?'))
#AktualnyRok=2019
PythonRok=1989

#Obliczenia wieku Pythona
wiekPythona = AktRok - PythonRok

#Pobieramy dane
imie = input('Hej, jak się nazywasz?')
wiek = int(input('Ile masz lat?'))

#Komunikaty
print("Witaj",imie)
print("Jestem Python, mam", wiekPythona, "lat!")

#Roznica wieku
rw = (int(wiek)) - (int(wiekPythona))

#Komunikaty warunkowe
if int(wiek) > int(wiekPythona):
    print("Jestes starszy ode mnie aż o tyle lat:", rw,"!")
else:
    print("O TY dzieciaku! ;)")