
import random

def vytvor (j): 
    policko=[]

    pole=[]

    for n in range (j):

        for i in range (j): 
            
            policko.append(random.randrange (10))

        pole.append(policko) 
        policko = []

    return (pole)

t=vytvor (3)

j=vytvor (3)

def sucet_matic (matl, mat2):

    polisko = []

    for x in range (len (matl)):

        policenko=[]

        for i in range (len (matl)): 
            vysledok=t [x] [i]+j [x] [i]

            policenko.append (vysledok) 
        polisko.append(policenko)

    return (polisko)

def vypis (d):

    for i in range (len (d)):

        print (d[i])





def zle_nasobenie (mat1, mat2):

    polisko = [] 
    for x in range (len (mat1)):
        policenko=[]
        for i in range (len (mat1)): 
            vysledok=t[x] [i]*j[i] [x] 
            policenko.append(vysledok)

        polisko.append (policenko)

    return (polisko)

print ("matical:")

vypis (t)

print ("matica2:") 
print ("súčet:") 
vypis (sucet_matic (t, j))
vypis (j)
print ("ZLE")
vypis (zle_nasobenie (t, j))
