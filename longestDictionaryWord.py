#Liam Collins
#5/10/18
#longestDictionaryWord.py

file = open('engmix.txt')

longest = ''
for item in file:
    if len(item) > len(longest):
        longest = item
print(longest)
