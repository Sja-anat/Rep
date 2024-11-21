def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    
    lens = len(string)
    for i in range(lens):
        if string[i] in vowels:
            kevin += len(string[i:])
        else:
            stuart += len(string[i:])
    
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')
        
        
if __name__ == '__main__':
    #s = input()
    s = 'BANANA'
    minion_game(s)