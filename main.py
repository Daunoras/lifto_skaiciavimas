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
        starting_floor_label = ttk.Label(self, text="Kuriame aukšte liftas")
        self.result_label = ttk.Label(self, text="")
        self.first_floor_amount = Entry(self)
        self.second_floor_amount = Entry(self)
        self.third_floor_amount = Entry(self)
        self.meeting_floor = Entry(self)
        self.starting_floor = Entry(self)
        button_calculate = ttk.Button(self, text="Skaičiuoti", command=self.print_result)

        first_floor_label.grid(row=0, column=0)
        second_floor_label.grid(row=1, column=0)
        third_floor_label.grid(row=2, column=0)
        meeting_floor_label.grid(row=3, column=0)
        starting_floor_label.grid(row=4, column=0)
        self.first_floor_amount.grid(row=0, column=1)
        self.second_floor_amount.grid(row=1, column=1)
        self.third_floor_amount.grid(row=2, column=1)
        self.meeting_floor.grid(row=3, column=1)
        self.starting_floor.grid(row=4, column=1)
        self.result_label.grid(row=6, column=0, columnspan=2)
        button_calculate.grid(row=5, column=0)

    def calculate(self):
        def arrival():
            pass

        def onboarding():
            pass

        trips = 0
        floors = {1: int(self.first_floor_amount.get()),
                  2: int(self.second_floor_amount.get()),
                  3: int(self.third_floor_amount.get())}
        total_people = sum(floors.values())
        current_floor = int(self.starting_floor.get())
        meet_floor = int(self.meeting_floor.get())
        elevator_amount = 0

        while floors[current_floor] < total_people:
            if elevator_amount > 0 and current_floor == meet_floor:
                arrival()

            trips += 1

        return trips



    def create_result(self):
        if not (self.first_floor_amount.get() and
                self.second_floor_amount.get() and
                self.third_floor_amount.get() and
                self.starting_floor.get() and
                self.meeting_floor.get()):
            return "Įvesti nevisi duomenys"
        if int(self.meeting_floor.get()) not in [1, 2, 3]:
            return "neteisingas susirinkimo aukštas"
        if int(self.starting_floor.get()) not in [1, 2, 3]:
            return "neteisingas esamas lifto aukštas"
        return f"Prireiks {self.calculate()} kelionių liftu."

    def print_result(self):
        self.result_label.config(text=self.create_result())






if __name__ == "__main__":
    app = App()
    app.mainloop()