import random

name = input('Who are you?')

print('Hello,',name,'!')

print('Tossing a coin...')
Head = 0
Tails = 0
for i in range(1,4):
    bo = random.randint(0,1)
    if(bo):
        value = 'Head'
        Head +=1
    else:
        value = 'Tails'
        Tails += 1
    
    print('Round',i,':',value)

print('Heads:', Head,', Tails:' , Tails)

if Head > Tails:
    print(name,'won!')
else:
    print(name,'lost!')