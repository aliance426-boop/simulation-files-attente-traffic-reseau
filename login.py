import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="#2980b9")  # fond bleu moderne

        # ---------- TITRE ----------
        title = tk.Label(
            self,
            text="Bienvenue !",
            font=("Segoe UI", 28, "bold"),
            bg="#2980b9",
            fg="white"
        )
        title.pack(pady=40)

        subtitle = tk.Label(
            self,
            text="Connectez-vous pour continuer",
            font=("Segoe UI", 14),
            bg="#2980b9",
            fg="white"
        )
        subtitle.pack(pady=10)

        # ---------- CADRE DE CONNEXION ----------
        form = tk.Frame(self, bg="white", padx=50, pady=40)
        form.pack(pady=30)
        form.configure(highlightbackground="#34495e", highlightthickness=2)

        # -- Entrées utilisateur --
        tk.Label(form, text="Utilisateur", bg="white", font=("Segoe UI", 12)).grid(row=0, column=0, pady=15, sticky="w")
        self.username = tk.Entry(form, font=("Segoe UI", 12), bd=2, relief="groove", width=25)
        self.username.grid(row=0, column=1, pady=15, padx=10)

        tk.Label(form, text="Mot de passe", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, pady=15, sticky="w")
        self.password = tk.Entry(form, font=("Segoe UI", 12), bd=2, relief="groove", show="*", width=25)
        self.password.grid(row=1, column=1, pady=15, padx=10)

        # -- Bouton Connexion --
        self.login_btn = tk.Button(
            form,
            text="Se connecter",
            bg="#27ae60",
            fg="white",
            font=("Segoe UI", 13, "bold"),
            width=20,
            relief="flat",
            cursor="hand2",
            command=self.login
        )
        self.login_btn.grid(row=2, column=0, columnspan=2, pady=25)

        # -- Hover effet sur le bouton --
        self.login_btn.bind("<Enter>", lambda e: self.login_btn.config(bg="#2ecc71"))
        self.login_btn.bind("<Leave>", lambda e: self.login_btn.config(bg="#27ae60"))

        # Optionnel : bouton réinitialiser mot de passe
        tk.Button(
            form,
            text="Mot de passe oublié ?",
            bg="white",
            fg="#2980b9",
            font=("Segoe UI", 10, "underline"),
            bd=0,
            cursor="hand2",
            command=lambda: messagebox.showinfo("Info", "Fonction non implémentée")
        ).grid(row=3, column=0, columnspan=2)

        # ---------- INFOS DE CONNEXION----------
        tk.Label(
            self,
            text="Utilisateur: admin | Mot de passe: 1234",
            font=("Segoe UI", 10),
            bg="#2980b9",
            fg="white"
        ).pack(side="bottom", pady=10)

        # ---------- LIAISON TOUCHE ENTREE ----------
        self.username.bind("<Return>", lambda event: self.login())
        self.password.bind("<Return>", lambda event: self.login())

    # ---------- FONCTION DE LOGIN ----------
    def login(self):
        if self.username.get() == "admin" and self.password.get() == "1234":
            self.master.show_dashboard()
        else:
            messagebox.showerror("Erreur", "Identifiants incorrects")