#Liam Collins
#5/10/18
#longestDictionaryWord.py

file = open('engmix.txt')

longest = 0
for item in file:
    if len(item) > longest:
        longest = item
print(longest)
