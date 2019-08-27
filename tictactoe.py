from gui import *
import random


class TicTacToe:
    def __init__(self, root):
        self.gui = TicTacToeGUI(self, root)
        self.newGame()

    def newGame(self):
        self.playsFirst = None
        self.gameOver = False
        self.moveNumber = 0
        self.won = 0
        self.playerLastMove = None

        self.moves = [None, None, None, None, None, None, None, None, None]

        self.gui.displayWhoPlaysFirstScreen()

    def whoPlaysFirst(self, option):
        self.playsFirst = option
        self.gui.displayXorOScreen()

    def whoPlaysWhat(self, option):
        if option == 0:
            self.computerLetter = "O"
            self.playerLetter = "X"
        else:
            self.computerLetter = "X"
            self.playerLetter = "O"

        self.gui.displayGameBoard()
        if self.playsFirst == 1:
            move = self.makeAMove()
            self.moves[move] = self.computerLetter
            self.moveNumber += 1
            self.gui.displayMove(move, self.computerLetter)

    def playerMove(self, playerMove):
        if self.gameOver:
            return
        self.playerLastMove = playerMove
        self.moves[playerMove] = self.playerLetter
        self.moveNumber += 1
        if not self.isGameOver(playerMove, 0):
            self.gui.displayMove(playerMove, self.playerLetter)
            computerMove = self.makeAMove()
            self.moves[computerMove] = self.computerLetter
            self.moveNumber += 1
            if not self.isGameOver(computerMove, 1):
                self.gui.displayMove(computerMove, self.computerLetter)

    def isGameOver(self, move, who):
        if self.hasPlayerWon():
            self.gameOver = True
            self.gui.displayMove(move, self.playerLetter, True, 2)
            return True
        elif self.hasComputerWon():
            self.gameOver = True
            self.gui.displayMove(move, self.computerLetter, True, 1)
            return True
        elif self.moveNumber == 9:
            self.gameOver = True
            if who == 0:
                letter = self.playerLetter
            else:
                letter = self.computerLetter
            self.gui.displayMove(move, letter, True, 0)
            return True
        else:
            return False

    def hasPlayerWon(self):
        return self.hasWon(self.playerLetter)

    def hasComputerWon(self):
        return self.hasWon(self.computerLetter)

    def hasWon(self, letter):
        # Check Rows
        if self.moves[0] == self.moves[1] == self.moves[2] == letter:
            return True
        if self.moves[3] == self.moves[4] == self.moves[5] == letter:
            return True
        if self.moves[6] == self.moves[7] == self.moves[8] == letter:
            return True

        # Check Columns
        if self.moves[0] == self.moves[3] == self.moves[6] == letter:
            return True
        if self.moves[1] == self.moves[4] == self.moves[7] == letter:
            return True
        if self.moves[2] == self.moves[5] == self.moves[8] == letter:
            return True

        # Check Diagonals
        if self.moves[0] == self.moves[4] == self.moves[8] == letter:
            return True
        if self.moves[2] == self.moves[4] == self.moves[6] == letter:
            return True

        return False

    def makeAMove(self):
        if self.moveNumber > 2:
            move = self.isWinning(1)
            if move:
                return move

        move = self.precaution()

        if not move:
            move = self.gameplan()

        return move

    def isWinning(self, who):
        if who == 0:
            letter = self.playerLetter
        else:
            letter = self.computerLetter

        # Check Rows
        if not self.moves[0] and (self.moves[1] == self.moves[2] == letter):
            return 0
        if not self.moves[1] and (self.moves[0] == self.moves[2] == letter):
            return 1
        if not self.moves[2] and (self.moves[0] == self.moves[1] == letter):
            return 2
        if not self.moves[3] and (self.moves[4] == self.moves[5] == letter):
            return 3
        if not self.moves[4] and (self.moves[3] == self.moves[5] == letter):
            return 4
        if not self.moves[5] and (self.moves[3] == self.moves[4] == letter):
            return 5
        if not self.moves[6] and (self.moves[7] == self.moves[8] == letter):
            return 6
        if not self.moves[7] and (self.moves[6] == self.moves[8] == letter):
            return 7
        if not self.moves[8] and (self.moves[6] == self.moves[7] == letter):
            return 8

        # Check Columns
        if not self.moves[0] and (self.moves[3] == self.moves[6] == letter):
            return 0
        if not self.moves[3] and (self.moves[0] == self.moves[6] == letter):
            return 3
        if not self.moves[6] and (self.moves[0] == self.moves[3] == letter):
            return 6
        if not self.moves[1] and (self.moves[4] == self.moves[7] == letter):
            return 1
        if not self.moves[4] and (self.moves[1] == self.moves[7] == letter):
            return 4
        if not self.moves[7] and (self.moves[1] == self.moves[4] == letter):
            return 7
        if not self.moves[2] and (self.moves[5] == self.moves[8] == letter):
            return 2
        if not self.moves[5] and (self.moves[2] == self.moves[8] == letter):
            return 5
        if not self.moves[8] and (self.moves[2] == self.moves[5] == letter):
            return 8

        # Check Diagonals
        if not self.moves[0] and (self.moves[4] == self.moves[8] == letter):
            return 0
        if not self.moves[4] and (self.moves[0] == self.moves[8] == letter):
            return 4
        if not self.moves[8] and (self.moves[0] == self.moves[4] == letter):
            return 8
        if not self.moves[2] and (self.moves[4] == self.moves[6] == letter):
            return 2
        if not self.moves[4] and (self.moves[2] == self.moves[6] == letter):
            return 4
        if not self.moves[6] and (self.moves[2] == self.moves[4] == letter):
            return 6

        return None

    def precaution(self):
        if self.moveNumber == 0:
            move = random.choice([0, 2, 6, 8, 4])

        if self.moveNumber > 2:
            move = self.isWinning(0)
            if move:
                return move

        if self.moveNumber == 1:
            if self.playerLastMove in (0, 2, 6, 8):
                return 4
            elif self.playerLastMove == 4:
                return random.choice([0, 2, 6, 8])

        if self.moveNumber == 3:
            return random.choice([1, 5, 7, 3])

        return False

    def gameplan(self):
        possibleMoves = [1] * (9 - self.moveNumber)
        n = 0
        for x in range(0, 9):
            if not self.moves[x]:
                possibleMoves[n] = x
                n += 1
        return random.choice(possibleMoves)


root = Tk()
tictactoe = TicTacToe(root)
root.mainloop()