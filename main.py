# -*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.config import Config

class SatcomRoot(BoxLayout):
    def show_fre_calculate_form(self):
        self.clear_widgets()
        fre_cal_form = Factory.FreCalculateForm()
        self.add_widget(fre_cal_form)

class SatcomIndex(BoxLayout):
    pass


class FreCalculateForm(BoxLayout):
    pass

class SatcomApp(App):
    pass

if __name__ == '__main__':
    Config.set('graphics', 'width', '270')
    Config.set('graphics', 'height', '480')
    SatcomApp().run()