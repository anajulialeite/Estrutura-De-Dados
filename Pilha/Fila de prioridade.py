import heapq

class ListaPrioridade:
    def __init__(self):
        self.max_heap = []  # Para max heap
        self.min_heap = []  # Para min heap

    def adicionar(self, elemento):
        """Adiciona um número natural positivo à lista de prioridade."""
        if isinstance(elemento, int) and elemento > 0:
            # Para max heap, usamos o valor negativo
            heapq.heappush(self.max_heap, -elemento)
            heapq.heappush(self.min_heap, elemento)
            print(f'Elemento "{elemento}" adicionado à lista de prioridade.')
        else:
            print("Apenas números naturais positivos e inteiros podem ser adicionados.")

    def remover_maior(self):
        """Remove e retorna o maior elemento (max heap)."""
        if self.max_heap:
            maior = -heapq.heappop(self.max_heap)
            print(f'Maior elemento removido: {maior}')
            return maior
        else:
            print("A lista de prioridade está vazia.")

    def remover_menor(self):
        """Remove e retorna o menor elemento (min heap)."""
        if self.min_heap:
            menor = heapq.heappop(self.min_heap)
            print(f'Menor elemento removido: {menor}')
            return menor
        else:
            print("A lista de prioridade está vazia.")

    def ler_max_heap(self):
        """Retorna todos os elementos da max heap em ordem decrescente."""
        return sorted([-x for x in self.max_heap], reverse=True)

    def ler_min_heap(self):
        """Retorna todos os elementos da min heap em ordem crescente."""
        return sorted(self.min_heap)

# Exemplo de uso com números naturais positivos
lista_prioridade = ListaPrioridade()

# Adicionando apenas números naturais positivos
lista_prioridade.adicionar(10)
lista_prioridade.adicionar(5)
lista_prioridade.adicionar(20)
lista_prioridade.adicionar(15)
lista_prioridade.adicionar(3)

print("Elementos na max heap (maior para menor):", lista_prioridade.ler_max_heap())
print("Elementos na min heap (menor para maior):", lista_prioridade.ler_min_heap())

lista_prioridade.remover_maior()  # Remove 20
print("Elementos na max heap após remoção:", lista_prioridade.ler_max_heap())

lista_prioridade.remover_menor()  # Remove 3
print("Elementos na min heap após remoção:", lista_prioridade.ler_min_heap())
