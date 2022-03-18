from threading import Timer
from tkinter import ttk
from pygame import mixer
from tkinter import * 
import os
from os import name
from plyer import notification
# -----------------Initializing---------------!!!
def setPath():
    # for windows
    current_dir = os.getcwd()
    print("Current Directory ---> ", current_dir)

    if name == 'nt':
        _ = os.chdir(f'{current_dir}\\Save-My-Eyes\\App\\')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.chdir(f'{current_dir}')

setPath()
print(os.getcwd())
mixer.init()
root = Tk()
photo = PhotoImage(file = "icon_.png")
root.iconphoto(False, photo)
root.title("Save My Eyes")
root.resizable('False','False')
width,height = 250,190
root.geometry(f"{width}x{height}")

timer_val = 1200 # Time for each iteration
# timer_repeat = 2 # Total num of iterations

value_inside = StringVar(root)
options_list = ["Voice1", "Voice2"]
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
        # notify_me("0")
        
        s = Timer(timer_val+6,default_state)
        s.start()


def notify_me(type_notify):
        if type_notify == "0":
                notification.notify(title = "Service Activated !",message="I will remind you after 20 mins till then, do the work !" ,timeout=4)
        elif type_notify == "1":
                notification.notify(title = "Service Stopped !",message="Re-activate, if needed !" ,timeout=4)
        
def text_update():
        
        if bottom_plate['text'] == 'Eye Care : OFF':

                bottom_plate.config(text='Eye Care :  ON')
                bottom_plate.config(bg='green')
                notify_me("0")
                     
        else:
                bottom_plate.config(text='Eye Care : OFF')
                bottom_plate.config(bg='red')
                notify_me("1")
        if Main_button['text'] == 'Activate':
                Main_button.config(text='Activated')
        else:
                Main_button.config(text='Activate')

      

# -----------------Other Windows---------------!!!
def default_state():
        # if __name__== "__timer__":
        notify_me("1")
        Main_button.config(text='Activate')
        bottom_plate.config(text='Eye Care : OFF')
        bottom_plate.config(bg='red')

def options():
        mixer.music.stop()
        mixer.music.unload()
        default_state()

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


# -----------------Menus & Buttons---------------!!! 

Main_button = Button(root,text='Activate',width=10,command=timer)
Main_button.pack(pady=60)

menubar = Menu(root)
menubar.add_command(label='Options',command=options)

root.config(menu=menubar)

bottom_plate = Label(text="Eye Care : OFF", bg="Red",
                     fg="White", font="sans 9 italic")
bottom_plate.pack(side=BOTTOM, fill=X)
    
# ------------Program-Starts-Here--------------
if __name__=="__main__":
    root.mainloop()