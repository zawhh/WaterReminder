import tkinter as tk
from tkinter import messagebox
import time


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.interval_sec = 10
        self.count_sec = self.interval_sec
        self.init_window()

    def init_window(self):
        self.master.title("Water Reminder")
        self.pack(fill=tk.BOTH, expand=1)
        self.start_reminder()
        self.time = tk.StringVar()
        self.label1 = tk.Label(self, justify='center',
                               textvariable=self.time, font='times 25 bold')
        self.label1.pack()

    def start_reminder(self):
        # self.after(self.interval_sec*1000, self.show_message)
        self.start_per_second()

    def show_message(self):
        messagebox.showinfo("Hello Ruki", "Time to drink water")
        # # 30 min
        # self.after(self.interval_sec*1000, self.show_message)

    def start_per_second(self):
        self.after(1000, self.per_second)

    def per_second(self):
        self.count_sec = self.count_sec - 1
        self.update_time()
        self.after(1000, self.per_second)

    def update_time(self):
        self.time.set(str(self.count_sec))
        if (self.count_sec == 0):
            self.count_sec = self.interval_sec
            self.show_message()
