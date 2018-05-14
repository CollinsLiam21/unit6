letter = input('Enter a letter: ')
file = open('lastWordDemo.py')

counter = ''
for line in file:
    line = line.strip()
    if line.count(letter) > counter.count(letter):
        counter = line
print(counter)






    
