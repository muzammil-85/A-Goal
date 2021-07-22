from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
import winsound
import time


class AGoal(MDApp):
    # make beep sound
    def beep(self):
        freq = 700
        dur = 50
        # loop iterates 5 times i.e, 5 beeps will be produced.
        for i in range(0, 5):
            winsound.Beep(freq, dur)
            dur += 100
    def relax(self):
        relaxtime = self.input1.text
        splt = relaxtime.split(':')
        hour = int(splt[0])
        minute = int(splt[1])
        minutes = (hour * 60) + minute
        seconds = minutes * 60
        t = int(seconds)
        self.setted.text = f"Time setted {relaxtime}"
        #raise Exception:
            #self.setted.text = "Please provide a valid time"

        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.beep()


    def set(self, args):
        self.setted.text = "Time setted"
        # input time in seconds
        studytime = self.input1.text
        splt = studytime.split(':')
        hour = int(splt[0])
        minute = int(splt[1])
        minutes = (hour * 60) + minute
        seconds = minutes * 60
        t = int(seconds)

        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.beep()
        self.relax()

    def reset(self, args):
        self.input1.text = "HH:MM"
        self.input2.text = "HH:MM"
        self.resetted.text = "Time Resetted"


    def build(self):
        # INITIALIZE SCREEN
        screen = MDScreen()

        # TOP TOOLBAR
        self.toolbar = MDToolbar(title="A-GOAL")
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)

        # STUDY TIME
        self.label = MDLabel(
            text="Study Time",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            theme_text_color="Secondary"
        )
        screen.add_widget(self.label)

        # STUDY TIME FIELD
        self.input1 = MDTextField(
            text="HH:MM",
            halign="center",
            size_hint=(0.3, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            font_size=22
        )
        screen.add_widget(self.input1)

        # RELAX TIME
        self.label = MDLabel(
            text="Relax Time",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            theme_text_color="Secondary"
        )
        # RELAX TIME
        self.input2 = MDTextField(
            text="HH:MM",
            halign="center",
            size_hint=(0.3, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=22
        )
        screen.add_widget(self.label)
        screen.add_widget(self.input2)

        # SET BUTTON
        screen.add_widget(MDFillRoundFlatButton(
            text="SET",
            font_size=17,
            pos_hint={"center_x": 0.45, "center_y": 0.25},
            on_press=self.set

        ))

        # RESET BUTTON
        screen.add_widget(MDFillRoundFlatButton(
            text="RESET",
            font_size=17,
            pos_hint={"center_x": 0.58, "center_y": 0.25},
            on_press=self.reset
        ))

        self.setted = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            theme_text_color="Secondary",
            font_style="H5"
        )

        self.resetted = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            theme_text_color="Secondary",
            font_style="H5"
        )
        screen.add_widget(self.setted)
        screen.add_widget(self.resetted)

        self.name1 = MDLabel(
            text="Achieve Goal",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            theme_text_color="Secondary",
            font_style="H5"
        )
        screen.add_widget(self.name1)

        return screen


if __name__ == '__main__':
    AGoal().run()
