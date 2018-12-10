from ad_controller import mainController

from PyQt5.QtWidgets import QApplication, QWidget

def gameMain(app):
    game = mainController()
    game.startGame(app)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    gameMain(app)