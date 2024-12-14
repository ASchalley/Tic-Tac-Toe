import random

from PyQt6.QtWidgets import *
from gamestart import *
from gameboard import *
from random import *

class GameStart(QMainWindow, Ui_MainWindow):

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
        if diff == 4:
            first = 2
        file.write(str(first))
        file.close()


class GameBoard(QMainWindow, Ui_MainWindow2):

    def __init__(self) -> None:
        """
        Method to define variables and set up UI.
        """
        self.__difficulty = 1
        self.__first = 1
        self.__chosen = []
        super().__init__()
        self.takesettings()
        self.setupUi(self)
        self.submitButton.clicked.connect( lambda : self.humanmove())

    def takesettings(self) -> None:
        """
        Method to retrieve settings
        """
        file = open("data.txt", "r")
        content = file.readlines() # https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
        self.__difficulty = content[0]
        self.__first = content[1]
        file.close()

    def computermove(self) -> None:
        """
        Method to place computers O
        """
        if self.__difficulty == 1:
            move = random.choice([1,2,3,4,5,6,7,8,9])
            while move in self.__chosen:
                move = random.choice([1,2,3,4,5,6,7,8,9])
        elif self.__difficulty == 2:
            pass
        elif self.__difficulty == 3:
            pass
        elif self.__difficulty == 4:
            pass


    def humanmove(self) -> None:
        """
        Method to submit human move
        """
        if self.spot1.isChecked():
            self.spot1.hide()
            self.label1.setText("X")
            self.__chosen.append(1)
            self.computermove()
        elif self.spot2.isChecked():
            self.spot2.hide()
            self.label2.setText("X")
            self.__chosen.append(2)
            self.computermove()
        elif self.spot3.isChecked():
            self.spot3.hide()
            self.label3.setText("X")
            self.__chosen.append(3)
            self.computermove()
        elif self.spot4.isChecked():
            self.spot4.hide()
            self.label4.setText("X")
            self.__chosen.append(4)
            self.computermove()
        elif self.spot5.isChecked():
            self.spot5.hide()
            self.label5.setText("X")
            self.__chosen.append(5)
            self.computermove()
        elif self.spot6.isChecked():
            self.spot6.hide()
            self.label6.setText("X")
            self.__chosen.append(6)
            self.computermove()
        elif self.spot7.isChecked():
            self.spot7.hide()
            self.label7.setText("X")
            self.__chosen.append(7)
            self.computermove()
        elif self.spot8.isChecked():
            self.spot8.hide()
            self.label8.setText("X")
            self.__chosen.append(8)
            self.computermove()
        elif self.spot9.isChecked():
            self.spot9.hide()
            self.label9.setText("X")
            self.__chosen.append(9)
            self.computermove()

    def wincheck(self) -> None:
        """
        Method to check if a move wins.
        """
        if self.label1 == "X":
            if self.label2 == "X":
                if self.label3 == "X":
                    self.placeLabel.setText("You Win!")
            if self.label4 == "X":
                if self.label7 == "X":
                    self.placeLabel.setText("You Win!")
            if self.label5 == "X":
                if self.label9 == "X":
                    self.placeLabel.setText("You Win!")
        if self.label2 == "X":
            if self.label5 == "X":
                if self.label8 == "X":
                    self.placeLabel.setText("You Win!")
        if self.label3 == "X":
            if self.label6 == "X":
                if self.label9 == "X":
                    self.placeLabel.setText("You Win!")
            if self.label5 == "X":
                if self.label7 == "X":
                    self.placeLabel.setText("You Win!")
        if self.label4 == "X":
            if self.label5 == "X":
                if self.label6 == "X":
                    self.placeLabel.setText("You Win!")
        if self.label7 == "X":
            if self.label8 == "X":
                if self.label9 == "X":
                    self.placeLabel.setText("You Win!")

        if self.label1 == "O":
            if self.label2 == "O":
                if self.label3 == "O":
                    self.placeLabel.setText("You Lose!")
            if self.label4 == "O":
                if self.label7 == "O":
                    self.placeLabel.setText("You Lose!")
            if self.label5 == "O":
                if self.label9 == "O":
                    self.placeLabel.setText("You Lose!")
        if self.label2 == "O":
            if self.label5 == "O":
                if self.label8 == "O":
                    self.placeLabel.setText("You Lose!")
        if self.label3 == "O":
            if self.label6 == "O":
                if self.label9 == "O":
                    self.placeLabel.setText("You Lose!")
            if self.label5 == "O":
                if self.label7 == "O":
                    self.placeLabel.setText("You Lose!")
        if self.label4 == "O":
            if self.label5 == "O":
                if self.label6 == "O":
                    self.placeLabel.setText("You Lose!")
        if self.label7 == "O":
            if self.label8 == "O":
                if self.label9 == "O":
                    self.placeLabel.setText("You Lose!")