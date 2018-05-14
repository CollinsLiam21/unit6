word = input('Enter a word: ')
file = open('engmix.txt')
filzz = open('engmix.txt').split()

end = True
while end:
    for line in file:
        if line.strip() == word:
            print(word, 'is in the dictionary!')
            end = False

        
        
    
