def triabulle(tab):
    n=len(tab)
    for i in range(n):
        for j in range(0,n-i-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]

def triparselection(tab):
    for i in range(i+1,len(tab)):
        if tab[min>tab[j]]:
            min=j
        tmp=tab[i]
        tab[i]=tab[min]
        tab[min]=tmp
        return tab
def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k


'''
ICI on a utiliser trois fonction de tri (tri par insertion,tri a bulle,tri par sélection) on a crée deux tableau et on a choisi le tri a bulle et le tri par insertion 
'''
tab=[2,4,1]
triabulle(tab)
print("le tableau trie est")
for i in range(len(tab)):
   print(tab[i])
tab = [1, 32, 2, 74 , 9]
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
   print ("% d" % tab[i])