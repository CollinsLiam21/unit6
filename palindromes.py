#Liam Collins
#5/11/18
#palindromes.py

file = open('engmix.txt')


for item in file:
    item = item.strip()
    anotherList = []
    anotherList.append(item)
    new = ''
    for ch in item:
        new = ch + new
    newList = new.split(' ')
    if anotherList == newList:
        print(item)
    
    


