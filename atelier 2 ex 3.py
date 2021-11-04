def nbroccurence(l,a):
    i=0
    for x in l:
        if(x==a):
            i=i+1
    return i
'''
Ici on a créer un dictionnaire ou la clé est le nombre et la valeur est la fonction nbroccurence qui reçoit comme argument la liste et le nombre a rechercher dans la fonction on a fais une simple boucle for pour iterer la liste qui a compteur i
'''
l=[1,1,2,3,3,3]
dic={1:nbroccurence(l,1),2:nbroccurence(l,2),3:nbroccurence(l,3)}
print(dic)