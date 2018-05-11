#Liam Collins
#5/11/18
#warmup16.py

file = open('engmix.txt')

for words in file:
    words = words.strip()
    if len(words) > 0:
        if words[0] == 'l' and words[-1] == 'c':
            print(words)
