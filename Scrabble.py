"""
CREATED BY UMAR SOHAIL
ENJOY :)
"""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}


user_input = str(input("please enter your sentense: "))

split = user_input.split(" ")
print(split)

g = []
def scrabble_score(word):   
    for i in word:
        total = 0
        i.lower()
        for k in i:
            total += score[k]
        g.append(total)
    return g

def calculator(a):
    locator = a.index(max(a))
    largest = split[locator]
    return largest

def answer(word, score, larg):
    c = " this is the largest number %s " % larg
    for i in range(0,len(word)):
        a = '%s = %s' % (word[i],score[i])
        b = print(a)
    print()
    return c
        
print(answer(split, scrabble_score(split), calculator(g)))
