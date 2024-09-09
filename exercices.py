# Exercie 1

def add(numb1, numb2):
    result = numb1 + numb2
    return result

print(add(60,100))

# Exercie 2

def less(numb1, numb2):
    result = numb1 - numb2
    return result

print (less(39,10))


# Exercie 3

def minutesToSecond(minutes):
    conversion = minutes *60
    return conversion

print(minutesToSecond(5))


# Exercie 4
def hoursToSecond(hours):
    conversion2 = hours*3600
    return conversion2

print(hoursToSecond(2))

# Exercie 5
def perimeter(long, larg):
    total = (long + larg) * 2
    return total

print(perimeter(10,6))

# Exercice 6
def nbrsPattes(poulets, vaches, chevaux):
    total = (poulets *2) + (vaches*4)+(chevaux*4)
    return total

print(nbrsPattes(1, 4,2))

# Exercice 7

def maxNumber(list):
    return max(list)

number = [41477, 145, 6587, 12547, 54, 56547, 4447895, 41, 54, 52]
result = maxNumber(number)
print(f'Le plus grand nombre parmi ces derniers {number} est {result} ')



# Exercice 8

def sumListNumber(list):
    return sum(list)

number = [0,0,0,1]
result = sumListNumber(number)
print(f'La somme de cette liste est {result} ')

def minNumber(list):
    return min(list)

number = [41477, 145, 6587, -12547, 54, 56547, 4447895, 41, 54, 52]
result = minNumber(number)
print(f'Le plus grand nombre parmi ces derniers {number} est {result} ')
