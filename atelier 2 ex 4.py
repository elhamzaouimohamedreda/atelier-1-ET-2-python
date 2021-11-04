def intersection (set1,set2):
    result=[]
    for i in set1:
        if i in set2:
            result.append(i)
    return result
'''
Dans ce programme on fait l’intersection avec une fonction (intersection) qui a comme argument set1et set2 qui a deux boucle for pour itérer les sets créer une liste deux nombres intersecté apres fait remove de nombre intersecte est print set1
'''
set1={1,2,3,4,5}
set2={1,3,5}
print("l'intesection donne ")
print(intersection(set1,set2))
for i in set1&set2:
    set1.remove(i)
print(set1)