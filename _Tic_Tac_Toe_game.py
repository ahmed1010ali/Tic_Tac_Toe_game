#!/usr/bin/env python
# coding: utf-8

# In[ ]:


game_board = [['', '', ''],
              ['', '', ''],
              ['', '', '']]
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)
def get_player_move(board, player_symbol):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '':
                board[row][col] = player_symbol
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers.")
def check_win(board, player_symbol):
    for row in board:
        if all(square == player_symbol for square in row):
            return True

    for col in range(3):
        if all(board[row][col] == player_symbol for row in range(3)):
            return True

    if all(board[i][i] == player_symbol for i in range(3)) or all(board[i][2-i] == player_symbol for i in range(3)):
        return True

    return False
def check_tie(board):
    for row in board:
        if '' in row:
            return False
    return True
def main():
    player_turn = 'X'

    while True:
        print_board(game_board)
        get_player_move(game_board, player_turn)
        
        if check_win(game_board, player_turn):
            print_board(game_board)
            print(f"Player {player_turn} wins!")
            break
        
        if check_tie(game_board):
            print_board(game_board)
            print("It's a tie!")
            break
        
        player_turn = 'O' if player_turn == 'X' else 'X'

if __name__ == "__main__":
    main()


# In[ ]:




