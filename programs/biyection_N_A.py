
A = ['a', 'b', 'c'] # alphabet



### translation

base = len(A)
letter_to_value = { a:i+1 for i,a in enumerate(A) }
value_to_letter = { i+1:a for i,a in enumerate(A) }

wordToNatural = lambda w : sum([letter_to_value[a]*base**(i) for i,a in enumerate(w[::-1])])

print('')
def naturalToWord (value:int):
    symbol = ''

    
    if value > 0: 
        index = value % base
        quotient = value // base

        if index == 0:
            index = base
            quotient -= 1
            
        print( f'value: {value}\tquotient: {quotient}\trest: {index%base}\tsymbol: {value_to_letter[index] }\t')
        symbol = naturalToWord(quotient) + value_to_letter[index] 

    return symbol

 

# exercise 1
print('\n_______Exercise 1_______\n')
n = [143, 100]

for i in n:
    r =  naturalToWord(i)
    print(f'C({i}) = {r}, y Z({r}) = {wordToNatural(r)}')

    
#exercise 2
print('\n_______Exercise 2_______\n')
l = ['aabc', 'bac']
for i in l:
    r =  wordToNatural(i)
    print(f'Z({i}) = {r}, y C({r}) = {naturalToWord(r)}')

'''
_______Exercise 1_______

value: 143	quotient: 47	rest: 2	symbol: b	
value: 47	quotient: 15	rest: 2	symbol: b	
value: 15	quotient: 4	rest: 0	symbol: c	
value: 4	quotient: 1	rest: 1	symbol: a	
value: 1	quotient: 0	rest: 1	symbol: a	
C(143) = aacbb, y Z(aacbb) = 143
value: 100	quotient: 33	rest: 1	symbol: a	
value: 33	quotient: 10	rest: 0	symbol: c	
value: 10	quotient: 3	rest: 1	symbol: a	
value: 3	quotient: 0	rest: 0	symbol: c	
C(100) = caca, y Z(caca) = 100

_______Exercise 2_______

value: 45	quotient: 14	rest: 0	symbol: c	
value: 14	quotient: 4	rest: 2	symbol: b	
value: 4	quotient: 1	rest: 1	symbol: a	
value: 1	quotient: 0	rest: 1	symbol: a	
Z(aabc) = 45, y C(45) = aabc
value: 24	quotient: 7	rest: 0	symbol: c	
value: 7	quotient: 2	rest: 1	symbol: a	
value: 2	quotient: 0	rest: 2	symbol: b	
Z(bac) = 24, y C(24) = bac
'''
