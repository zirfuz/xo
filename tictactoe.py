import tkinter as tk
from tictactoecore import TicTacToeCore

import winsound         # for sound

def beep(freq, dur):
    winsound.Beep(freq, dur)

G_SIZE = 10

class TicTacToe:
    def __init__(self, size):
        self.__root = tk.Tk()
        self.__frame = tk.Frame(self.__root)
        self.__frame.pack()
        self.__root.resizable(0,0)
        self.__root.wm_title('Tic-Tac-Toe')
        img_arg = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='
        self.__emptyImg = tk.PhotoImage(img_arg)
        self.__ttt = TicTacToeCore(size)
        self.__cong = False
        self.__buttons = [[None] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                self.__buttons[i][j] = tk.Button(self.__frame, width=2, height=1, disabledforeground="blue", font=('', 10, 'bold'))
                self.__buttons[i][j].grid(row=i, column=j)
                self.__buttons[i][j].bind('<Button>', self.__clicked)
        self.__button1 = tk.Button(self.__frame, text="Player", fg="blue")
        self.__button1.grid(row=size, column=0, columnspan=2)
        self.__button2 = tk.Button(self.__frame, text="Player", fg="red")
        self.__button2.grid(row=size, column=size-2, columnspan=2)
        self.__new_res = tk.Button(self.__frame, text="New", command=self.__reset)
        self.__new_res.grid(row=size, column=(size-1)//2, columnspan=2)
    def run(self):
        self.__root.mainloop()
    def __clicked(self, event):
        but = event.widget
        grid_info = but.grid_info()
        i, j = grid_info['row'], grid_info['column']
        current = self.__ttt.current
        go = self.__ttt.game_over
        if self.__ttt.action(i,j) != None:
            x_turn = current == 'x'
            but['text'] = '✕' if x_turn else '◯'
            but['disabledforeground'] = 'blue' if x_turn else 'red'
            but['state'] = 'disabled'
            freq = 350 if x_turn else 300
            if not self.__ttt.win():
                beep(freq, 200)
        win_cells = self.__ttt.win()
        if win_cells is not None and not go:
            self.__set_buttons_state(False)
            for cell in win_cells:
                self.__buttons[cell[0]][cell[1]]['background'] = 'orange'
            beep(400, 500)
    def __set_buttons_state(self, val):
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__buttons[i][j]['state'] = 'normal' if val else 'disabled'
        #state = 'normal' if val else 'disabled'
        #self.__for_each(self, lambda self, but, state: but['state']=state)
    def __reset(self):
        self.__set_buttons_state(True)
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__ttt.reset()
                but = self.__buttons[i][j]
                but['text'] = ''
                but['background'] = self.__root.cget("background")
        beep(700, 75)
    # def __for_each(self, fun, *args):
    #     for i in range(self.__ttt.size):
    #         for j in range(self.__ttt.size):
    #             fun(self.__buttons[i][j], args)



if __name__ == "__main__":
    ttt = TicTacToe(G_SIZE)
    ttt.run()
