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

    def displayGameBoard(
        self, moves, isGameOver=False, computerWon=False, playerWon=False
    ):
        self.movesLabels = [None, None, None, None, None, None, None, None, None]

        self.gameBoardFrame = Frame(self.root)
        self.gameBoardFrame.grid(row=0)

        Label(self.gameBoardFrame, text="Tic-Tac-Toe", font="bold 24").grid(
            row=0, columnspan=3
        )

        for x in range(0, 9):
            self.movesLabels[x] = Label(
                self.gameBoardFrame,
                text=moves[x],
                font="bold 16",
                bg="#DDDDDD",
                width=4,
                height=2,
            )
            self.movesLabels[x].grid(row=(x // 3) + 1, column=x % 3, padx=4, pady=3)
            if moves[x] == " ":
                self.movesLabels[x].bind("<Button-1>", self.userMove)

        if isGameOver:
            if playerWon:
                message = "Game Over! You Win! Well Played!"
            elif computerWon:
                message = "Game Over! You Lose!"
            else:
                message = "Game Over! Draw! Well Played!"
        else:
            message = "Game in Progress..."

        self.subtextLabel = Label(self.gameBoardFrame, text=message).grid(
            row=4, columnspan=3
        )

        return

    def userMove(self, event):
        for x in range(0, 9):
            if event.widget == self.movesLabels[x]:
                self.tictactoe.userMove(x)
        return
