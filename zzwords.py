#Liam Collins
#5/10/18
#zzwords.py

file = open('engmix.txt')


for line in file:
    if 'zz' in line:
        print(line.strip())

