letter = input('Enter a letter: ')
file = open('lastWordDemo.py')

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


    
