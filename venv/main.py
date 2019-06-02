import collections
import string

# Global Variables
t = (('row0', ['', '', '', '', '']),
     ('row1', [1, '-', 4, '-', 7]),
     ('row2', [2, '-', 5, '-', 8]),
     ('row3', [3, '-', 6, '-', 9]))
d = collections.OrderedDict(t)
d_items = list(d.items())
player = ''
winner = False

# Display board
def interface():
    values_list = []
    for i in range(len(d_items)):
        values_list.append(d_items[i][1])
    values_list_length = len(values_list)
    single_list_length = len(values_list[0])
    for i in range(0, single_list_length):
        for j in range(0, values_list_length):
            print(values_list[j][i], '', end='|')
        print()

def modify(player):
    cell = int(input('Insert where to place marker'))
    if player == 'x':
        turn = 'X'
    else:
        turn = '0'
    if cell in range(1,10) and 1 == cell and (t[1][1][0]) == 1 :
        t[1][1][0] = turn
        interface()
    elif cell in range(1,10) and 2 == cell and (t[2][1][0]) == 2:
        t[2][1][0] = turn
        interface()
    elif cell in range(1,10) and 3 == cell and (t[3][1][0]) == 3:
        t[3][1][0] = turn
        interface()
    elif cell in range(1,10) and 4 == cell and (t[1][1][2]) == 4:
        t[1][1][2] = turn
        interface()
    elif cell in range(1,10) and 5 == cell and (t[2][1][2]) == 5 :
        t[2][1][2] = turn
        interface()
    elif cell in range(1,10) and 6 == cell and (t[3][1][2]) == 6:
        t[3][1][2] = turn
        interface()
    elif cell in range(1,10) and 7 == cell and (t[1][1][4]) == 7 :
        t[1][1][4] = turn
        interface()
    elif cell in range(1,10) and 8 == cell and (t[2][1][4]) == 8 :
        t[2][1][4] = turn
        interface()
    elif cell in range(1,10) and 9 == cell and (t[3][1][4]) == 9:
        t[3][1][4] = turn
        interface()
    else:
        print('Game rules violation!!! \n You lose your turn!')
        interface()

def selectp():
    global player
    player = input('Insert desired player X or 0')
    if player not in list(string.printable) or player.lower() == 'x' or player == '0':
        inside_selectp()
    else:
        print('Not a valid player selected, please select again.')
        selectp()

def inside_selectp():
        interface()
        if player.lower() == 'x':
            for i in range(1,10):
                if i % 2 != 0:
                    p = 'x'
                else:
                    p = '0'
                winner(t)
                if winner == False:
                    continue
                if winner == True:
                    if i % 2 != 0:
                        p = '0'
                    else:
                        p = 'x'
                    print(f'Player {p.capitalize()} has won!!' )
                    interface()
                    break
                print( f'Player {p.capitalize()} turn' )
                i += 1
                modify(p)
            print('Game Over!')
        else:
            for i in range(1, 10):
                if i % 2 != 0:
                    p = '0'
                else:
                    p = 'x'
                winner( t )
                if winner == False:
                    continue
                if winner == True:
                    if i % 2 != 0:
                        p = 'x'
                    else:
                        p = '0'
                    print( f'Player {p.capitalize()} has won!!' )
                    interface()
                    break
                print( f'Player {p.capitalize()} turn' )
                i += 1
                modify(p)
            print( 'Game Over!' )

def winner(t):
    """This function checks if the condition of a player being a winner is valid or not"""
    global winner
    #Vertical check
    if (t[1][1][0]) == (t[1][1][2]) == (t[1][1][4]):
        (t[1][1][0]), (t[1][1][2]), (t[1][1][4]) = ['W','I','N']
        winner = True
    elif (t[2][1][0]) == (t[2][1][2]) == (t[2][1][4]):
        (t[2][1][0]), (t[2][1][2]), (t[2][1][4]) = ['W','I','N']
        winner = True
    elif (t[3][1][0]) == (t[3][1][2]) == (t[3][1][4]):
        (t[3][1][0]),(t[3][1][2]),(t[3][1][4]) = ['W','I','N']
        winner = True
    #Cross check
    elif (t[1][1][0]) == (t[2][1][2]) == (t[3][1][4]):
        (t[1][1][0]),(t[2][1][2]),(t[3][1][4]) = ['W','I','N']
        winner = True
    elif (t[1][1][4]) == (t[2][1][2]) == (t[3][1][0]):
        (t[1][1][4]),(t[2][1][2]),(t[3][1][0]) = ['W','I','N']
        winner = True
    #Horizontal check
    elif (t[1][1][0]) == (t[2][1][0]) == (t[3][1][0]):
        (t[1][1][0]),(t[2][1][0]),(t[3][1][0]) = ['W','I','N']
        winner = True
    elif (t[1][1][2]) == (t[2][1][2]) == (t[3][1][2]):
        (t[1][1][2]),(t[2][1][2]),(t[3][1][2]) = ['W','I','N']
        winner = True
    elif (t[1][1][4]) == (t[2][1][4]) == (t[3][1][4]):
        (t[1][1][4]),(t[2][1][4]),(t[3][1][4]) = ['W','I','N']
        winner = True
    else:
        pass

#Auto Start Game
def gamestart():
    selectp()
gamestart()