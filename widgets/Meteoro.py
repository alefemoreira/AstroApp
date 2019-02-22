from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ListProperty, StringProperty
from kivy.graphics import Color, Ellipse, Rectangle
from math import sin, cos, pi

class Meteoro(Widget):
    tamanho = ListProperty([40, 102])
    imagem = StringProperty('img/giphy.gif')
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
            #Rectangle(size=self.tamanho, source=self.imagem, pos=self.Pos)
            Image(source=self.imagem, pos=self.Pos, size=self.tamanho)

    def upPosition(self, *args):
        pass
