from game_logic import *  # import statement needed to gain access to the television file


def main():
    application = QApplication([])
    window = GameStart()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()