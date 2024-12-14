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
        self.__humanWins = 0
        self.__computerWins = 0
        super().__init__()
        self.takesettings()
        self.setupUi(self)
        self.replayButton.hide()
        if self.__first == 1:
            self.humanmove()
        elif self.__first == 2:
            self.computermove()
        self.submitButton.clicked.connect( lambda : self.humanmove())
        self.replayButton.clicked.connect( lambda : self.resetboard())

    def takesettings(self) -> None:
        """
        Method to retrieve settings
        """
        file = open("data.txt", "r")
        content = file.readlines() # https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
        self.__difficulty = content[0]
        self.__first = content[1]
        file.close()

    def resetboard(self):
        self.__chosen = []
        self.replayButton.hide()
        self.submitButton.show()

    def computermove(self) -> None:
        """
        Method to place computers O
        """
        print("start computer move")
        move = None
        if self.__difficulty == 1:
            move = 1#random.choice([1,2,3,4,5,6,7,8,9])
            #while move in self.__chosen:
                #move = random.choice([1,2,3,4,5,6,7,8,9])
        elif self.__difficulty == 2:
            pass
        elif self.__difficulty == 3:
            pass
        elif self.__difficulty == 4:
            pass
        print("place computer move")
        if move == 1:
            self.spot1.hide()
            self.label1.setText("O")
            self.__chosen.append(1)
        elif move == 2:
            self.spot2.hide()
            self.label2.setText("O")
            self.__chosen.append(2)
        elif move == 3:
            self.spot2.hide()
            self.label3.setText("O")
            self.__chosen.append(3)
        elif move == 4:
            self.spot4.hide()
            self.label4.setText("O")
            self.__chosen.append(4)
        elif move == 5:
            self.spot5.hide()
            self.label5.setText("O")
            self.__chosen.append(5)
        elif move == 6:
            self.spot6.hide()
            self.label6.setText("O")
            self.__chosen.append(6)
        elif move == 7:
            self.spot7.hide()
            self.label7.setText("O")
            self.__chosen.append(7)
        elif move == 8:
            self.spot8.hide()
            self.label8.setText("O")
            self.__chosen.append(8)
        elif move == 9:
            self.spot9.hide()
            self.label9.setText("O")
            self.__chosen.append(9)
        print("end computer move")
        self.wincheck(2)

    def winscreen(self, winner):
        self.submitButton.hide()
        self.replayButton.show()
        if winner == 1:
            self.__humanWins += 1
        elif winner == 2:
            self.__computerWins += 1
        self.humanWinLabel.setText(f"Human Wins: {self.__humanWins}")
        self.computerWinLabel.setText(f"Computer Wins: {self.__computerWins}")

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
        print("wincheck reached")
        print(player)
        if player == "1":
            if self.label1.text() == "X":
                if self.label2.text() == "X":
                    if self.label3.text() == "X":
                        self.placeLabel.setText("You Win!")
                if self.label4.text() == "X":
                    if self.label7.text() == "X":
                        self.placeLabel.setText("You Win!")
                if self.label5.text() == "X":
                    if self.label9.text() == "X":
                        self.placeLabel.setText("You Win!")
            if self.label2.text() == "X":
                if self.label5.text() == "X":
                    if self.label8.text() == "X":
                        self.placeLabel.setText("You Win!")
            if self.label3.text() == "X":
                if self.label6.text() == "X":
                    if self.label9.text() == "X":
                        self.placeLabel.setText("You Win!")
                if self.label5.text() == "X":
                    if self.label7.text() == "X":
                        self.placeLabel.setText("You Win!")
            if self.label4.text() == "X":
                if self.label5.text() == "X":
                    if self.label6.text() == "X":
                        self.placeLabel.setText("You Win!")
            if self.label7.text() == "X":
                if self.label8.text() == "X":
                    if self.label9.text() == "X":
                        self.placeLabel.setText("You Win!")
        print("test%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        #if self.placeLabel.text() == "You Win!": # PROBLEM CHILD ****************************************************************************************************************************
            #self.winscreen(1)
        #else:
            #self.computermove()
        print("computer wincheck time **********")
        if player == "2":
            if self.label1.text() == "O":
                if self.label2.text() == "O":
                    if self.label3.text() == "O":
                        self.placeLabel.setText("You Lose!")
                if self.label4.text() == "O":
                    if self.label7.text() == "O":
                        self.placeLabel.setText("You Lose!")
                if self.label5.text() == "O":
                    if self.label9.text() == "O":
                        self.placeLabel.setText("You Lose!")
            if self.label2.text() == "O":
                if self.label5.text() == "O":
                    if self.label8.text() == "O":
                        self.placeLabel.setText("You Lose!")
            if self.label3.text() == "O":
                if self.label6.text() == "O":
                    if self.label9.text() == "O":
                        self.placeLabel.setText("You Lose!")
                if self.label5.text() == "O":
                    if self.label7.text() == "O":
                        self.placeLabel.setText("You Lose!")
            if self.label4.text() == "O":
                if self.label5.text() == "O":
                    if self.label6.text() == "O":
                        self.placeLabel.setText("You Lose!")
            if self.label7.text() == "O":
                if self.label8.text() == "O":
                    if self.label9.text() == "O":
                        self.placeLabel.setText("You Lose!")
        print("wincheck finished")
        if self.placeLabel.text() == "You Lose!":
            self.winscreen(2)
        else:
            #self.humanmove()
            print("human move time")
            exit()