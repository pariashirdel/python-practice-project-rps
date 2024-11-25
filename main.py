from tkinter import *
import random
from PIL import ImageTk, Image


root = Tk()
root.geometry('500x300')
root.title('Rock Paper Scissors')

choises = ['rock', 'paper', 'scissors']

'''
user : pc
if user goes for 
rock: tie, lose, win
paper: win, tie, lose
scissors: lose, win, tie
'''
answer ={
    'rock':['tie', 'lose', 'win'],
    'paper':['win', 'tie', 'lose'],
    'scissors':['lose', 'win', 'tie'],
}

def game(arg):
    pc = random.choice(choises)
    index_num = choises.index(pc)
    list = answer.get('rock')
    status = list[index_num]
    
    if status == 'win':
        win_window = Toplevel()
        win_window.title('You won!')
        
        background_image = Image.open('static/win.png')
        tk_image = ImageTk.PhotoImage(background_image)
        
        label1 = Label(win_window, image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
    
    if status == 'lose':
        lose_window = Toplevel()
        lose_window.title('You lost!')
        
        background_image = Image.open('static/lose.png')
        tk_image = ImageTk.PhotoImage(background_image)
        
        label1 = Label(lose_window, image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
    
    if status == 'tie':
        tie_window = Toplevel()
        tie_window.title('We got a tie.')
        
        background_image = Image.open('static/tie.png')
        tk_image = ImageTk.PhotoImage(background_image)
        
        label1 = Label(tie_window, image= tk_image, compound='center')
        label1.grid(row=4 , column=0)
        label1.image = tk_image
    


button_rock= Button(root, text='Rock', command=lambda: game('rock')).pack()
button_paper= Button(root, text='Paper', command=lambda: game('paper')).pack()
button_scissors= Button(root, text='Scissors', command=lambda: game('scissors')).pack()

root.mainloop()