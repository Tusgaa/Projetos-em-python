n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
#vendo qual valor é menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor valor é {}.'.format(menor))
#vendo qual valor é maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O maior valor é {}.'.format(maior))
