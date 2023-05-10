from tkinter import Tk, Button
from screens import render_register_screen
from screens import render_main_screen
from json import dumps

if __name__ == '__main__':
    tk = Tk()
    tk.geometry('600x600')
    tk.title('The GUI Shop')
    render_main_screen(tk)
    tk.mainloop()
