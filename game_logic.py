from PyQt6.QtWidgets import *
from gamestart import *
from gameboard import *
import random

class GameStart(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        """
        Method to set up UI.
        """
        super().__init__()
        self.setupUi(self)
        self.game = None
        self.diff = 0
        self.first = 0
        print("1")
        self.startGameButton.clicked.connect(lambda : self.startgame())

    def startgame(self) -> None:
        """
        Method to start game with selected settings.
        """
        self.storesettings()
        self.game = GameBoard() # https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/ to create a second window
        self.game.show()


    def storesettings(self) -> None:
        """
        Method to write settings
        """
        if self.difficultyButton1.isChecked():
            self.diff = 1
        elif self.difficultyButton2.isChecked():
            self.diff = 2
        elif self.difficultyButton3.isChecked():
            self.diff = 3
        elif self.difficultyButton4.isChecked():
            self.diff = 4
        else:
            self.diff = 1
        if self.firstButton2.isChecked():
            self.first = 1
        elif self.firstButton3.isChecked():
            self.first = 2
        else:
            self.first = random.choice([1, 2])  # https://www.geeksforgeeks.org/random-numbers-in-python/
        file = open("data.txt", "w")
        file.write(str(self.diff) + "\n")
        if self.diff == 4:
            self.first = 2
        file.write(str(self.first))
        file.close()


class GameBoard(QMainWindow, Ui_gameBoard):

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
        if self.__first == 1:
            self.humanmove()
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
        self.wincheck(2)

    def winscreen(self, winner):
        if winner == 1:
            pass

    def humanmove(self) -> None:
        """
        Method to submit human move
        """
        if self.spot1.isChecked():
            self.spot1.hide()
            self.label1.setText("X")
            self.__chosen.append(1)
        elif self.spot2.isChecked():
            self.spot2.hide()
            self.label2.setText("X")
            self.__chosen.append(2)
        elif self.spot3.isChecked():
            self.spot3.hide()
            self.label3.setText("X")
            self.__chosen.append(3)
        elif self.spot4.isChecked():
            self.spot4.hide()
            self.label4.setText("X")
            self.__chosen.append(4)
        elif self.spot5.isChecked():
            self.spot5.hide()
            self.label5.setText("X")
            self.__chosen.append(5)
        elif self.spot6.isChecked():
            self.spot6.hide()
            self.label6.setText("X")
            self.__chosen.append(6)
        elif self.spot7.isChecked():
            self.spot7.hide()
            self.label7.setText("X")
            self.__chosen.append(7)
        elif self.spot8.isChecked():
            self.spot8.hide()
            self.label8.setText("X")
            self.__chosen.append(8)
        elif self.spot9.isChecked():
            self.spot9.hide()
            self.label9.setText("X")
            self.__chosen.append(9)
        self.wincheck(1)

    def wincheck(self, player) -> None:
        """
        Method to check if a move wins.
        """
        if player == 1:
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
        if self.placeLabel.text() == "You Win!":
            self.winscreen(1)
        else:
            self.computermove()
        if player == 2:
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
        if self.placeLabel.text() == "You Lose!":
            self.winscreen(2)
        else:
            self.humanmove()