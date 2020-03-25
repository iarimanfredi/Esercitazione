def tree(n):
    for j in range(n+1):
        print('{}'.format(mess), end = ' ')
    print('\n')

print('Scrivi il messaggio da stampare e quante volte lo vuoi stampare\n')
mess = input('Messaggio --> ')
t = int(input('Numero --> '))
for i in range(t):
    tree(i)

