"""Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
aceste cifre luate o singură dată. Exemplu : date de intrare : 3 4 2 Date de ieşire : 324
342 243 234 432.
"""

a = input("dati a= ")
b = input("dati b= ")
c = input("dati c= ")
print(a+b+c ,a+c+b ,c+b+a ,c+a+b ,b+a+c)
