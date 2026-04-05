import tkinter as tk
from login import LoginPage
from dashboard import Dashboard


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Simulation Réseau")
        self.geometry("900x600")

        self.current_frame = None
        self.show_login()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_login(self):
        self.clear_frame()
        self.current_frame = LoginPage(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.clear_frame()
        self.current_frame = Dashboard(self)
        self.current_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Erreur critique : {e}")