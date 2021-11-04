def somme(n):
   if n ==0:
    return 0
   else:
    return n+somme(n-1)
 '''
 ICI on a utiliser la fonction récursive somme d’argument n pou calculer la somme par exemple somme(3) donne 3+somme(2) et comme ca il va calculer la somme
 '''
n=int(input("entrer n"))
print(somme(n))
