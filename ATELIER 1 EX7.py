def str(string):
    if len(string)==0:
        return string
    else :
        return str(string[1:])+string[0]
'''
ICI ON a fait une fonction récursive pour faire l’inverse des mot
'''
string="reda"
print(string)
print(str(string))