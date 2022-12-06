from player import HumanPlayer, ComputerPlayer
import time
class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.currentWinner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+ ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        numBoard = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in numBoard:
            print('| '+' | '.join(row)+ ' |')

    def avaiable_moves(self):
        moves=[]
        for(i,spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_index = square //3
        row = self.board[row_index*3: (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_index = square%3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square%2==0:
            dia1 = [self.board[i] for i in [0,4,8]]
            if all([spot==letter for spot in dia1]):
                return True
            dia2 = [self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in dia2]):
                return True
        return False
            


def play(game, x_player, o_player, print_board_game = True):
    if print_board_game:
        game.print_board_nums()
        
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_board_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.currentWinner:
                if print_board_game:
                    print(letter+ ' wins!')
            letter = 'O' if letter =='X' else 'X'
        time.sleep(0.5)
    if print_board_game:
        print('It\'s a tie!!')
    
if __name__ == '__main__':
    x_p = HumanPlayer('X')
    o_p = ComputerPlayer('O')
    t = TicTacToe()
    play(t,x_p,o_p, print_board_game=True)