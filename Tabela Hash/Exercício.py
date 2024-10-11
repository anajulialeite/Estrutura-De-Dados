class TabelaHash:
    ## Inicializa table com o tamanho 10
    def __init__(self, size=10):  
        self.tabela = [[] for _ in range(size)]

    ## Cria um hash
    def _hash(self, chave):
        return hash(chave) % len(self.tabela)
    
    ## Produz o hash em índice
    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])
    
    def buscar(self, chave):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None
    
    def deletar(self, chave):
        indice = self._hash(chave)
        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                del self.tabela[indice][i]
                return True
        return False


# Testando a classe TabelaHash
hash_table = TabelaHash()
hash_table.inserir("nome", "João")
hash_table.inserir("idade", 25)
print(hash_table.buscar("nome"))

hash_table.deletar("nome")
print(hash_table.buscar("nome"))


cinco_table = TabelaHash()
cinco_table.inserir("nome1", "César")
cinco_table.inserir("idade1", 42)

cinco_table.inserir("nome2", "Ana Júlia")
cinco_table.inserir("idade2", 32)

cinco_table.inserir("nome3", "Maria Clara")
cinco_table.inserir("idade3", 35)

cinco_table.inserir("nome4", "Cássia")
cinco_table.inserir("idade4", 62)

cinco_table.inserir("nome5", "Nelson")
cinco_table.inserir("idade5", 34)

cinco_table.deletar("nome2")
cinco_table.deletar("nome4")

# Iterando sobre os itens da tabela
for i in range(1, 6):  # Itera de 1 a 5
    print(cinco_table.buscar(f"nome{i}"))
