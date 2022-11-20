from tkinter import *
class Login:
    def __init__(self, Login_window):
        self.Login_window = Login_window

def main_window_login():
    login_window = Tk()
    login_window.title("Library")
    login_window.configure(width=700, height=500)
    login_window.configure(bg='lightgreen')
    login_window.mainloop()


main_window_login()