from gui import *
import random


class TicTacToe:
    COMPUTER = 1
    PLAYER = 2

    def __init__(self, root):
        self._gui = TicTacToeGUI(self, root)
        self.new_game()

    def new_game(self):
        self._plays_first = None
        self._game_over = False
        self._move_number = 0
        self._player_last_move = None
        self._computer_last_move = None

        self._moves = [None for _ in range(9)]

        self._gui.display_who_plays_first_screen()

    def who_plays_first(self, option):
        self._plays_first = option
        self._gui.display_x_or_o_screen()

    def who_plays_what(self, option):
        if option == 0:
            self._computer_letter = "O"
            self._player_letter = "X"
        else:
            self._computer_letter = "X"
            self._player_letter = "O"

        self._gui.display_game_board()
        if self._plays_first == self.COMPUTER:
            computer_move = self._make_a_move()
            self._computer_last_move = computer_move
            self._moves[computer_move] = self._computer_letter
            self._move_number += 1
            self._gui.display_move(computer_move, self._computer_letter)

    def player_move(self, player_move):
        if self._game_over:
            return
        if self._moves[player_move]:
            return
        self._player_last_move = player_move
        self._moves[player_move] = self._player_letter
        self._move_number += 1
        if not self._is_game_over(player_move, self.PLAYER):
            self._gui.display_move(player_move, self._player_letter)
            computer_move = self._make_a_move()
            self._computer_last_move = computer_move
            self._moves[computer_move] = self._computer_letter
            self._move_number += 1
            if not self._is_game_over(computer_move, self.COMPUTER):
                self._gui.display_move(computer_move, self._computer_letter)

    def _is_game_over(self, move, who):
        if self._has_player_won():
            self._game_over = True
            self._gui.display_move(
                move, self._player_letter, True, self.PLAYER
            )
            return True
        elif self._has_computer_won():
            self._game_over = True
            self._gui.display_move(
                move, self._computer_letter, True, self.COMPUTER
            )
            return True
        elif self._move_number == 9:
            self._game_over = True
            if who == self.PLAYER:
                letter = self._player_letter
            else:
                letter = self._computer_letter
            self._gui.display_move(move, letter, True)
            return True
        else:
            return False

    def _has_player_won(self):
        return self._has_won(self._player_letter)

    def _has_computer_won(self):
        return self._has_won(self._computer_letter)

    def _has_won(self, letter):
        # Check Rows
        if self._moves[0] == self._moves[1] == self._moves[2] == letter:
            return True
        if self._moves[3] == self._moves[4] == self._moves[5] == letter:
            return True
        if self._moves[6] == self._moves[7] == self._moves[8] == letter:
            return True

        # Check Columns
        if self._moves[0] == self._moves[3] == self._moves[6] == letter:
            return True
        if self._moves[1] == self._moves[4] == self._moves[7] == letter:
            return True
        if self._moves[2] == self._moves[5] == self._moves[8] == letter:
            return True

        # Check Diagonals
        if self._moves[0] == self._moves[4] == self._moves[8] == letter:
            return True
        if self._moves[2] == self._moves[4] == self._moves[6] == letter:
            return True

        return False

    def _make_a_move(self):
        if self._move_number > 2:
            computer_move = self._is_computer_winning()
            if computer_move is not None:
                return computer_move

        computer_move = self._precaution()

        if computer_move is None:
            computer_move = self._game_on()

        return computer_move

    def _is_computer_winning(self):
        return self._is_winning(self.COMPUTER)

    def is_player_winning(self):
        return self._is_winning(self.PLAYER)

    def _is_winning(self, who):
        if who == self.PLAYER:
            letter = self._player_letter
        else:
            letter = self._computer_letter

        # Check Rows
        if not self._moves[0] and (self._moves[1] == self._moves[2] == letter):
            return 0
        if not self._moves[1] and (self._moves[0] == self._moves[2] == letter):
            return 1
        if not self._moves[2] and (self._moves[0] == self._moves[1] == letter):
            return 2
        if not self._moves[3] and (self._moves[4] == self._moves[5] == letter):
            return 3
        if not self._moves[4] and (self._moves[3] == self._moves[5] == letter):
            return 4
        if not self._moves[5] and (self._moves[3] == self._moves[4] == letter):
            return 5
        if not self._moves[6] and (self._moves[7] == self._moves[8] == letter):
            return 6
        if not self._moves[7] and (self._moves[6] == self._moves[8] == letter):
            return 7
        if not self._moves[8] and (self._moves[6] == self._moves[7] == letter):
            return 8

        # Check Columns
        if not self._moves[0] and (self._moves[3] == self._moves[6] == letter):
            return 0
        if not self._moves[3] and (self._moves[0] == self._moves[6] == letter):
            return 3
        if not self._moves[6] and (self._moves[0] == self._moves[3] == letter):
            return 6
        if not self._moves[1] and (self._moves[4] == self._moves[7] == letter):
            return 1
        if not self._moves[4] and (self._moves[1] == self._moves[7] == letter):
            return 4
        if not self._moves[7] and (self._moves[1] == self._moves[4] == letter):
            return 7
        if not self._moves[2] and (self._moves[5] == self._moves[8] == letter):
            return 2
        if not self._moves[5] and (self._moves[2] == self._moves[8] == letter):
            return 5
        if not self._moves[8] and (self._moves[2] == self._moves[5] == letter):
            return 8

        # Check Diagonals
        if not self._moves[0] and (self._moves[4] == self._moves[8] == letter):
            return 0
        if not self._moves[4] and (self._moves[0] == self._moves[8] == letter):
            return 4
        if not self._moves[8] and (self._moves[0] == self._moves[4] == letter):
            return 8
        if not self._moves[2] and (self._moves[4] == self._moves[6] == letter):
            return 2
        if not self._moves[4] and (self._moves[2] == self._moves[6] == letter):
            return 4
        if not self._moves[6] and (self._moves[2] == self._moves[4] == letter):
            return 6

        return

    def _precaution(self):
        if self._move_number == 0:
            computer_move = random.choice([0, 2, 6, 8, 4])
            return computer_move

        if self._move_number > 2:
            computer_move = self.is_player_winning()
            if computer_move is not None:
                return computer_move

        if self._move_number == 1:
            if self._player_last_move == 4:
                return random.choice([0, 2, 6, 8])
            else:
                return 4

        if self._move_number == 2:
            if self._computer_last_move == 0 and self._player_last_move in (
                1,
                3,
            ):
                return 4
            if self._computer_last_move == 2 and self._player_last_move in (
                1,
                5,
            ):
                return 4
            if self._computer_last_move == 6 and self._player_last_move in (
                3,
                7,
            ):
                return 4
            if self._computer_last_move == 8 and self._player_last_move in (
                5,
                7,
            ):
                return 4

            if self._player_last_move == 4 and self._computer_last_move in (
                0,
                2,
                6,
                8,
            ):
                if self._computer_last_move == 0:
                    return random.choice([1, 2, 3, 6])
                if self._computer_last_move == 2:
                    return random.choice([0, 1, 5, 8])
                if self._computer_last_move == 6:
                    return random.choice([0, 3, 7, 8])
                if self._computer_last_move == 8:
                    return random.choice([2, 5, 6, 7])

        if self._move_number == 3:
            if self._moves[
                4
            ] == self._player_letter and self._player_last_move in (
                0,
                2,
                6,
                8,
            ):
                if self._player_last_move == 0:
                    return random.choice([2, 6])
                if self._player_last_move == 2:
                    return random.choice([0, 8])
                if self._player_last_move == 6:
                    return random.choice([0, 8])
                if self._player_last_move == 8:
                    return random.choice([2, 6])

            if self._player_last_move in (0, 2, 6, 8):
                if self._player_last_move == 0:
                    return random.choice([1, 3])
                if self._player_last_move == 2:
                    return random.choice([1, 5])
                if self._player_last_move == 6:
                    return random.choice([3, 7])
                if self._player_last_move == 8:
                    return random.choice([5, 7])

        return

    def _game_on(self):
        possible_moves = []

        for x in range(0, 9):
            if self._moves[x] is None:
                possible_moves.append(x)

        return random.choice(possible_moves)


root = Tk()
tictactoe = TicTacToe(root)
root.mainloop()
