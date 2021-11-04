from collections import Counter
text = 'je mappelle elhamzaoui mohamed reda'
frequence = Counter(text)
print("Nombre d'occurrences de tous les caractères :")
for (key, value) in frequence.items():
    print("Nombre d'occurrences de ", key, " est : ", value)
L = sorted(freq(texte).items(), key=lambda colonne: colonne[1], reverse=True)
'''
On a cree premierement un texte pour compter on utiliser counter pour compter les frequences est on a utiliser le dictionnare pour stocker le texte nombre d’occurrence dans key et la valeur dans la place de value
'''
for i in L:
    print('{} : {}'.format(i[0], i[1]))