from threading import Timer
from tkinter import ttk
from pygame import mixer
from tkinter import * 
import os
from os import name
# -----------------Initializing---------------!!!
def Work():
  
    # for windows
    if name == 'nt':
        _ = os.chdir('C:/Projects/Save-My-Eyes/App/')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        username = os.getlogin()
        _ = os.chdir(f'/home/{username}/Projects/Save-My-Eyes/App/')
Work()

mixer.init()
root = Tk()
root.title("Save My Eyes !")
root.resizable('False','False')
width,height = 250,190
root.geometry(f"{width}x{height}")

timer_val = 5 # Timer for each iteration
timer_repeat = 2 # Total num of iterations

# -----------------Important Functions---------------!!!
def library():
        mixer.music.load('Voice1.mp3')
        mixer.music.load('Voice2.mp3')
        mixer.music.play()

        
def timer():
        for repeat in range(timer_repeat):
                t = Timer(timer_val,library)
                t.start()
                print("Loop happend")

def text_update(event):
        
        if bottom_plate['text'] == 'Eye Care : OFF':

                bottom_plate.config(text='Eye Care :  ON')
        else:
                bottom_plate.config(text='Eye Care : OFF')
        if Main_button['text'] == 'Activate':
                Main_button.config(text='Activated')
        else:
                Main_button.config(text='Activate')
# -----------------Other Windows---------------!!!

def options():
        root = Tk()
        root.title("Options")
        root.resizable('False','False')
        width,height = 230,170
        root.geometry(f"{width}x{height}")

        Title = Label(root,text="Select From Voices Below",font="sans 10")
        Title.pack(pady=10)

        options_list = ["Voice 1", "Voice 2", "Voice 3"]
        value_inside = StringVar(root)
        value_inside.set(options_list[1])

        def h(event):
                print(value_inside.get())
        root.bind('<Return>',h)
        
        question_menu = OptionMenu(root, value_inside, *options_list)
        question_menu.pack(pady=6)
        
        root.mainloop()

def about():
        root = Tk()
        root.title("About")
        root.mainloop()
        print("Working...")


# -----------------Menus & Buttons---------------!!!
Main_button = Button(root,text='Activate',width=10,command=timer)
Main_button.pack(pady=60)

menubar = Menu(root)
menubar.add_command(label='Options',command=options)
menubar.add_command(label='About',command=about)

root.config(menu=menubar)
root.bind('<Button-1>',text_update)

bottom_plate = Label(text="Eye Care : OFF", bg="Red",
                     fg="White", font="sans 9 italic")
bottom_plate.pack(side=BOTTOM, fill=X)
    
# ------------Program-Starts-Here--------------
if __name__=="__main__":
    
    root.mainloop()