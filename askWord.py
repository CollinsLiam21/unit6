file = open('engmix.txt')


letter = input('Enter a letter: ')
counter = ''
for line in file:
    line = line.strip()
    if line.count(letter) > counter.count(letter):
        counter = line
print(counter)


word = input('Enter a word: ')
inD = False
for line in file:
    line = line.strip()
    if word == line:
        print('In dictionary')
        inD = True
        break
if not inD:
    print('no')
    

num = int(input('enter a number: '))
L = []
for line in file:
    line = line.strip()
    L.append(line)
print(L[num-1])

stuff = open('lastWordDemo.py')
for line in stuff:
    print(line.strip() + '!')




    
