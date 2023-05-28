import os

print('==========')

operations = {
    '+': 'soma',
    '-': 'subtração',
    '*': 'muçtiplicação',
    '/': 'divisão',
    '^': 'exponencial'
}

while True:
    os.system('clear')
    i = 0

    for op, name in operations.items():
        print(i, ':', name)
        i += 1

os.system('clear')
i = 0

for op, name in operations.items():
    print(i, ':', name, '=', op)
    i += 1
