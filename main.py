# -*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.config import Config
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty

class SatcomRoot(BoxLayout):
    def show_fre_calculate_form(self):
        self.clear_widgets()
        fre_cal_form = Factory.FreCalculateForm()
        self.add_widget(fre_cal_form)

class SatcomIndex(BoxLayout):
    pass


class FreCalculateForm(BoxLayout):
    fre_shift = ObjectProperty()
    fre_interval = ObjectProperty()
    land_receive = ObjectProperty()
    land_emit = ObjectProperty()
    plane_emit = ObjectProperty()
    plane_receive = ObjectProperty()
    notice = ObjectProperty()

    def calculate_frequency(self):
        land_receive_value = self.land_receive.text
        fre_shift_value = self.fre_shift.text
        fre_interval_value = self.fre_interval.text

        land2 = int(land_receive_value)
        shift = int(fre_shift_value)
        interval = int(fre_interval_value)

        plane1 = land2 + shift
        plane2 = land2 - interval
        land1 = plane2 + shift
        self.plane_emit.text = str(plane1)
        self.plane_receive.text = str(plane2)
        self.land_emit.text = str(land1)
        self.notice.text = "Good Job!"


class SatcomApp(App):
    pass

if __name__ == '__main__':
    Config.set('graphics', 'width', '270')
    Config.set('graphics', 'height', '480')
    SatcomApp().run()