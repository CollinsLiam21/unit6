word = input('Enter a word: ')
file = open('engmix.txt')

end = True
for line in file:
    if line.strip() == word:
        print(word, 'is in the dictionary!')
        end = False
        break

if end == True:
    print(word, 'is not in dictionary')
    
