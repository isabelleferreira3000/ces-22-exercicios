import turtle

def desenhando_quadrado_com_a_turtle():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.color("blue")

    for i in range(4):
        tess.forward(100)
        tess.left(90)
    wn.mainloop()

def mostre_qual_funcao_chamei(funcao):
    def mostre(*args, **kwds):
        print("Chamando", funcao.__name__)
        return funcao(*args, **kwds)
    return mostre


quadrado = mostre_qual_funcao_chamei(desenhando_quadrado_com_a_turtle)
quadrado()
