word = input('Enter a word: ')
file = open('engmix.txt')

end = True
while end == True:
    for line in file:
        if line == word:
            print(word, 'is in the dictionary!')
            end = False
        
        
    
