# Exercice 1
import math


def multipleOfFive(numb):
   return numb % 5 == 0

print(multipleOfFive(50))


# Exercice 2
def lastElement(list):
    return list[-1]

test = [1, 2, 3, 4, 5, 39]
print(lastElement(test))


# Exercice 3
def carre(numb):
    result = numb**2
    return result
print (carre(4))


# Exercice 4
def assess(expression):
    result = eval(expression)
    return result
print(assess("4*2/2"))


# Exercice 5
def spacecontain(sentence):
    return ' ' in sentence
example = "really"
print(spacecontain(example))


# Exercice 6

def singularOrPlural(characterString):
    try:
       if characterString[-1] =='s':
            return True
       else:
            return False

    except IndexError:
        return "La chaîne de caractères renseignée n'est pas valide"

example = "retours"
example2 = "voute"
example3 = "images"

print(singularOrPlural(example3))


# Exercice 7
def evenorodd(number):
    try:
        if number % 2 == 0:
            return "Le nombre est pair."

        else:
            return'Le nombre est impair'

    except TypeError:
        return "La numéro renseigné n'est pas valide"

n = 10001
print(evenorodd(n))


# Exercice 8
def emptystring(characterstring):
    try:
        if len(characterstring)==0:
            return True
        else:
            return False
    except TypeError:
        return "Chaîne de caractère non valide"

ex = ""
print(emptystring(ex))



