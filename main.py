from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TicTacToe(GridLayout):
    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        self.cols = 3
        self.buttons = [[Button() for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].bind(on_press=self.on_button_press)
                self.add_widget(self.buttons[row][col])

        self.restart_button = Button(text="Restart Game", on_press=self.restart_game)
        self.add_widget(Label())  # Empty space for layout
        self.add_widget(self.restart_button)

        self.reset_game()

    def reset_game(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.update_board()

    def on_button_press(self, instance):
        row, col = self.get_button_position(instance)
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            self.update_board()
            winner = self.check_winner()
            if winner:
                self.display_winner(winner)
            else:
                self.switch_player()

    def get_button_position(self, button):
        for row in range(3):
            if button in self.buttons[row]:
                return row, self.buttons[row].index(button)

    def update_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].text = self.board[row][col]

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for row in self.board:
            if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
                return row[0]

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == 'X' for row in range(3)) or all(self.board[row][col] == 'O' for row in range(3)):
                return self.board[0][col]

        # Check diagonals
        if all(self.board[i][i] == 'X' for i in range(3)) or all(self.board[i][2 - i] == 'O' for i in range(3)):
            return self.board[0][0]

        return None

    def display_winner(self, winner):
        self.restart_button.text = f"{winner} Wins! Click to Play Again."

    def restart_game(self, instance):
        self.reset_game()
        self.restart_button.text = "Restart Game"

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()

if __name__ == '__main__':
    TicTacToeApp().run()
