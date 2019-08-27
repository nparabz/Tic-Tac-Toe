from gui import *


class TicTacToe:

    whoPlaysFirst = None
    isGameOver = False
    moveNumber = 0

    def __init__(self, root):
        self.moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        self.gui = TicTacToeGUI(self, root)
        self.gui.displayWhoPlaysFirstScreen()

    def whoPlaysFirst(self, option):
        self.whoPlaysFirst = option
        self.gui.displayXorOScreen()

    def whoPlaysWhat(self, option):
        if option == 0:
            self.computerLetter = "O"
            self.playerLetter = "X"
        else:
            self.computerLetter = "X"
            self.playerLetter = "O"

        if self.whoPlaysFirst == 0:
            self.gui.displayGameBoard(self.moves)
        elif self.whoPlaysFirst == 1:
            self.makeAMove()

    def userMove(self, position):
        self.moves[position] = self.playerLetter
        self.moveNumber += 1
        if not self.isGameOver():
            self.makeAMove()
        self.gui.displayGameBoard(self.moves)

    def isGameOver(self):
        if self.hasUserWon():
            return True
        elif self.hasComputerWon():
            return True
        elif self.moveNumber == 9:
            return True
        else:
            return False

    def makeAMove(self):
        self.goForWin()
        self.precaution()
        self.gameplan()

    def goForWin(self):
        return

    def precaution(self):
        return

    def gameplan(self):
        return


root = Tk()
tictactoe = TicTacToe(root)
root.mainloop()
