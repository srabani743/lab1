from math import *

# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne

i1 = 2
i2 = 4
f1 = 1.4
f2 = 2.9
s1 = "python"
s2 = "pycharm"
c1 = 2 + 3j
c2 = 8 - 4j

print("Zad1")
print(i1)
print(i2)
print(f1)
print(f2)
print(s1)
print(s2)
print(c1)
print(c2)

# Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne

print("Zad2")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Dzielenie")
print("4.Mnożenie")

dzialanie = input("Wybierz dzialanie(podaj cyfre): ")

l1 = float(input("Wybierz 1 liczbe: "))
l2 = float(input("Wybierz 2 liczbe: "))

if dzialanie == "1":
    print(l1, "+", l2, "=", l1+l2)
elif dzialanie == "2":
    print(l1, "-", l2, "=", l1-l2)
elif dzialanie == "3":
    print(l1, "/", l2, "=", l1 / l2)
elif dzialanie == "4":
    print(l1, "*", l2, "=", l1 * l2)

# Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

print("Zad3")
a = 3
print("a = ", a)
a += 2
print("a += 2", a)
a -= 3
print("a -= 3", a)
a *= 3
print("a *= 3", a)
a /= 2
print("a /= 2", a)
a **= 2
print("a **= 2", a)
a %= 2
print("a %= 2", a)

# Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:

print("Zad4")
print(exp(10))
print(pow((log((5 + pow(sin(8), 2)))), 1 / 6))
print(floor(3.55))
print(ceil(4.80))

# Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a poszostałe małe.
# (trzeba użyć metody capitalize)

print("Zad5")
imie = "JAKUB"
nazwisko = "PIETKIEWICZ"

print(str.capitalize(imie) + " " + str.capitalize(nazwisko))

# Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami
# np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)

piosenka = """Black bird, black moon
Black sky, black light
Black, everything black
Black heart
Black Keys, black diamonds
Black out, everything black
Black, black, everything, everything
All black, everything, everything
All black, everything, everything
All black, everything, everything, black"""

print("Zad6")
print("Liczba slow w piosence:", piosenka.count("black") + piosenka.count("Black"))

# Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy

indeks = "Awokado"

print("Zad7")
print(indeks)
print("Druga litera:", indeks[1])
print("Ostatnia litera:", indeks[len(indeks) - 1])

# Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy.
# (trzeba użyć metody split)

print("Zad8")
print(piosenka.split())

# Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.

nitka = "nitka"
splawik = 3.14
heksa = hex(20)

print("Zad9")
print("String: %s" % nitka)
print("Float: %d" % splawik)
print("Hex: %s" % heksa)
