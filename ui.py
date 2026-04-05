import tkinter as tk
from tkinter import ttk
from logic import run_simulation

class SimulationUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#ecf0f1")

        # ---------- HEADER ----------
        header_frame = tk.Frame(self, bg="#2c3e50", pady=20)
        header_frame.pack(fill="x")

        tk.Label(
            header_frame,
            text="SIMULATION DE TRAFIC RÉSEAU",
            font=("Segoe UI", 22, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack()

        tk.Label(
            header_frame,
            text="Modèles M/M/1 et M/G/1",
            font=("Segoe UI", 12),
            bg="#2c3e50",
            fg="white"
        ).pack()

        # ---------- CONTAINER ----------
        container = tk.Frame(self, bg="#ecf0f1")
        container.pack(pady=20, padx=30, fill="both", expand=True)

        # -------- PARAMÈTRES --------
        param_frame = tk.Frame(container, bg="white", bd=2, relief="groove")
        param_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        tk.Label(param_frame, text="Paramètres", font=("Segoe UI", 14, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(param_frame, text="λ Taux d'arrivée", bg="white").grid(row=1, column=0, pady=10, sticky="w")
        entry_lambda = ttk.Entry(param_frame, width=20)
        entry_lambda.grid(row=1, column=1, pady=10, sticky="e")

        # -------- μ (stocké pour pouvoir le cacher) --------
        mu_label = tk.Label(param_frame, text="μ Taux de service", bg="white")
        mu_label.grid(row=2, column=0, pady=10, sticky="w")

        entry_mu = ttk.Entry(param_frame, width=20)
        entry_mu.grid(row=2, column=1, pady=10, sticky="e")

        tk.Label(param_frame, text="Nombre de requêtes", bg="white").grid(row=3, column=0, pady=10, sticky="w")
        entry_n = ttk.Entry(param_frame, width=20)
        entry_n.grid(row=3, column=1, pady=10, sticky="e")

        # -------- MODÈLE --------
        model_frame = tk.Frame(container, bg="white", bd=2, relief="groove")
        model_frame.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        tk.Label(model_frame, text="Choix du modèle", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

        model_var = tk.StringVar(value="M/M/1")
        ttk.Radiobutton(model_frame, text="M/M/1", variable=model_var, value="M/M/1").pack(anchor="w", padx=20, pady=5)
        ttk.Radiobutton(model_frame, text="M/G/1", variable=model_var, value="M/G/1").pack(anchor="w", padx=20, pady=5)

        # -------- TYPE --------
        type_frame = tk.Frame(container, bg="white", bd=2, relief="groove")
        type_frame.grid(row=1, column=0, columnspan=2, pady=15, sticky="nsew")

        tk.Label(type_frame, text="Type de variable", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

        type_var = tk.StringVar(value="Continue")

        # -------- Fonction pour cacher/afficher μ --------
        def update_mu_state():
            if type_var.get() == "Discrète":
                mu_label.grid_remove()
                entry_mu.grid_remove()
            else:
                mu_label.grid()
                entry_mu.grid()

        ttk.Radiobutton(type_frame, text="Continue", variable=type_var, value="Continue", command=update_mu_state).pack(side="left", padx=40, pady=10)
        ttk.Radiobutton(type_frame, text="Discrète", variable=type_var, value="Discrète", command=update_mu_state).pack(side="left", padx=40, pady=10)

        # -------- BOUTON --------
        result_var = tk.StringVar()

        def safe_run():
            try:
                if not entry_lambda.get() or not entry_n.get():
                    result_var.set("Remplissez λ et N")
                    return

                if type_var.get() == "Continue" and not entry_mu.get():
                    result_var.set("μ requis en mode continu")
                    return

                run_simulation(entry_lambda, entry_mu, entry_n, model_var, type_var, result_var)

            except Exception as e:
                result_var.set(f"Erreur : {e}")

        run_btn = tk.Button(
            self,
            text="▶ Lancer la simulation",
            font=("Segoe UI", 14, "bold"),
            bg="#2980b9",
            fg="white",
            padx=30,
            pady=12,
            relief="flat",
            cursor="hand2",
            command=safe_run
        )
        run_btn.pack(pady=20)

        # -------- RÉSULTATS --------
        result_frame = tk.Frame(self, bg="white", bd=2, relief="groove")
        result_frame.pack(fill="both", padx=50, pady=20, expand=True)

        tk.Label(result_frame, text="Résultats de la simulation", font=("Segoe UI", 14, "bold"), bg="white").pack(pady=10)

        result_label = tk.Label(
            result_frame,
            textvariable=result_var,
            font=("Segoe UI", 12),
            bg="white",
            fg="#2c3e50",
            justify="left"
        )
        result_label.pack(padx=10, pady=10)