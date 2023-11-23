class Matriz:
    def __init__(self):
        self.el = []

    def append(self, linha, coluna, valor):
        try:
            l = self.el[linha]
        except IndexError:
            # Se a linha não existe, insere uma nova lista vazia para essa linha
            self.el.insert(linha, [])
            l = self.el[linha]

        try:
            l[coluna] = valor
        except IndexError:
            # Se a coluna não existe, insere o valor diretamente na posição correta
            while len(l) <= coluna:
                l.append("0")

        l[coluna] = valor

    def __str__(self):
        string = ""
        for linhas in range(len(self.el),-1, -1):
            for el in self.ellinhas:
                string = f"{string}{el.ljust(10, ' ')}"
            string = f"{string}\n"

        return string