from kivy.uix.widget import Widget
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.graphics import Color, Ellipse
from math import sin, cos, pi

class Planetas(Widget):
	imagem = StringProperty(None)
	tamanho = ListProperty([100, 100])
	#raio = NumericProperty(0)
	#pos = ListProperty((0,0))

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
			Ellipse(size=self.tamanho, source=self.imagem)

	def movimentacao(r=100, v=10*pi/180, *args):
		print('hello')
