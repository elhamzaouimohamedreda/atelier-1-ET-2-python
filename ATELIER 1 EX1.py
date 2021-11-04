def fun(a):
    if a==1:
        return 1
    else:
        return a*fun(a-1)
'''
Dans ce code on a fait deux fonctions la fonction fun(a) pour calculer le factoriel et la fonction somme (b) pour fair la somme de n’import quel serie de la forme x=i+i !
'''
def somme(b):
    s=b+(fun(b+1))
    return s
num = int(input("enter the number?"))
print("la somme est",somme(num))