#Liam Collins
#5/10/18
#reverseFile.py

file = open(input('Enter file name: '))

new = []
for line in file:
    words = line.split()
    if len(line)>0:
        new.append(words)

print(new)

