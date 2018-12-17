class Retangulo:
    def verifica_fora_dentro(self, pontos):
        """Verifica se os pontos estão dentro."""
        x, y = pontos
        if x < self.x or x > (self.x + self.largura):
            return False
        elif y < self.y or y > (self.y + self.altura):
            return False
        return True

    def __init__(self, x, y, largura, altura):
        """Insere os valores de x,y largura e altura"""
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y
