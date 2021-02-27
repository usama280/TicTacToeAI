from Player import HumanPlayer, RandomComputerPlayer, AIPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = [i for (i,spot) in enumerate(self.board) if spot == ' ']
        '''
        for (i,spot) in enumerate(self.board):
            #[x, x, o] --> [(0,x), (1,x), (2,o)]
            if spot == ' ':
                moves.append(i)
        '''
        return moves

    def empty(self):
        return ' ' in self.board

    def num_of_empty(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    def winner(self, square, letter):
        row_ind = square//3 #divides and rounds down
        row = self.board[row_ind*3:(row_ind+1)*3]

        if all([letter == spot for spot in row]):
            return True
        

        col_ind = square%3 
        col = [self.board[col_ind+i*3] for i in range(3)]

        if all([letter == spot for spot in col]):
            return True
        
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
           
            if all([letter == spot for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2,4,6]]
        
            if all([letter == spot for spot in diagonal2]):
                return True
        
        return False



def play(game, x, o, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty():
        if letter == 'O':
            square = o.get_move(game)
        else:
            square = x.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                game.print_board()
                print('')

            if game.current_winner:
                print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    print('Its a tie')




x = HumanPlayer('X')
#o = RandomComputerPlayer('O')  Play agaisnt AI or change to randomCompPlayer
o = AIPlayer('O')
t = TicTacToe()

play(t, x, o, print_game = True)