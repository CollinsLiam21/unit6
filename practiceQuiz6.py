#Liam Collins
#5/18/18
#practiceQuiz6.py

file = open('engmix.txt')

#Program 1
for line in file:
    line = line.strip()
    if line.count('c') == 3 and line.count('p') == 2:
        print(line)

#Program 2
i = 0
for line in file:
    line = line.strip()
    if len(line) > 0:
        if line[0] == 'r':
            i += 1
print(i)

#Program 3
number = int(input('Enter a number: '))
for line in file:
    line = line.strip()
    if len(line) == number:
        print(line)
        break
    
#Program 4
tot = 0
letter = input('Enter a letter: ')
for line in file:
    if letter not in line:
        tot += 1
print(tot)

#Program 5
new = []
for line in file:
    if len(line) > 0:
        new.append(line)

print(new[len(new)//2])




