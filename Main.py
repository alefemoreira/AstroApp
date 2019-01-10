#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.clock import Clock
from widgets import Sol, Meteoros, Planetas
from telas.Telas import *

Config.read('config.ini')


class Gerenciador(ScreenManager):
	def __init__(self, **kw):
		super().__init__(**kw)


class Main(App):
	def build(self):
		return Gerenciador()
	
	def chamaPlayThru(self):
		#Clock.schedule_interval(self.playThru, 1.0/120.0)
		pass

	def playThru(self):
		pass

Main().run()
