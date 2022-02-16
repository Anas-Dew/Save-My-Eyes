from ctypes import alignment
from time import sleep
from pygame import mixer
from tkinter import *

mixer.init()
root = Tk()
root.title("Save My Eyes !")
root.resizable('False','False')
width,height = 250,190
root.geometry(f"{width}x{height}")

bottom_plate = Label(text="Eye Care : OFF", bg="Red",
                     fg="White", font="sans 9 italic")
bottom_plate.pack(side=BOTTOM, fill=X)



def relax():
        mixer.music.load('Voice1.mp3')
        mixer.music.load('Voice2.mp3')
        mixer.music.play(1)


def timer():
        timer_val = 5
        for j in range(12):

                
                for i in range(1200):
                        sleep(1)
                        timer_val-=1
                        
                        if timer_val == 0:
                                relax()
        

# timer_display = Label(root,text=,bg="Black",fg="White",cursor="watch")
# timer_display.pack()

Main_button = Button(root,text='Activate',width=10,command=timer)
Main_button.pack(pady=60)
                        
def text_update(event):
        if bottom_plate['text'] == 'Eye Care : OFF':

                bottom_plate.config(text='Eye Care :  ON')
        else:
                bottom_plate.config(text='Eye Care : OFF')
        if Main_button['text'] == 'Activate':
                Main_button.config(text='Activated')
        else:
                Main_button.config(text='Activate')
                
               
menubar = Menu(root)
menubar.add_command(label='Options',command=None)
menubar.add_command(label='About',command=None)
root.config(menu=menubar)
root.bind('<Button-1>',text_update)

if __name__=="__main__":
    
    root.mainloop()