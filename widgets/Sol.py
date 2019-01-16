from kivy.uix.widget import Widget
from kivy.properties import ListProperty, StringProperty
from kivy.graphics import Color, Ellipse, Rotate, PushMatrix, PopMatrix
from kivy.graphics.transformation import Matrix
from math import sin, cos, pi

rotation = 0

class Sol(Widget):
    imagem = StringProperty(None) 
    tamanho = ListProperty([0, 0])
    Pos = [0, 0]
    screen = [0, 0]

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        global rotation
        self.canvas.before.clear()

        with self.canvas.before:
            Color(rgba=(1, 1, 1, 1))
            Ellipse(size=self.tamanho, source=self.imagem, pos=self.Pos)
            
            PushMatrix()
            Rotate(angle=rotation, origin=self.center)
            PopMatrix()

    def giro(self, screen=[1280, 720], *args):
        global rotation
        self.screen = screen
        self.Pos = [screen[0] / 2 - self.tamanho[0] / 2, screen[1] - self.tamanho[1] / 2]
        self.atualizar()
        rotation += 3
