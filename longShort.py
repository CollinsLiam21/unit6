#Liam Collins
#5/17/18
#longShort.py

file = open('engmix.txt')

longList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shortList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alph = 'abcdefghijklmnopqrstuvwxyz'

for line in file:
    line = line.strip()
    if len(line) > len(longList[alph.index(line[0])]):
        longList[alph.index(line[0])] = line
    elif len(line) < len(shortList[alph.index(line[0])]):
        shortList[alph.index(line[0])] = line

print(longList.strip())
print(shortList.strip())
    
    


    
    
