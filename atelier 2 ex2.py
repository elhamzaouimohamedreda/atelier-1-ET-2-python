list = ['1','2','3','4','5','6','7','8','9']

n=3
'''
On a utiliser ici la boucle for de i in range(0,len(list),n)avec la format de liste qu’on veut avoir list[i :i+n]AVEC n LE NOMBRE de position dans la liste qu’on veut avoir
'''
trilist=[list[i:i + n] for i in range(0, len(list), n)]
print(trilist)