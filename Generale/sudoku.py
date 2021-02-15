import os

__author__ = "https://github.com/nicholas-progetti-scuola un ringraziamento a https://www.youtube.com/watch?v=lK4N8E6uNr4 per il codice di ricerca"

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

print("inserisci tutti i numeri 0 per numero ignoto verranno inseriti riga  per riga (------------)")


def inserire():
    global board
    for riga in range(9):
        while True:
            try:
                numeri=input("dammi i numeri separati da uno spazio per i caratteri vuoti digitare 0 della riga  " + str(riga+1) + "| ").split()
                for numero in range(9):
                    if int(numeri[numero])!=0:
                        board[riga].pop(numero)
                        board[riga].insert(numero,int(numeri[numero]))
                break
                
            except Exception as e:
                print("si è verificato un errore di " + str(e) + " reinserire riga")
        
        
        
        


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

  
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  #9 9 9 9 9 9 9 9 9 

    return None


while True:
    inserire()
    print_board(board)
    conferma=input("tabella confermata y/n")
    if conferma.lower()=="y":
        os.system("cls")
        break
    else:
        os.system("cls")
        board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

print_board(board)
solve(board)
print("__________risolto____________")
print_board(board)

input()
