"""
A Tkinter app to deal with everything GUI related.
"""
from tkinter import *
from tkinter import ttk


class ImageWatermark:
    def __init__(self, root):
        root.title("Python Img Watermark")

        #Configure the main layout
        main_layout = ttk.Frame(root, padding="5, 5, 5, 5")
        main_layout.grid(row=0, column=0, sticky=(N, S, W, E))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ...

