#Liam Collins
#5/18/18
#practiceQuiz6.py

file = open('engmix.txt')

#Program 1
for line in file:
    line = line.strip()
    if line.count('c') == 3 and line.count('p') == 2:
        print(line)
