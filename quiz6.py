#Liam Collins
#5/21/18
#quiz6.py

file = open('engmix.txt')

#Program 1
'''letter = input('Enter a letter: ')
for line in file:
    line = line.strip()
    if line.count(letter) == 4:
        print(line)

#Program 2
for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[4] == line[8]:
            print(line)
            break
            
#Program 3
letterz = input('Enter a letter: ')
num = int(input('Enter a number: '))
for line in file:
    line = line.strip()
    if len(line) > 0:
        if line[0] == letterz and len(line) == num:
            print(line)'''
            
#Program 5
vowel = ''
for line in file:
    if (line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')) > (vowel.count('a') + vowel.count('e') + vowel.count('i') + vowel.count('o') + vowel.count('u')):
        vowel = line
print(vowel)
        







