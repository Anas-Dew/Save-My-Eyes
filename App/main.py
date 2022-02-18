from threading import Timer
from time import sleep
from tkinter import ttk
from pygame import mixer
from tkinter import * 
import os
from os import name
from plyer import notification

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

timer_val = 5 # Time for each iteration
timer_repeat = 2 # Total num of iterations

value_inside = StringVar(root)
options_list = ["Voice1", "Voice2", "Voice3"]
default = "Voice1.mp3"

# -----------------Important Functions---------------!!!  

def library():

        if value_inside.get() == '':

                mixer.music.load(default)
        else:
                mixer.music.load(f"{value_inside.get()}.mp3")

        if bottom_plate['text'] == 'Eye Care : OFF':
                pass
        else:
                mixer.music.play()

def timer():
        t = Timer(timer_val,library)
        t.start()
        print("Timer Pressed !")
        text_update()
        notify()

def notify():
        notification.notify(title = "Service Activated !",message="I will remind you after 20 mins till then, do the work baby!" ,timeout=4)

def text_update():
        
        if bottom_plate['text'] == 'Eye Care : OFF':

                bottom_plate.config(text='Eye Care :  ON')
                bottom_plate.config(bg='green')
                                            
                        
        else:
                bottom_plate.config(text='Eye Care : OFF')
                bottom_plate.config(bg='red')

        if Main_button['text'] == 'Activate':
                Main_button.config(text='Activated')
        else:
                Main_button.config(text='Activate')

      

# -----------------Other Windows---------------!!!

def options():
        mixer.music.unload()
        bottom_plate.config(text='Eye Care : OFF')
        bottom_plate.config(bg='red')

        global value_inside

        root = Tk()
        root.title("Options")
        root.resizable('False','False')
        width,height = 230,170
        root.geometry(f"{width}x{height}")
        
        Title = Label(root,text="Select From Voices Below",font="sans 10")
        Title.pack(pady=10)
        
        choose_voice = OptionMenu(root, value_inside, *options_list)
        choose_voice.pack(pady=6)

def about():
        root = Tk()
        root.title("About")
        root.resizable('False','False')
        width,height = 210,150
        root.geometry(f"{width}x{height}")

        Message = Label(root,text="Hello Geek !",font="sans 10")
        Message.pack(pady=10)

        root.mainloop()
        print("Working...")


# -----------------Menus & Buttons---------------!!!
v = StringVar(root, "1")
values = {"Enable" : "1",
          "Disable" : "2",
          }

for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
                value = value, indicator = 0,
                background = "light blue")
 

Main_button = Button(root,text='Activate',width=10,command=timer)
Main_button.pack(pady=60)

menubar = Menu(root)
menubar.add_command(label='Options',command=options)
menubar.add_command(label='About',command=about)

root.config(menu=menubar)

bottom_plate = Label(text="Eye Care : OFF", bg="Red",
                     fg="White", font="sans 9 italic")
bottom_plate.pack(side=BOTTOM, fill=X)
    
# ------------Program-Starts-Here--------------
if __name__=="__main__":
    
    root.mainloop()