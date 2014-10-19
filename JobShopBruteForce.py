import itertools

pierwsze, drugie, trzecie, czwarte, piate, szoste = (20, 21), (9, 103), (99, 37), (82, 104), (93, 31), (111, 80) 

lista = pierwsze, drugie, trzecie, czwarte, piate, szoste, (117, 115), (85, 122), (8, 68)





permutacje = itertools.permutations(lista)

#for p in permutacje:
#    print p



def oblicz_czasy(lista):
    czas1 = 0
    czas2 = 0 
    for element in lista:
        T1, T2 = element
        czas1+=T1
        czas2 = max(czas1, czas2) + T2
       # print str(czas1) + "  " + str(czas2)
    return czas2

oblicz_czasy(lista)

def wartosc_czasy(czasy):
    T2, czasy   = czasy
    czasy
    return T2


czasy_wykonania =  [ (oblicz_czasy(p), p) for p in permutacje]




mina = min(czasy_wykonania, key=wartosc_czasy)

for p in czasy_wykonania:
    if p == mina:
        print p

print mina


#print czasy_wykonania
    