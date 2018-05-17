#Liam Collins
#5/17/18
#warmup18.py

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if 'c' in line and 'o' in line and 'l' in line and 'i' in line and 'n' in line and 's' in line:
        print(line)
