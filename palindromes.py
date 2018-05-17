#Liam Collins
#5/11/18
#palindromes.py

file = open('engmix.txt')


for item in file:
    item = item.strip()
    new = ''
    for ch in item:
        new = ch + new
    if new == item:
        print(item)
    
    


