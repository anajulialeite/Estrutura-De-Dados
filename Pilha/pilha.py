class Pilha:
    #inicia 
    def __init__(self):
        self.itens = [] 

    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        self.itens.append(item)

    def desempilhar(self):
        """Remove e retorna o item do topo da pilha. Lança um erro se a pilha estiver vazia."""
        if not self.vazia():
            return self.itens.pop() #remove
        else:
            raise IndexError("Desempilhando de uma pilha vazia.")

    def topo(self):
        """Retorna o item do topo da pilha sem removê-lo. Lança um erro se a pilha estiver vazia."""
        if not self.vazia():
            return self.itens[-1]
        else:
            raise IndexError("Pilha vazia, não é possível acessar o topo.")

    def atualizar_topo(self, novo_item):
        """Atualiza o item do topo da pilha. Lança um erro se a pilha estiver vazia."""
        if not self.vazia():
            self.itens[-1] = novo_item
        else:
            raise IndexError("Pilha vazia, não é possível atualizar o topo.")

    def listar(self):
        """Retorna todos os itens da pilha."""
        return self.itens[::-1]  # Retorna uma cópia da pilha em ordem do topo para a base

    def vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0

    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return len(self.itens)

# Exemplo de uso
if __name__ == "__main__":
    p = Pilha()
    
    # Criar
    p.empilhar(1)
    p.empilhar(2)
    p.empilhar(3)

    # Ler
    print("Topo da pilha:", p.topo())  
    print("Itens na pilha:", p.listar()) 
    
    # Atualizar
    p.atualizar_topo(99)
    print("Novo topo da pilha após atualização:", p.topo())  

    # remover
    print("Desempilhando:", p.desempilhar()) 
    print("Itens na pilha após desempilhar:", p.listar())  

    while not p.vazia():
        print("Desempilhando:", p.desempilhar())

    print("A pilha está vazia?", p.vazia())  
