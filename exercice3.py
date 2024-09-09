def countword(sentence):
    return sentence.count("False")

example ="False, False, True, True, True"
print (countword(example))


def getDifference(*args):
    minimum = min(*args)
    maximum = max(*args)
    return maximum - minimum

print(getDifference(2, 10, 5, 98))


def ifbrokenbridge(sentence):
    return not ' ' in sentence

string = " ### ###########"
print(ifbrokenbridge(string))


def getMinMax(list):
    return [min(list),max(list)]

test = [8, 1, 9, 2, 6]
print(getMinMax(test))


def convert(number):
    return  "-" * number

test2 = 5
print(convert(test2))


def withs(name):
    return name.endswith("s")

print(withs("Thomas"))


def divide(a, b):
    return a/b

print(divide(1,6))


def rest(a,b):
    return a%b

print(rest(1,3))


def firstLast(list):
    return [list[0], list[-1]]

test = [5,2,8,17,6,14]
test2 = ["A", 2, True, None]
print(firstLast(test2))

