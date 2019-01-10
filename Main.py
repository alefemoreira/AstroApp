#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from widgets import Sol, Meteoros, Planetas
from telas.Telas import *

Config.read('config.ini')


class Gerenciador(ScreenManager):
    def __init__(self, **kw):
        super().__init__(**kw)


class Main(App):
    def build(self):
        return Gerenciador()


Main().run()
