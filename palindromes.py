#Liam Collins
#5/11/18
#palindromes.py

file = open('engmix.txt')


for item in file:
    if len(item)%2==0:
        if item[:len(item)//2] == item[len(item)//2:]:
            print(item)
    if len(item)%2 != 0:
        if item[:len(item)//2] == item[(len(item)//2 + 1):]:
            print(item)
