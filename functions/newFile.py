from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter.ttk import *
from tkinter import font
from tkinter import colorchooser as ColorChooser
from tkinter import messagebox as MessageBox
from io import open
import os
from menu import root, text, message

def new_file(event=None):
    global location
    message.set("New file")
    location = ""
    text.delete(1.0, END)
    root.title("Text-Editor")