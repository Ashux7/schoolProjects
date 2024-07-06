import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
import pandas as pd
g=pd.read_csv("Project_urooj.csv")
#print(g)
sign = 0
global board
board = [[" " for x in range(3)] for y in range(3)]
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        box = messagebox.showinfo("Winner", name1.get() + " won the match")
        g.loc[len(g),:]=[name1.get(),name2.get(),name1.get() + " won the match"]
        g.to_csv("Project_urooj.csv",index=False)
        print(g)
        gb.destroy()

    elif winner(board, "O"):
        box = messagebox.showinfo("Winner", name2.get()+ " won the match")
        g.loc[len(g), :] = [name1.get(), name2.get(), name2.get() + " won the match"]
        g.to_csv("Project_urooj.csv",index=False)
        print(g)
        gb.destroy()

    elif (isfull()):
        box = messagebox.showinfo("Tie Game", "Tie Game")
        g.loc[len(g), :] = [name1.get(), name2.get(),"Tie Game" ]
        g.to_csv("Project_urooj.csv",index=False)
        print(g)
        gb.destroy()

def isfree(i, j):
    return board[i][j] == " "
def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag

def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()

def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):

        x = False
        box = messagebox.showinfo("Winner",  name1.get() + " won the match")
        g.loc[len(g.index)] = {'Player1':name1.get(), 'Player2':'Computer','Result':"{} won the match".format(name1.get()) }  # type: ignore
        g.to_csv("Project_urooj.csv",index=False)
        print(g)
        gb.destroy()

    elif winner(board, "O"):

        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
        g.loc[len(g.index)] = {'Player1':name1.get(), 'Player2':'Computer','Result':"Computer won the match" }  # type: ignore
        g.to_csv("Project_urooj.csv",index=False)
        print(g)
        gb.destroy()

    elif (isfull()):

        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
        g.loc[len(g.index)] = {'Player1':name1.get(), 'Player2':'Computer','Result':"Tie Game" }  # type: ignore
        g.to_csv("Project_urooj.csv",index=False)
        print(g)
        gb.destroy()

    if (x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
def withpc(game_board):
    game_board.destroy()
    global h
    h=Tk()
    h.geometry('250x250')
    h.title("Details")
    n1= Label(h, text="ENTER PLAYER NAME", width=20, font=('arial', 12))
    n1.place(x=20, y=100)
    global name1
    name1= StringVar()
    en1 = Entry(h, textvariable=name1)
    en1.place(x=200, y=100)
    def r():
        h.destroy()
        game_board = Tk()
        game_board.title("Tic Tac Toe")
        l1 = Button(game_board, text=name1.get()+": X", width = 10)
        l1.grid(row=1, column=1)
        l2 = Button(game_board, text="Computer : O",
                    width=10, state=DISABLED)
        l2.grid(row=2, column=1)
        gameboard_pc(game_board, l1, l2)

    B3 = Button(h, text="CONTINUE", command=r, activeforeground='lavender',
                activebackground="azure3", bg="lavender", fg="black",
                width=20, font='summer', bd=5).pack()



def withplayer(game_board):
    game_board.destroy()
    global h
    h = Tk()
    h.geometry('250x250')
    h.title("Details")
    lb1 = Label(h, text="ENTER PLAYER1 NAME", width=20, font=("arial", 12))
    lb1.place(x=20, y=100)
    global name1
    name1 = StringVar()
    en1 = Entry(h, textvariable=name1)
    en1.place(x=200, y=100)

    lb3 = Label(h, text="ENTER PLAYER2 NAME", width=20, font=("arial", 12))
    lb3.place(x=19, y=140)
    global name2
    name2 = StringVar()
    en3 = Entry(h, textvariable=name2)
    en3.place(x=200, y=140)
    def f():
        h.destroy()
        game_board = Tk()
        game_board.title("Tic Tac Toe")
        l1 = Button(game_board, text=name1.get()+": X", width=10)

        l1.grid(row=1, column=1)
        l2 = Button(game_board, text=name2.get()+": O",
                    width=10, state=DISABLED)

        l2.grid(row=2, column=1)
        gameboard_pl(game_board, l1, l2)

    B3 = Button(h, text="CONTINUE", command=f, activeforeground='lavender',
                activebackground="azure3", bg="lavender", fg="black",
                width=50, font='summer', bd=5).pack()

def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)

    head=Label(menu, text="---Welcome to tic-tac-toe---",activeforeground='lavender',activebackground="azure3", bg="lavender",fg="black",width=500, font='summer', bd=5)

    B1 = Button(menu, text="Single Player", command=wpc,activeforeground='lavender',activebackground="azure3", bg="lavender",fg="black", width=500, font='summer', bd=5)
    B2 = Button(menu, text="Multi Player", command=wpl, activeforeground='lavender',activebackground="azure3", bg="lavender", fg="black",width=500, font='summer', bd=5)
    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='lavender',activebackground="azure3", bg="lavender", fg="black",width=500, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()
