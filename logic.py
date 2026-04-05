import numpy as np
import matplotlib.pyplot as plt
from simulation import simulate_mm1, simulate_mg1

def run_simulation(entry_lambda, entry_mu, entry_n, model_var, type_var, result_var):
    try:
        # ----------- RÉCUPÉRATION SÉCURISÉE -----------
        lam = float(entry_lambda.get())
        n = int(entry_n.get())

        if lam <= 0 or n <= 0:
            result_var.set("Valeurs invalides")
            return

        # μ seulement si CONTINU
        if type_var.get() == "Continue":
            mu = float(entry_mu.get())
            if mu <= 0:
                result_var.set("μ doit être > 0")
                return
        else:
            mu = None  # inutile en discret

        # ----------- SIMULATION -----------
        if type_var.get() == "Continue":

            if model_var.get() == "M/M/1":
                wait = simulate_mm1(lam, mu, n)
            else:
                wait = simulate_mg1(lam, mu, n)

            if len(wait) == 0:
                result_var.set("Erreur dans la simulation")
                return

            avg = np.mean(wait)
            rho = lam / mu

            result_var.set(f"Temps moyen: {avg:.3f}    |    ρ = {rho:.3f}")

        else:
            # ----------- MODE DISCRET -----------
            counts = np.random.poisson(lam, n)

            avg = np.mean(counts)

            result_var.set(f"Moyenne (discret): {avg:.3f}")

        # ----------- FIGURE -----------
        plt.figure()

        if type_var.get() == "Continue":

            # Histogramme
            plt.subplot(1, 2, 1)
            plt.hist(wait, bins=20)
            plt.title("Histogramme")
            plt.xlabel("Temps")
            plt.ylabel("Fréquence")
            plt.grid()

            # Courbe cumulative
            plt.subplot(1, 2, 2)
            sorted_data = np.sort(wait)
            cumulative = np.arange(1, len(sorted_data)+1) / len(sorted_data)

            plt.plot(sorted_data, cumulative)
            plt.title("Courbe cumulative")
            plt.xlabel("Temps")
            plt.ylabel("Probabilité cumulée")
            plt.grid()

        else:
            values, freq = np.unique(counts, return_counts=True)

            # Diagramme en bâtons
            plt.subplot(1, 2, 1)
            plt.bar(values, freq)
            plt.title("Diagramme en bâtons")
            plt.xlabel("Nombre de requêtes")
            plt.ylabel("Fréquence")
            plt.grid()

            # Courbe cumulative
            plt.subplot(1, 2, 2)
            cumulative = np.cumsum(freq) / np.sum(freq)

            plt.plot(values, cumulative, marker='o')
            plt.title("Courbe cumulative")
            plt.xlabel("Valeurs")
            plt.ylabel("Probabilité cumulée")
            plt.grid()

        plt.tight_layout()
        plt.show()

    except ValueError:
        result_var.set("Entrées invalides (vérifie les nombres)")
    except Exception as e:
        result_var.set(f"Erreur : {e}")
    avg = np.mean(wait)
    var = np.var(wait)
    std = np.std(wait)

    result_var.set(
        f"Moyenne: {avg:.3f} | Variance: {var:.3f} | Écart-type: {std:.3f}"
    )