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
from kivy_garden.zbarcam import ZBarCam
from kivy.uix.boxlayout import BoxLayout


class MainBox(BoxLayout):

    def __init__(self, **kwargs):
        super(MainBox, self).__init__(**kwargs)


class DemoApp(App):

    def build(self):
        return MainBox()


if __name__ == '__main__':
    DemoApp().run()
