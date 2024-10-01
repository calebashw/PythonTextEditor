import sys
import os
v = sys.version

is_mac = sys.platform == "darwin"

if "2.7" in v:
    from Tkinter import *
    import tkFileDialog
elif "3." in v or "3.4" in v or "3.9" in v:
    from tkinter import *
    import tkinter.filedialog as filedialog

root = Tk()
text=Text(root)
text.grid()

############################## Saving #####################################

def saveAs(event=None):
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:
        with open(savelocation, "w+") as file1:
            file1.write(t)
        
        # Getting filename from path
        filename = os.path.basename(savelocation)
        
        # Setting window title to just be filename once it's saved
        root.title(f"{filename}")

# Saving with cmd/ctrl s:
if is_mac:
    # Binding Command+S for macOS
    root.bind("<Command-s>", saveAs)  
else:
    # Bind Ctrl+S for Windows/Linux
    root.bind("<Control-s>", saveAs)  

############################## /Saving ####################################


########################## Character Count ###################################
char_count_label = Label(root, text="Characters: 0")
char_count_label.grid()

def charCount(event=None):
    chars = text.get("1.0", "end-1c")
    char_count = len(chars)
    char_count_label.config(text=f"Characters: {char_count}")

# On key release, update
text.bind("<KeyRelease>", charCount)

########################## /Character Count ###################################

############################# Font Selection ##################################
def FontHelvetica():
   global text
   text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
helvetica=IntVar() 
courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, 
command=FontHelvetica)

############################# /Font Selection #################################

button=Button(root, text="Save", command=saveAs)
button.grid()

root.title("My Personal Text Editor")

root.mainloop()
