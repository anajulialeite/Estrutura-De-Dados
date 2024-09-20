#Crie uma lista vazia para representar a pilha.
#Adicione os elementos "A", "B" e "C" à pilha.
#Exiba o item no topo da pilha (sem removê-lo).
#Remova dois itens da pilha e mostre o valor de cada um.
#Verifique o tamanho atual da pilha.
#Verifique se a pilha está vazia.
#Remova o último item e mostre o status da pilha novamente.

# Crie uma lista vazia para representar a pilha
pilha = []
# Adicione os elementos "A", "B" e "C" à pilha
pilha.append("A")
pilha.append("B")
pilha.append("C")
# Exiba o item no topo da pilha (sem removê-lo)
print("Item no topo da pilha:", pilha[-1])
# Remova dois itens da pilha e mostre o valor de cada um
print("Item removido 1:", pilha.pop())
print("Item removido 2:", pilha.pop())
# Verifique o tamanho atual da pilha
tamanho = len(pilha)
print("Tamanho atual da pilha:", tamanho)
# Verifique se a pilha está vazia
esta_vazia = len(pilha) == 0
print("A pilha está vazia?", esta_vazia)
# Remova o último item e mostre o status da pilha novamente
if not esta_vazia:
    pilha.pop()
print("Status da pilha após remoção:", pilha)