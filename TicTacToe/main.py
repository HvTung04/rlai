from game import TicTacToe, play
from Player.human import HumanPlayer

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player)