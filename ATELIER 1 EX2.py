def bin(nbr):
    b=0
    c=0
    while nbr!=0:
        reste=nbr%2
        p=10**c
        b=b+reste*p
        c=c+1
        nbr=nbr//2
    print(b)
    '''
    An ici fait la fonction bin(n) pour faire la   conversion (b est la variable ou on stock les nombre binaire c est l’ordre et apres ce calcule on trouve le nombre binaire)
    '''
nbr=int(input("entrer le nombre decimal"))
bin(nbr)