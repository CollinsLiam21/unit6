word = input('Enter a word: ')
file = open('engmix.txt')

end = True
while end:
    for line in file:
        if line.strip() == word:
            print(word, 'is in the dictionary!')
            end = False

if end == True:
    print(word, 'is not in the dictionary :(')
        
        
    
