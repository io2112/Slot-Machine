import sys
import random
import winsound
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5 import uic


class SlotMachine(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('slot.ui', self)

        #symbols
        self.symbols = ['🍒', '🍋', '🍊', '🔔', '⭐', '💎', '7']

        self.pushButton.clicked.connect(self.spin)
        self.checkBox.clicked.connect(self.sound_toggle)
        self.radioButton.clicked.connect(self.auto_mode)
        self.lineEdit.textChanged.connect(self.name_change)

        self.sound_on = False
        self.auto_spin_on = False
        self.player_name = ""

        #autospin timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.spin)

        self.label1.setText('?')
        self.label2.setText('?')
        self.label3.setText('?')

    def spin(self):
        slot1 = random.choice(self.symbols)
        slot2 = random.choice(self.symbols)
        slot3 = random.choice(self.symbols)
        self.label1.setText(slot1)
        self.label2.setText(slot2)
        self.label3.setText(slot3)

        #check if the player won
        if slot1 == slot2 == slot3:
            if self.player_name != None:
                print(self.player_name + " WON!")
            else:
                print("YOU WON!")

            #win sound
            if self.sound_on == True:
                try:
                    winsound.PlaySound('win.wav', winsound.SND_FILENAME)
                except:
                    pass  # sound file might not exist
        else:
            print("Try again")

    def sound_toggle(self):
        if self.checkBox.isChecked():
            self.sound_on = True
            print("Sound is on")
        else:
            self.sound_on = False
            print("Sound is off")

    #autospin
    def auto_mode(self):
        if self.radioButton.isChecked():
            self.auto_spin_on = True
            print("Auto spin is on")
            #spin interval set to 0.5 sec
            self.timer.start(500)
        else:
            self.auto_spin_on = False
            print("Auto spin is off")
            #stop autospin
            self.timer.stop()

    def name_change(self):
        self.player_name = self.lineEdit.text()
        if len(self.player_name) > 0:
            print("Hello " + self.player_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SlotMachine()
    window.show()
    app.exec_()