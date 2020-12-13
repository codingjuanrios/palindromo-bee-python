"""
Una aplicación para comprobar palíndromos
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, BOTTOM

#IMPORT
import json
import random
import os
import time


class PalindrApp(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        pal_label = toga.Label(
            'Introduce un palíndromo: ',
            style=Pack(padding=(0,5))
        )
        self.pal_input = toga.TextInput(style=Pack(flex=1))

        pal_box = toga.Box(style=Pack(direction=ROW, padding=5))
        pal_box.add(pal_label)
        pal_box.add(self.pal_input)

        button = toga.Button(
            'Comprobar',
            on_press=self.comprobar,
            style=Pack(padding=5)
        )

        saber_label = toga.Label(
            'Aquí tiene un palíndromo de regalo: ',
            style=Pack(direction=COLUMN, flex=1, alignment=BOTTOM, padding=(0,5))
        )

        with open("src/palindrapp/resources/listado.json", "r", encoding="utf-8") as read_file:
            listado = json.load(read_file)
            elegido = random.choice(listado)['palindromo']
            regalo_label = toga.Label(
                "{}".format(elegido)
            )

        regalo_box = toga.Box(style=Pack(direction=ROW, padding=5, background_color=red))
        regalo_box.add(saber_label)
        regalo_box.add(regalo_label)


        main_box.add(pal_box)
        main_box.add(button)
        main_box.add(regalo_box)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def comprobar(self, widget):

        Pal = self.pal_input.value

        palmin = Pal.lower()

        pallimpio = palmin.replace(' ','').replace(',','').replace(';','').replace('.','').replace(':','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')

        palgirado = pallimpio[::-1]

        if pallimpio == palgirado:
            self.main_window.info_dialog(
                '¡Comprobado!',
                "Efectivamente, {} es un palíndromo".format(self.pal_input.value)
            )
            espal = True
        else:
            self.main_window.info_dialog(
                'Oh,no!',
                "Lamentablemente, {} no es un palíndromo".format(self.pal_input.value)
            )
            espal = False


def main():
    return PalindrApp()
