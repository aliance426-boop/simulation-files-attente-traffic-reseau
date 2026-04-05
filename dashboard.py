import tkinter as tk
from ui import SimulationUI
from PIL import Image, ImageTk
import os


class Dashboard(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#f4f6f7")

        # MENU GAUCHE
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        self.sidebar.pack(side="left", fill="y")

        tk.Label(
            self.sidebar,
            text="MENU",
            bg="#2c3e50",
            fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=20)

        tk.Button(
            self.sidebar,
            text="Simulation",
            bg="#1abc9c",
            fg="white",
            width=15,
            command=self.show_simulation
        ).pack(pady=10)

        tk.Button(
            self.sidebar,
            text="Historique",
            bg="#3498db",
            fg="white",
            width=15
        ).pack(pady=10)

        tk.Button(
            self.sidebar,
            text="Déconnexion",
            bg="#e74c3c",
            fg="white",
            width=15,
            command=master.show_login
        ).pack(pady=10)

        # CONTENU DROITE
        self.content = tk.Frame(self, bg="#f4f6f7")
        self.content.pack(side="right", fill="both", expand=True)

        self.show_home()

    # PAGE ACCUEIL
    def show_home(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        # ===== FRAME TITRE =====
        titre_frame = tk.Frame(self.content, bg="#f4f6f7")
        titre_frame.pack(pady=20, fill="x")

        # TITRE DÉFILANT
        self.title_text = "Bienvenue dans notre application de simulation réseau    "
        self.title_label = tk.Label(
            titre_frame,
            text=self.title_text,
            font=("Segoe UI", 20, "bold"),
            bg="#f4f6f7",
            fg="#2c3e50"
        )
        self.title_label.pack()

        def defile_titre():
            self.title_text = self.title_text[1:] + self.title_text[0]
            self.title_label.config(text=self.title_text)
            self.content.after(150, defile_titre)

        defile_titre()

        # ===== FRAME IMAGE =====
        image_frame = tk.Frame(self.content, bg="#f4f6f7")
        image_frame.pack(pady=20)

        # Chargement image
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "network.png")

        try:
            image = Image.open(image_path)
            image = image.resize((900, 400))
            self.img = ImageTk.PhotoImage(image)  # important : garder référence
            img_label = tk.Label(image_frame, image=self.img, bg="#f4f6f7")
            img_label.pack()

        except FileNotFoundError:
            tk.Label(
                image_frame,
                text="Image non trouvée",
                font=("Segoe UI", 14),
                bg="#f4f6f7"
            ).pack()

        except Exception as e:
            tk.Label(
                image_frame,
                text=f"Erreur chargement image",
                font=("Segoe UI", 14),
                bg="#f4f6f7"
            ).pack()

        # ===== FRAME DESCRIPTION =====
        desc_frame = tk.Frame(self.content, bg="#f4f6f7")
        desc_frame.pack(pady=20)

        description = tk.Label(
            desc_frame,
            text="Cette application permet de simuler le trafic réseau\navec les modèles M/M/1 et M/G/1.",
            font=("Segoe UI", 14),
            bg="#f4f6f7",
            fg="#34495e",
            justify="center"
        )
        description.pack()

    # PAGE SIMULATION
    def show_simulation(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        simulation = SimulationUI(self.content)
        simulation.pack(fill="both", expand=True)