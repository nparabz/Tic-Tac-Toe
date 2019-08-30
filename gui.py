from tkinter import *


class TicTacToeGUI:
    def __init__(self, tictactoe, root):
        self._tictactoe = tictactoe
        self._root = root

    def display_who_plays_first_screen(self):
        self._who_plays_first_frame = Frame(self._root)
        self._who_plays_first_frame.grid(row=0)

        Label(
            self._who_plays_first_frame, text="Tic-Tac-Toe", font="bold 24"
        ).grid(row=0, columnspan=2)

        Label(
            self._who_plays_first_frame, text="Do you want to play first?"
        ).grid(row=1, columnspan=2)

        Button(
            self._who_plays_first_frame,
            text="Yes",
            command=self._player_plays_first,
        ).grid(row=2, column=0)

        Button(
            self._who_plays_first_frame,
            text="No, let computer play first",
            command=self._computer_plays_first,
        ).grid(row=2, column=1)

    def _player_plays_first(self):
        self._who_plays_first_frame.grid_forget()
        self._who_plays_first_frame.destroy()
        self._tictactoe.who_plays_first(self._tictactoe.PLAYER)

    def _computer_plays_first(self):
        self._who_plays_first_frame.grid_forget()
        self._who_plays_first_frame.destroy()
        self._tictactoe.who_plays_first(self._tictactoe.COMPUTER)

    def display_x_or_o_screen(self):
        self._who_plays_what_frame = Frame(self._root)
        self._who_plays_what_frame.grid(row=0)

        Label(
            self._who_plays_what_frame, text="Tic-Tac-Toe", font="bold 24"
        ).grid(row=0, columnspan=2)

        Label(
            self._who_plays_what_frame, text="Do you want to play X or O?"
        ).grid(row=1, columnspan=2)

        Button(
            self._who_plays_what_frame, text="X", command=self._player_plays_x
        ).grid(row=2, column=0)
        Button(
            self._who_plays_what_frame, text="O", command=self._player_plays_o
        ).grid(row=2, column=1)

    def _player_plays_x(self):
        self._who_plays_what_frame.grid_forget()
        self._who_plays_what_frame.destroy()
        self._tictactoe.who_plays_what(0)

    def _player_plays_o(self):
        self._who_plays_what_frame.grid_forget()
        self._who_plays_what_frame.destroy()
        self._tictactoe.who_plays_what(1)

    def display_game_board(self):

        self._moves_letters = [StringVar() for _ in range(9)]
        self._subtext_string = StringVar()

        self._moves_labels = [None for _ in range(9)]

        self._game_board_frame = Frame(self._root)
        self._game_board_frame.grid(row=0)

        Label(self._game_board_frame, text="Tic-Tac-Toe", font="bold 24").grid(
            row=0, columnspan=3
        )

        for x in range(0, 9):
            self._moves_labels[x] = Label(
                self._game_board_frame,
                textvariable=self._moves_letters[x],
                font="bold 16",
                bg="#DDDDDD",
                width=4,
                height=2,
            )
            self._moves_labels[x].grid(
                row=(x // 3) + 1, column=x % 3, padx=4, pady=3
            )
            self._moves_labels[x].bind("<Button-1>", self._player_move)

        self.subtext_label = Label(
            self._game_board_frame, textvariable=self._subtext_string
        ).grid(row=4, columnspan=3)

        self._subtext_string.set("Game in Progress...")

        return

    def display_move(self, move, letter, is_game_over=False, who_won=0):
        self._moves_letters[move].set(letter)

        if is_game_over:
            if who_won == self._tictactoe.PLAYER:
                self._subtext_string.set("Game Over! You Win! Well Played!")
            elif who_won == self._tictactoe.COMPUTER:
                self._subtext_string.set("Game Over! You Lose!")
            else:
                self._subtext_string.set("Game Over! Draw! Well Played!")

            self._new_game_button_frame = Frame(self._game_board_frame)
            self._new_game_button = Button(
                self._new_game_button_frame,
                text="New Game",
                command=self._new_game,
            ).grid(row=0)
            self._new_game_button_frame.grid(row=5, columnspan=3)

        return

    def _new_game(self):
        self._game_board_frame.grid_forget()
        self._game_board_frame.destroy()
        self._tictactoe.new_game()
        return

    def _player_move(self, event):
        for x in range(0, 9):
            if event.widget == self._moves_labels[x]:
                self._tictactoe.player_move(x)
        return
