def extract(L1,L2):
    L3=[]
    for x in L1:
        if(x%2!=0):
            L3.append(x)
    for y in L2:
        if(y%2==0):
            L3.append(y)
    return L3
'''
Ici on a crée deux liste et on va les donner a la fonction extract pour extraire les nombre impaire du premier et les nombre paire du deuxième list  et les mettre dans une troisieme list l3
'''

L1=[1,3,2,5]
L2=[2,4,9,6]
print("la fonction va donne",extract(L1,L2))

