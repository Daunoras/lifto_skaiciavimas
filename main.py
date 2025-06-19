import tkinter as tk
from tkinter import ttk, Entry

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lifto skaičiuoklė")
        self.geometry("700x300")
        self.resizable(True, True)

        first_floor_label = ttk.Label(self, text="Kiek darbuotojų pirmame aukšte")
        second_floor_label = ttk.Label(self, text="Kiek darbuotojų antrame aukšte")
        third_floor_label = ttk.Label(self, text="Kiek darbuotojų trečiame aukšte")
        meeting_floor_label = ttk.Label(self, text="Kuriame aukšte susirinkimas")
        self.result_label = ttk.Label(self, text="")
        self.first_floor_amount = Entry(self)
        self.second_floor_amount = Entry(self)
        self.third_floor_amount = Entry(self)
        self.meeting_floor = Entry(self)
        button_calculate = ttk.Button(self, text="Skaičiuoti", command=self.calculate)

        first_floor_label.grid(row=0, column=0)
        second_floor_label.grid(row=1, column=0)
        third_floor_label.grid(row=2, column=0)
        meeting_floor_label.grid(row=3, column=0)
        self.first_floor_amount.grid(row=0, column=1)
        self.second_floor_amount.grid(row=1, column=1)
        self.third_floor_amount.grid(row=2, column=1)
        self.meeting_floor.grid(row=3, column=1)
        self.result_label.grid(row=5, column=0, columnspan=2)
        button_calculate.grid(row=4, column=0)

    def calculate(self):
        pass




if __name__ == "__main__":
    app = App()
    app.mainloop()