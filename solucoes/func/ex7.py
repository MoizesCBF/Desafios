# Solução proposta por @Sithis#7545

test1 = 'I Love You'
test2 = 'ata po bls'
test3 = 'this is a phrase'

def calc(string):
    numbers = []
    for word in string.split(' '):
        numbers.append(str(len(word)))
    print("-".join(numbers))

calc(test1)
calc(test2)
calc(test3)
