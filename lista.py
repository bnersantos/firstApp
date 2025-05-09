# Etapa 1 criar uma lista com 5 objetos
lista = ['lápis','borracha','caneta','mochila','tesoura']
# Printar os obejtos da lista
for objetos in lista:
    print(f'Objetos:{objetos}')

# Adicionar mais um objeto ao final da lista
item_novo = 'apontador'
lista.append(item_novo)
# Printar objeto adicionado
print(f'Item novo:{item_novo} adicionado com sucesso!')

for objetos in lista:
    print(objetos)

# Acessar o segundo objeto da lista e printar
print(f'Printar o segundo objeto da lista: {lista[1]}')

# Remover um objeto da lista
remover_item = 'caneta'
lista.remove(remover_item)
print(f'Objeto removido : {remover_item} removido com sucesso!')
for objetos in lista:
    print(f'lista: {objetos}')

# Exibir o tamanho da lista
print(f'A quantidade de itens na lista é:',len(lista))

# Mostrar todos os itens com laço for
for objetos in lista:
    print(f'item: {objetos}')

# Verificar se cadeira está na lista. Se sim remover senão adicionar
if 'cadeira' in lista:
    remover = 'cadeira'
    lista.remove('cadeira')
    print(f'{remover} removido com sucesso!')
    print(f'{lista}')
else:
    adicionar = 'cadeira'
    lista.append(adicionar)
    print(f'{adicionar} adicionado com sucesso!')
    print(f'{lista}')
# Ordenar a lista em ordem alfabética
lista.sort()
print(lista)
# Exibir o primeiro e o último objeto
print(f'Primeiro: {lista[0]}, Último: {lista[5]}')
# Limpar toda a lista
lista.clear()
print('Lista limpada com sucesso!')
print(lista)



