from tkinter import Frame, BOTH, Button, messagebox


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Water Reminder")
        self.pack(fill=BOTH, expand=1)
        drinkButton = Button(self, text="I've drink water",
                             command=self.drinkReminderCallback)
        drinkButton.place(x=0, y=0)

    def drinkReminderCallback(self):
        messagebox.showinfo("Hello Ruki", "Time to drink water")
