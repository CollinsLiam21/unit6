#Liam Collins
#5/11/18
#palindromes.py

file = open('engmix.txt')

for item in file:
    if len(item)%2==0:
        new.append(item)
        item[:len(item)//2] == item[len(item)//2:]
