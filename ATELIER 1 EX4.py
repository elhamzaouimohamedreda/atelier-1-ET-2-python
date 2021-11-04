def fib(n):
    if n<2:
        return n
    else:
        return fib(n-2)+fib(n-1)


'''
ON  a utiliser la fonction récursive fib(n) par exemple si on a 4 fib(2)+fib(3) qui va donner 2+1 qui est 3
'''
a=int(input("entrer n"))
print(fib(a))
