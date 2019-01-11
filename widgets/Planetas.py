from kivy.uix.widget import Widget
from kivy.properties import ListProperty, StringProperty
from kivy.graphics import Color, Ellipse

class Planetas(Widget):
	imagem = StringProperty(None)
	tamanho = ListProperty([100, 100])

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
