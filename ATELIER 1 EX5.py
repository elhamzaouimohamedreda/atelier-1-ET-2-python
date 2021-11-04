def somme(n):
    if n//10==0:
        return n
    else:
        return n%10+somme(n//10)
'''
On utiliser ici la récursivité par exemple si on a 44 on va faire la division reelle on 10 on aller a else qui faire le modulo de 44%10qui va donner 4 +somme de (44//10) QUI va donner a la fin 4+4=8
'''
a=int(input("donner un nombre"))
print(somme(a))