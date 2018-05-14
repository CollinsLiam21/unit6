num = int(input('Enter a number: '))
file = open('engmix.txt')

new = []
for line in file:
    line = line.strip()
    if len(line) > 0:
        new.append(line)

print('The',num,'th word is',new[num-1])


    
