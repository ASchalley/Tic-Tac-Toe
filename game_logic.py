import csv
from PyQt6.QtWidgets import *
from gamestart import *


class GameStart(QMainWindow, Ui_MainWindow1):


    def __init__(self) -> None:
        """
        Method to define variables and set up UI.
        """
        super().__init__()
        self.setupUi(self)


    def power(self) -> None:
        """
        Method to turn tv off and on.
        """
