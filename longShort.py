#Liam Collins
#5/17/18
#longShort.py

file = open('engmix.txt')

longList = ['']*26
shortList = ['']*26
alph = 'abcdefghijklmnopqrstuvwxyz'

for line in file:
    line = line.strip()
    if len(line) > len(longList[alph.index(line[0])]):
        longList[alph.index(line[0])] = line
    elif len(line) < len(shortList[alph.index(line[0])]):
        shortList[alph.index(line[0])] = line

print(longList.strip())
print(shortList.strip())


    
    


    
    
