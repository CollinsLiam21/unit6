#Liam Collins
#5/10/18
#reverseFile.py

file = open(input('Enter file name: '))

new = []
for line in file:
    line = line.split()
    if len(line)>0:
        new.append(line)

new.reverse()
for word in new:
    print(word)

