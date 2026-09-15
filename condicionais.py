#  condicicionais - if else
# condicionais - if else
trabalho_terminado = False
if trabalho_terminado == True:
    print('Bora')
else:
    print('não posso sair')


estou_livre = input('você está livre? s/n')
if estou_livre == 's':
    print('OK, bora mover as caixas')
else:
    print('pede ajuda para o meu irmão')

# como lidar com mais que 2 condições?

atrasos = int(input('Quantas faltas você tem?'))
if atrasos >= 3:
    print('você está suspenso')
elif atrasos == 2:
    print('mais uma falta e estará suspenso')
elif atrasos == 1:
    print('mais duas faltas e estará suspenso')
else:
    print('pode entrar')

# Problema:
# Crie um programa que recebe dois valores e exibe qual é o valor maior

primero_valor = int(input( 'Digite o 1° valor '))
segundo_valor = int(input('Digite o 2° valor '))

if primero_valor > segundo_valor:
    print('O 1° valor é maior')
else:
    print('O 2° valor é maior')

    
