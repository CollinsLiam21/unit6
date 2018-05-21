#Liam Collins
#5/21/18
#quiz6.py

file = open('engmix.txt')

#Program 1
letter = input('Enter a letter: ')
for line in file:
    if line.count(letter) == 4:
        print(line)
