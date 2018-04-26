class Desenho:
    qnt_desenhos = 0
    desenhos = []

    def __init__(self):
        raise NotImplementedError

    def informacao():
        print("Essa clase eh responsavel pelos desenhos")


class Circulo(Desenho):
    def __init__(self, nome, centro, raio):
        super(Circulo).__init__()
        self.nome = nome
        self.centro = centro
        self.raio = raio
        self.qnt_desenhos += 1
        self.desenhos.append(self)


class Retangulo(Desenho):
    def __init__(self, nome, quina, largura, altura):
        super(Retangulo).__init__()
        self.nome = nome
        self.quina = quina
        self.largura = largura
        self.altura = altura
        self.qnt_desenhos += 1
        self.desenhos.append(self)


cir_1 = Circulo("bola", (0, 0), 5)
ret_1 = Retangulo("ret", (0, 0), 10, 20)
Desenho.informacao()
print(Desenho.qnt_desenhos)
for i in Desenho.desenhos:
    print(i.nome)

