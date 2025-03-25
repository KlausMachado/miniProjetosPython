from random import randint

def sorteando():
    n = (randint(1, 10), randint(1, 10), randint(1, 10))
    print(f"Os números sorteados foram: {n}")    
    print(f"O maior número entre todos é: {max(n)} e o menor é: {min(n)}")
sorteando()