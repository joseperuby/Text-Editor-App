################################################
#                                              #
#########       Description 😎       ###########
# """ This is my text editor using tkinter """ #
#                                              #
#########           Autor 🧑🏻         ###########
#              """ Joseperuby """              #
#                                              #
#################################################

# Modules
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter.ttk import *
from tkinter import font
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox
from io import open
import os
import tempfile


# Pred Var
location = "" 
font_size_pred = 12
font_style_pred = 'Arial'
weight_pred = 'normal'
slant_pred = 'roman'
underline_pred = 'normal'



# Functions
def new_file(event=None):
    global location
    message.set("New file")
    location = ""
    text.delete(1.0, END)
    root.title("Text-Editor")

def open_file(event=None):
    global location
    message.set("Open file")
    location = FileDialog.askopenfilename(
        initialdir='.',
        filetype = (("File text", "*.txt"),),
        title="Open a file text")
    
    if location != "":
        file = open(location, 'r')
        content = file.read()
        text.delete(1.0, END)
        text.insert('insert', content)
        file.close()
        root.title(location + " Text-Editor")

def save_file(event=None):
    message.set("Save file")
    if location != "":
        content = text.get(1.0, 'end-1c')
        file = open(location,'w+')
        file.write(content)
        file.close()
        message.set("File successfully saved")
    else:
        save_as_file(event)

def save_as_file(event=None):
    global location
    message.set("Save file as")
    file = FileDialog.asksaveasfile(title="Save file", mode="w", defaultextension=".txt")
    if file is not None:
        if location is None:
            pass
        else:
            location = file.name
            content = text.get(1.0, 'end-1c')
            file = open(location,'w+')
            file.write(content)
            file.close()
            message.set("File successfully saved")
    else:
        message.set("Guardado cancelado")
        location = ""

def close_window(event=None):
    global location
    if text.edit_modified():
       answer = MessageBox.askyesnocancel("Warning", "Do you want to save the file?")
       if answer is True:
            if location != "":
                content = text.get(0.0, END)
                file = open(location, "w+")
                file.write()
                file.close()
                root.destroy()
            else:
                content = text.get(0.0, END)
                file = FileDialog.asksaveasfile(title="Save file", mode="w", defaultextension=".txt")
                if file is not None:
                    location = file.name
                    content = text.get(1.0, 'end-1c')
                    file = open(location,'w+')
                    file.write(content)
                    file.close()
                    root.destroy
                else:
                    message.set("Guardado cancelado")
                    location = ""
                    root.destroy()

       elif answer is False:
            root.destroy()
       else:
            pass
    else:
        root.destroy()

def print_out(event=None):
    file_txt = tempfile.mktemp(".txt")
    open(file_txt, "w").write(text.get(1.0, END))
    os.startfile(file_txt, "print")

def font_style(Any):
    global font_style_pred
    font_style_pred = font_family_var.get()
    text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred))

def font_size(Any):
    global font_size_pred
    font_size_pred = font_size_var.get()
    text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred))

def text_bold(): 
   global weight_pred
   textConfig = font.Font(font=text['font']).actual()
   if textConfig['weight'] == 'normal':
       weight_pred = 'bold'
       text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred))

   elif textConfig['weight'] == 'bold':
       weight_pred = 'normal'
       text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred))

def text_italic():
    global slant_pred
    textConfig = font.Font(font=text['font']).actual()
    if textConfig['slant'] == 'roman':
       slant_pred = 'italic'
       text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred))

    elif textConfig['slant'] == 'italic':
       slant_pred = 'roman'
       text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred))

def text_underline():
    global underline_pred
    textConfig = font.Font(font=text['font']).actual()
    if textConfig['underline'] == 0:
       underline_pred = 'underline'
       text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred, underline_pred))

    elif textConfig['underline'] == 1:
       text.config(font=(font_style_pred, font_size_pred, weight_pred, slant_pred,))

def select_color():
    color = ColorChooser.askcolor()
    text.config(fg=color[1])

def align_left():
    data = text.get(0.0, END)
    text.tag_config("left", justify="left")
    text.delete(0.0, END)
    text.insert(INSERT, data, "left")
    

def align_right():
    data = text.get(0.0, END)
    text.tag_config("right", justify="right")
    text.delete(0.0, END)
    text.insert(INSERT, data, "right")

def align_center():
    data = text.get(0.0, END  )
    text.tag_config("center", justify="center")
    text.delete(0.0, END)
    text.insert(INSERT, data, "center")

def status_bar(event):
    if text.edit_modified():
        word = len(text.get(0.0,END).split())
        characters = len(text.get(0.0, "end-1c").replace(" ",""))
        message.set(f"Characters: {characters} Words: {word}")

    text.edit_modified(False)

def find_text():

    # Root2 Functions
    def find_words():
        text.tag_remove("match", 1.0, END)
        start = "1.0"
        word = entry_find.get()
        if word:
            while True:
                start = text.search(word, start, stopindex=END)
                if not start:
                    break
                end_post = f"{start} + {len(word)}c"
                text.tag_add("match", start, end_post)

                text.tag_config("match", foreground="red", background="yellow")
                start = end_post

    def replace_words():
        word = entry_find.get()
        replace_word = entry_replace.get()
        content = text.get(1.0, END)
        new_content = content.replace(word, replace_word)
        text.delete(1.0, END)
        text.insert(1.0, new_content)

    def no_tag():
        text.tag_remove("match", 1.0, END)
        root2.destroy()

    # New root in top of the other
    root2 = Toplevel()
    root2.title("Find")
    root2.geometry("460x260+500+200")
    root2.resizable(0, 0)

    label_frame = LabelFrame(root2, text="Find/Replace")
    label_frame.pack(pady=25)

    find_label = Label(label_frame, text="Find")
    find_label.grid(row=0, column=0, padx=5, pady=5)
    entry_find = Entry(label_frame)
    entry_find.grid(row=0, column=1)

    replace_label = Label(label_frame, text="Replace")
    replace_label.grid(row=1, column=0, padx=5, pady=5)
    entry_replace = Entry(label_frame)
    entry_replace.grid(row=1, column=1)

    find_button = Button(label_frame, text="Find", command=find_words)
    find_button.grid(row=2, column=0, padx=5, pady=5)

    replace_button = Button(label_frame, text="Replace", command=replace_words)
    replace_button.grid(row=2, column=1, padx=5, pady=5)

    
    root2.protocol("WM_DELETE_WINDOW", no_tag)
    root2.mainloop()

def show_hide_toolbar():
    if toolbar_var.get() == False:
        toolbar.pack_forget()
    if toolbar_var.get() == True:
        text.pack_forget()
        toolbar.pack(fill=X)
        text.pack(fill="both", expand=1)

def show_hide_statusbar():
    if statusbar_var.get() == False:
        monitor.pack_forget()
    if statusbar_var.get() == True:
        monitor.pack(side="bottom")

def color_theme(bg_color, fg_color):
    text.config(bg=bg_color, fg=fg_color)

# Root configuration
root = Tk()
root.title("Text-Editor")
root.iconbitmap("C:\\Users\\Pepe\\Desktop\\Editor\\Images\\text-editor.ico")
root.geometry("1260x620")

# Images
new_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\new.png")
open_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\open.png")
save_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\save.png")
save_as_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\save_as.png")
close_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\close.png")
copy_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\copy.png")
paste_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\paste.png")
cut_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\cut.png")
clear_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\clear.png")
find_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\find.png")
tool_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\tool.png")
status_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\status.png")
white_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\white.png")
black_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\black.png")
pink_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\pink.png")
bold_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\bold.png")
italic_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\italic.png")
underline_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\underline.png")
font_color_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\font_color.png")
left_align_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\left_align.png")
center_align_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\center_align.png")
right_align_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\right_align.png")
print_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\print.png")
select_all_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\select.png")
undo_image = PhotoImage(file="C:\\Users\\Pepe\\Desktop\\Editor\\Images\\undo.png")

# Toolbar 
toolbar = Label(root)
toolbar.pack(side="top", fill=X)

# Font families
font_family_var = StringVar()
font_families = font.families()
font_Combobox = Combobox(toolbar, width= 30, values=font_families, state="readonly", textvariable=font_family_var)
font_Combobox.current(font_families.index("Arial"))
font_Combobox.grid(row=0, column=0, padx=5)

# Font size
font_size_var = IntVar()
font_size_Combobox = Combobox(toolbar, width=10, textvariable=font_size_var, state="readonly", values=tuple(range(5, 101)))
font_size_Combobox.current(7)
font_size_Combobox.grid(row=0, column=1, padx=5)
font_Combobox.bind("<<ComboboxSelected>>", font_style)
font_size_Combobox.bind("<<ComboboxSelected>>", font_size)

# Buttons
bold_button = Button(toolbar, image=bold_image, command=text_bold)
bold_button.grid(row=0, column=2, padx=5)

italic_button = Button(toolbar, image=italic_image, command=text_italic)
italic_button.grid(row=0, column=3, padx=5)

underline_button = Button(toolbar, image=underline_image, command=text_underline)
underline_button.grid(row=0, column=4, padx=5)

font_color_button = Button(toolbar, image=font_color_image, command=select_color)
font_color_button.grid(row=0, column=5, padx=5)

left_align_button = Button(toolbar, image=left_align_image, command=align_left)
left_align_button.grid(row=0, column=6, padx=5)

center_align_button = Button(toolbar, image=center_align_image, command=align_center)
center_align_button.grid(row=0, column=7, padx=5)

right_align_button = Button(toolbar, image=right_align_image, command=align_right)
right_align_button.grid(row=0, column=8, padx=5)

# Text Widget
text = Text(root,undo = True)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=(font_style_pred, font_size_pred))


# Bottom label
message = StringVar()
message.set("Welcome to the best text editor!")
monitor = Label(root, textvar=message, justify="left")
monitor.pack(side="bottom")

# Menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
viewmenu = Menu(menubar, tearoff=0)
themesmenu = Menu(menubar, tearoff=0)

# Filemenu
filemenu.add_command(label="New", accelerator="Ctrl + N", image=new_image, compound="left" ,command=new_file)
filemenu.add_command(label="Open", accelerator="Ctrl + O", image=open_image, compound="left" ,command=open_file)
filemenu.add_command(label="Save", accelerator="Ctrl + S", image=save_image, compound="left" ,command=save_file)
filemenu.add_command(label="Save as", accelerator="Ctrl + Alt + S", image=save_as_image, compound="left" ,command=save_as_file)
filemenu.add_command(label="Print", accelerator="Ctrl + P", image=print_image, compound="left", command=print_out)
filemenu.add_separator()
filemenu.add_command(label="Close", accelerator="Ctrl + Q", image=close_image, compound="left" ,command=close_window)
menubar.add_cascade(menu=filemenu, label="File")

# Viewmenu
toolbar_var = BooleanVar()
statusbar_var = BooleanVar()
viewmenu.add_checkbutton(label="Tool Bar", variable=toolbar_var, onvalue=True, offvalue=False, image= tool_image, compound="left", command=show_hide_toolbar)
viewmenu.add_separator()
viewmenu.add_checkbutton(label="Status Bar", variable=statusbar_var, onvalue=True, offvalue=False, image= status_image, compound="left", command=show_hide_statusbar)
menubar.add_cascade(menu=viewmenu, label="View")
toolbar_var.set(True)
statusbar_var.set(True)

# Themesmenu
theme_choice = StringVar()
themesmenu.add_radiobutton(label="Light", image= white_image, variable=theme_choice, compound="left", 
                           command=lambda :color_theme('white', 'black'))
themesmenu.add_radiobutton(label="Dark", image= black_image, variable=theme_choice, compound="left",
                           command=lambda :color_theme('black', 'white'))
themesmenu.add_radiobutton(label="Pink", image= pink_image, variable=theme_choice, compound="left",
                           command=lambda: color_theme('pink', 'black'))
menubar.add_cascade(menu=themesmenu, label="Theme")

# Editmenu
editmenu.add_command(label="Undo", accelerator="Ctrl + Z", image=undo_image, compound="left")
editmenu.add_command(label="Copy", accelerator="Ctrl + C", image=copy_image, compound="left",
                     command= lambda: text.event_generate("<Control c>"))
editmenu.add_command(label="Cut", accelerator="Ctrl + X", image=cut_image, compound="left", 
                     command= lambda: text.event_generate("<Control x>"))
editmenu.add_command(label="Paste", accelerator="Ctrl + V", image=paste_image, compound="left",
                     command= lambda: text.event_generate("<Control v>"))
editmenu.add_command(label="Select All", accelerator="Ctrl + A", image=select_all_image, compound="left")

editmenu.add_separator()

editmenu.add_command(label="Clear", accelerator="Ctrl + Alt + X", image=clear_image, compound="left",
                     command=lambda: text.delete(0.0, END))
editmenu.add_command(label="Find", accelerator="Ctrl + F", image=find_image, compound="left",
                     command=find_text)
menubar.add_cascade(menu=editmenu, label="Edit")
root.config(menu=menubar)

# Bind
text.bind("<<Modified>>", status_bar)
root.bind("<Control-o>", open_file)
root.bind("<Control-n>", new_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Alt-s>", save_as_file)
root.bind("<Control-q>", close_window)
root.bind("<Control-p>", print_out)
 
# Mainloop
root.mainloop()