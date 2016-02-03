import random

dictionary = {}
with open('./diceware_wordlist.txt','r') as f:
    linelist = []
    code = 0
    for i, line in enumerate(f):
        if i > 1 and code < 66666:
            code,word = line.split('\t')
            code = int(code)
            word = word.split('\n')[0]
            dictionary[code] = word
            linelist.append(line)
            #if i < 20:
                #print code, word
    #print dictionary

words = []
for word_num in range(7):
    word = ''
    for digit in range(5):  
        
        x = random.randint(1,6)
        #print(x)
        word += str(x)
        #print(word)
    word = int(word)
    #print('-------------')
    #print(word)
    #print('-------------')
    words.append(word)
#print(words)

for word in words:
    print(dictionary[word])
