import tkinter as tk
import tkinter.ttk as ttk

from main import Clipper

class Application(Clipper):
    def __init__(self, master):

        clipper = Clipper(master)
        clipper.pack(fill='both', expand=True)

        master.mainloop()

if __name__ == '__main__':
    window = tk.Tk()
    window.minsize(width=600, height=400)
    window.maxsize(width=600, height=400)
    window.iconbitmap(r"C:\Users\User\PycharmProjects\split-merge-pdf\icon.ico")
    window.title("clipper")
    app = Application(window)