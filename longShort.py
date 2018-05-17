#Liam Collins
#5/17/18
#longShort.py

file = open('engmix.txt')

longList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shortList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for line in item:
    line = line.strip()
    if len(line) > len(longList[longList.index(line[0])]:
        longList[longList.index(line[0])] = line
    elif len(line) < len(shortList[shortList.index(line[0])]:
        shortList[shortList.index(line[0])] = line

print(longList.strip())
print(shortList.strip())
    
    


    
    
