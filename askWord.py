
file = open('lastWordDemo.py')

new = []
for line in file:
    line = line.strip()
    if len(line)>0:
        new.append(line)

for word in new:
    print(word,'!')






    
