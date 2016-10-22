from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton
from kivy.uix.label import Label
from kivy.factory import Factory
import json

class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    addlocationform = ObjectProperty()
    def show_current_weather(self, location=None):
        self.clear_widgets()
        if self.current_weather is None:
            self.current_weather = CurrentWeather()

        if location is not None:
            self.current_weather.location = location
            self.current_weather.update_weather()
            self.add_widget(self.current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.addlocationform = AddLocationForm()
        self.add_widget(self.addlocationform)

class LocationButton(ListItemButton):
    location = ListProperty()

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/" + "find?q={}&type=like&appid=2233c2ce7363b83f8bc8c182f74316bc"
        qstring = self.search_input.text
        print qstring
        if qstring == "":
            qstring = "Beijing"
        search_url = search_template.format(qstring)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = [(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities
        del self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()

    def args_converter(self, index, data_item):
        city, country = data_item
        return {'location': (city, country)}

class CurrentWeather(BoxLayout):
    location = ListProperty(['Beijing', 'CN'])
    conditions = StringProperty()
    temp = NumericProperty()
    # temp_min = NumericProperty()
    # temp_max = NumericProperty()
    wind_speed = NumericProperty()
    wind_deg = NumericProperty()
    dt = NumericProperty()
    def update_weather(self):
        weather_template = "http://api.openweathermap.org/data/2.5/" + "weather?q={},{}&units=metric&appid=2233c2ce7363b83f8bc8c182f74316bc"
        weather_url = weather_template.format(*self.location)
        request = UrlRequest(weather_url, self.weather_retrieved)
    def weather_retrieved(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        self.conditions = data['weather'][0]['description']
        self.temp = data['main']['temp']
        self.dt = data['dt']
        self.wind_speed = data['wind']['speed']
        self.wind_deg = data['wind']['deg']
        # self.temp_min = data['main']['temp_min']
        # self.temp_max = data['main']['temp_max']

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
