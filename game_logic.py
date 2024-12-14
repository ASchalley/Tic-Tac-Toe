import random

from PyQt6.QtWidgets import *
from gamestart import *
from gameboard import *
from random import *

class GameStart(QMainWindow, Ui_MainWindow1):

    def __init__(self) -> None:
        """
        Method to set up UI.
        """
        super().__init__()
        self.setupUi(self)
        self.startGameButton.clicked.connect(lambda : self.startgame())

    def startgame(self) -> None:
        """
        Method to start game with selected settings.
        """
        self.storesettings()
        application = QApplication([])
        window = GameBoard()
        window.show()
        application.exec()

    def storesettings(self) -> None:
        """
        Method to write settings
        """
        if self.difficultyButton1.isChecked():
            diff = 1
        elif self.difficultyButton2.isChecked():
            diff = 2
        elif self.difficultyButton3.isChecked():
            diff = 3
        elif self.difficultyButton4.isChecked():
            diff = 4
        else:
            diff = 1
        if self.firstButton2.isChecked():
            first = 1
        elif self.firstButton3.isChecked():
            first = 2
        else:
            first = random.choice([1, 2])  # https://www.geeksforgeeks.org/random-numbers-in-python/
        file = open("data.txt", "w")
        file.write(str(diff) + "\n")
        file.write(str(first))
        file.close()


class GameBoard(QMainWindow, Ui_MainWindow2):

    def __init__(self) -> None:
        """
        Method to define variables and set up UI.
        """
        self.__difficulty = 1
        self.__first = 1
        super().__init__()
        self.takesettings()
        self.setupUi(self)

    def takesettings(self) -> None:
        """
        Method to retrieve settings
        """
        file = open("data.txt", "r")
        content = file.readlines() # https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
        self.__difficulty = content[0]
        self.__first = content[1]
        file.close()