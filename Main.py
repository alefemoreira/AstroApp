#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.clock import Clock
from widgets import Sol, Meteoro, Planetas
from telas.Telas import *

Config.read('config.ini')

class Gerenciador(ScreenManager):
	def __init__(self, **kw):
		super().__init__(**kw)

class AtaqueDosMeteoros(Jogo):
    def __init__(self, **kw):
        super().__init__(**kw)

    def chamaPlayThru(self):
        Clock.schedule_interval(self.playThru, 1.0/120.0)

    def playThru(self, *args):
        self.ids.sol.giro(screen=self.size)
        self.ids.mercurio.movimentacao(self.size, self.size[0]*0.234, 0.25 * 4.14)
        self.ids.venus.movimentacao(self.size, self.size[0]*0.335 , 0.25 * 1.62)
        self.ids.terra.movimentacao(self.size, self.size[0]*0.445 , 0.25)
        self.ids.marte.movimentacao(self.size, self.size[0]*0.531 , 0.25 * 0.53)

class Main(App):
	def build(self):
		return Gerenciador()
	

Main().run()
