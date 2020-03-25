print('Scrivi il messaggio da stampare e quante volte lo vuoi stampare\n')
mess = input('Messaggio --> ')
t = int(input('Numero --> '))
for i in range(t):
    print('{}\n'.format(mess))

