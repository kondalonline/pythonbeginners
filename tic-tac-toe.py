
class TicTacToe():
    theBoard = {'a1': ' ', 'a2': ' ', 'a3': ' ',
                'b1': ' ', 'b2': ' ', 'b3': ' ',
                'c1': ' ', 'c2': ' ', 'c3': ' '}

    def printBoard(board):
        print(board['a1'] + '|' + board['a2'] + '|' + board['a3'])
        print('-+-+-')
        print(board['b1'] + '|' + board['b2'] + '|' + board['b3'])
        print('-+-+-')
        print(board['c1'] + '|' + board['c2'] + '|' + board['c3'])


    def playthegame():
        turn = 'X'
        for i in range(9):
            printBoard(theBoard)
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            theBoard[move] = turn
            turn = 'O' if turn == 'X' else 'X'


if __name__ == '__main__':
    playthegame
    printBoard(theBoard)