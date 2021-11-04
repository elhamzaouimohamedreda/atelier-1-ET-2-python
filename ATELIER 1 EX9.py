def recherche_dichotomique(li, c):
    a, b = 0, len(li) - 1
    while a <= b:
        m = (a + b) // 2
        if c == li[m]:
            return m
        elif c < li[m]:
            b = m - 1
        else:
            a = m + 1
    return -1
'''
ON A utiliser la fameuse technique dichotomique avec deux argument la matrice avec le nombre qu’on veut l’avoir .on a fait une boucle while avec trois if pour iterer la matrice puis trouver le nombre a rechercher
'''
print(recherche_dichotomique([0, 2, 5, 7, 8], 7))