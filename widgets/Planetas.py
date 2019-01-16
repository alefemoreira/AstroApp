from kivy.uix.widget import Widget
from kivy.properties import ListProperty, StringProperty
from kivy.graphics import Color, Ellipse
from math import sin, cos, pi

x = 0

class Planetas(Widget):
    imagem = StringProperty(None)
    tamanho = ListProperty([100, 100])
    Pos = [0, 0]
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()

        with self.canvas.before:
            Color(rgba=(1,1,1,1))
            Ellipse(size=self.tamanho, source=self.imagem, pos=self.Pos)

    def movimentacao(self, screenSize, r=100, v=10, *args):
        global x

        width = screenSize[0]
        height = screenSize[1]

        self.Pos[0] = (width / 2) + r * cos((x / 180 * pi) * v)
        self.Pos[1] = height + r * sin((x / 180 * pi) * v)

        x += 1

        self.atualizar()
