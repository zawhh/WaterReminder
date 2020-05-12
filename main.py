from tkinter import Tk
from src.ui import window

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300")
    app = window.Window(root)
    root.mainloop()
