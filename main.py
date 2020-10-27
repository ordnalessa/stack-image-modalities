# Created by Alessandro Ardu (alessandro) on 27/10/2020 at 10:43
# IDE: PyCharm
# Project name: stack-image-modalities
# File name : main.py
# Entity name: main

import tkinter as tk
from src.stack_images_tk import StackImagesApp


if __name__ == "__main__":
    root = tk.Tk()
    app = StackImagesApp()
    app.Page0(root)
    root.mainloop()
