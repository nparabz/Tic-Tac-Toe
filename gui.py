from tkinter import *


class TicTacToeGUI:
    def __init__(self, tictactoe, root):
        self.tictactoe = tictactoe
        self.root = root

    def displayWhoPlaysFirstScreen(self):
        self.whoPlaysFirstFrame = Frame(self.root)
        self.whoPlaysFirstFrame.grid(row=0)

        Label(self.whoPlaysFirstFrame, text="Tic-Tac-Toe", font="bold 24").grid(
            row=0, columnspan=2
        )

        Label(self.whoPlaysFirstFrame, text="Do you want to play first?").grid(
            row=1, columnspan=2
        )

        Button(self.whoPlaysFirstFrame, text="Yes", command=self.playerPlaysFirst).grid(
            row=2, column=0
        )

        Button(
            self.whoPlaysFirstFrame,
            text="No, let computer play first",
            command=self.computerPlaysFirst,
        ).grid(row=2, column=1)

    def playerPlaysFirst(self):
        self.whoPlaysFirstFrame.grid_forget()
        self.whoPlaysFirstFrame.destroy()
        self.tictactoe.whoPlaysFirst(0)

    def computerPlaysFirst(self):
        self.whoPlaysFirstFrame.grid_forget()
        self.whoPlaysFirstFrame.destroy()
        self.tictactoe.whoPlaysFirst(1)

    def displayXorOScreen(self):
        self.whoPlaysWhatFrame = Frame(self.root)
        self.whoPlaysWhatFrame.grid(row=0)

        Label(self.whoPlaysWhatFrame, text="Tic-Tac-Toe", font="bold 24").grid(
            row=0, columnspan=2
        )

        Label(self.whoPlaysWhatFrame, text="Do you want to play X or O?").grid(
            row=1, columnspan=2
        )

        Button(self.whoPlaysWhatFrame, text="X", command=self.playerPlaysX).grid(
            row=2, column=0
        )
        Button(self.whoPlaysWhatFrame, text="O", command=self.playerPlaysO).grid(
            row=2, column=1
        )

    def playerPlaysX(self):
        self.whoPlaysWhatFrame.grid_forget()
        self.whoPlaysWhatFrame.destroy()
        self.tictactoe.whoPlaysWhat(0)

    def playerPlaysO(self):
        self.whoPlaysWhatFrame.grid_forget()
        self.whoPlaysWhatFrame.destroy()
        self.tictactoe.whoPlaysWhat(1)

    def displayGameBoard(self):

        self.movesLetters = [
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
        ]
        self.subtextString = StringVar()

        self.movesLabels = [None, None, None, None, None, None, None, None, None]

        self.gameBoardFrame = Frame(self.root)
        self.gameBoardFrame.grid(row=0)

        Label(self.gameBoardFrame, text="Tic-Tac-Toe", font="bold 24").grid(
            row=0, columnspan=3
        )

        for x in range(0, 9):
            self.movesLabels[x] = Label(
                self.gameBoardFrame,
                textvariable=self.movesLetters[x],
                font="bold 16",
                bg="#DDDDDD",
                width=4,
                height=2,
            )
            self.movesLabels[x].grid(row=(x // 3) + 1, column=x % 3, padx=4, pady=3)
            self.movesLabels[x].bind("<Button-1>", self.playerMove)

        self.subtextLabel = Label(
            self.gameBoardFrame, textvariable=self.subtextString
        ).grid(row=4, columnspan=3)

        self.subtextString.set("Game in Progress...")

        return

    def displayMove(self, move, letter, isGameOver=False, whoWon=0):
        self.movesLetters[move].set(letter)

        if isGameOver:
            if whoWon == 2:
                self.subtextString.set("Game Over! You Win! Well Played!")
            elif whoWon == 1:
                self.subtextString.set("Game Over! You Lose!")
            else:
                self.subtextString.set("Game Over! Draw! Well Played!")

            self.newGameButtonFrame = Frame(self.gameBoardFrame)
            self.newGameButton = Button(
                self.newGameButtonFrame, text="New Game", command=self.newGame
            ).grid(row=0)
            self.newGameButtonFrame.grid(row=5, columnspan=3)

        return

    def newGame(self):
        self.gameBoardFrame.grid_forget()
        self.gameBoardFrame.destroy()
        self.tictactoe.newGame()
        return

    def playerMove(self, event):
        for x in range(0, 9):
            if event.widget == self.movesLabels[x]:
                self.tictactoe.playerMove(x)
        return
