class Fila:
    # Inicia
    def __init__(self):
        self.elementos = []

    def enfileirar(self, elemento):
        """Adiciona um elemento ao final da fila."""
        self.elementos.append(elemento)
        print(f'Elemento "{elemento}" adicionado à fila.')

    def desenfileirar(self):
        """Remove e retorna o primeiro elemento da fila."""
        if not self.esta_vazia():
            elemento = self.elementos.pop(0) # Remove
            print(f'Elemento "{elemento}" removido da fila.')
            return elemento
        else:
            print("A fila está vazia.")

    def ler_elementos(self):
        """Retorna todos os elementos da fila."""
        return self.elementos

    def esta_vazia(self): # Mostra a lista vazia
        """Verifica se a fila está vazia."""
        return len(self.elementos) == 0

    def primeiro_elemento(self): # Mostra o primeiro elemento
        """Retorna o primeiro elemento da fila sem removê-lo."""
        if not self.esta_vazia():
            return self.elementos[0]
        else:
            print("A fila está vazia.")

    def ultimo_elemento(self): # Mostra o último elemento
        """Retorna o último elemento da fila sem removê-lo."""
        if not self.esta_vazia():
            return self.elementos[-1]
        else:
            print("A fila está vazia.")

# Exemplo de uso
minha_fila = Fila()
minha_fila.enfileirar('a')
minha_fila.enfileirar('b')
minha_fila.enfileirar('c')

print("Elementos na fila:", minha_fila.ler_elementos())

print("Primeiro elemento da fila:", minha_fila.primeiro_elemento())
print("Último elemento da fila:", minha_fila.ultimo_elemento())

minha_fila.desenfileirar()  # Remove 
print("Elementos na fila após desenfileirar:", minha_fila.ler_elementos())

print("Primeiro elemento da fila:", minha_fila.primeiro_elemento())
print("Último elemento da fila:", minha_fila.ultimo_elemento())

