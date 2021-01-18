#!/usr/bin/env python
"""
This demo can be ran from the project root directory via:
```sh
python src/main.py
```
It can also be ran via p4a/buildozer.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

Builder.load_file('main.kv')


class ZBarPopup(Popup):

    def __init__(self, **kwargs):
        super(ZBarPopup, self).__init__(**kwargs)


class ZBar(BoxLayout):

    def __init__(self, **kwargs):
        super(ZBar, self).__init__(**kwargs)

        self.zbarpopup = ZBarPopup()
        self.symbols = self.zbarpopup.ids.zbarcam.symbols
        self.zbarpopup.bind(on_dismiss=self.process_characters)

        self.label = self.ids.label

    def get_qrcode(self):
        self.zbarpopup.open()

    def process_characters(self, *args):
        self.label.text = ', '.join([str(symbol.data) for symbol in self.symbols])


class DemoApp(App):

    def build(self):
        return ZBar()


if __name__ == '__main__':
    DemoApp().run()
