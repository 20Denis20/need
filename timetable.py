import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

time = time.localtime(time.time())

wday = time.tm_wday
time1 = time.tm_hour
time2 = time.tm_min


class TestApp(App):

    def change_text(self, instance):
        if wday == 0 and time1 <= 8 and time2 <= 30:
            self.label.text = "английский"
        elif wday == 0 and time1 <= 9 and time2 <= 25:
            self.label.text = "литература"
        elif wday == 0 and time1 <= 10 and time2 <= 20:
            self.label.text = "ФК"
        elif wday == 0 and time1 <= 11 and time2 <= 15:
            self.label.text = "математика"
        elif wday == 0 and time1 <= 12 and time2 <= 30:
            self.label.text = "биология"
        elif wday == 0 and time1 <= 13 and time2 <= 25:
            self.label.text = "музыка"
        elif wday == 0 and time1 <= 14 and time2 <= 20:
            self.label.text = "риторика"
        elif wday == 0 and time1 >= 15 and time2 > 5:
            self.label.text = "всё!"

        elif wday == 1 and time1 <= 8 and time2 <= 30:
            self.label.text = "география"
        elif wday == 1 and time1 <= 9 and time2 <= 25:
            self.label.text = "русский"
        elif wday == 1 and time1 <= 10 and time2 <= 20:
            self.label.text = "ОБЖ"
        elif wday == 1 and time1 <= 11 and time2 <= 15:
            self.label.text = "химия"
        elif wday == 1 and time1 <= 12 and time2 <= 30:
            self.label.text = "математика"
        elif wday == 1 and time1 <= 13 and time2 <= 25:
            self.label.text = "физика"
        elif wday == 1 and time1 <= 14 and time2 <= 20:
            self.label.text = "математика"
        elif wday == 1 and time1 >= 15 and time2 > 5:
            self.label.text = "всё!"

        elif wday == 2 and time1 <= 8 and time2 <= 30:
            self.label.text = "английский"
        elif wday == 2 and time1 <= 9 and time2 <= 25:
            self.label.text = "биология"
        elif wday == 2 and time1 <= 10 and time2 <= 20:
            self.label.text = "русский"
        elif wday == 2 and time1 <= 11 and time2 <= 15:
            self.label.text = "франзуский"
        elif wday == 2 and time1 <= 12 and time2 <= 30:
            self.label.text = "литература"
        elif wday == 2 and time1 <= 13 and time2 <= 25:
            self.label.text = "информатика"
        elif wday == 2 and time1 <= 14 and time2 <= 20:
            self.label.text = "обществознание"
        elif wday == 2 and time1 >= 15 and time2 > 5:
            self.label.text = "всё!"

        elif wday == 3 and time1 <= 8 and time2 <= 30:
            self.label.text = "русский"
        elif wday == 3 and time1 <= 9 and time2 <= 25:
            self.label.text = "русский"
        elif wday == 3 and time1 <= 10 and time2 <= 20:
            self.label.text = "ФК"
        elif wday == 3 and time1 <= 11 and time2 <= 15:
            self.label.text = "математика"
        elif wday == 3 and time1 <= 12 and time2 <= 30:
            self.label.text = "математика"
        elif wday == 3 and time1 <= 13 and time2 <= 25:
            self.label.text = "физика"
        elif wday == 3 and time1 >= 15 and time2 > 5:
            self.label.text = "всё!"

        elif wday == 4 and time1 <= 10 and time2 <= 20:
            self.label.text = "русский"
        elif wday == 4 and time1 <= 11 and time2 <= 15:
            self.label.text = "русский"
        elif wday == 4 and time1 <= 12 and time2 <= 30:
            self.label.text = "ФК"
        elif wday == 4 and time1 <= 13 and time2 <= 25:
            self.label.text = "математика"
        elif wday == 4 and time1 <= 14 and time2 <= 20:
            self.label.text = "математика"
        elif wday == 4 and time1 <= 15 and time2 <= 5:
            self.label.text = "всё!"

        elif wday == 5 and time1 <= 9 and time2 <= 25:
            self.label.text = "русский"
        elif wday == 5 and time1 <= 10 and time2 <= 20:
            self.label.text = "русский"
        elif wday == 5 and time1 <= 11 and time2 <= 15:
            self.label.text = "ФК"
        elif wday == 5 and time1 <= 12 and time2 <= 0:
            self.label.text = "всё!"

        elif wday == 6:
            self.label.text = "уроков нет!"

    def build(self):
        bl = BoxLayout()
        self.label = Label(text="")
        bl.add_widget(Button(text="следующий урок", on_press=self.change_text))
        bl.add_widget(self.label)

        return bl


if __name__ == '__main__':
    TestApp().run()