from kivy.uix.widget import Widget
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.graphics import Color, Ellipse
from math import sin, cos, pi

class Planetas(Widget):
    imagem = StringProperty(None)
    tamanho = ListProperty([100, 100])
    #raio = NumericProperty(0)
    Pos = [100, 0]
    
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

    def movimentacao(self, r=100, v=10*pi/180, *args):
        self.Pos[0] += 10
        self.atualizar()
        #pass
        #print('hello')
