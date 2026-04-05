import numpy as np

# Simulation des modèles M/M/1
def simulate_mm1(lam, mu, n):
    try:
        if lam <= 0 or mu <= 0 or n <= 0:
            raise ValueError("Paramètres invalides")

        arrivals = np.cumsum(np.random.exponential(1/lam, n))
        services = np.random.exponential(1/mu, n)

        start, finish, wait = np.zeros(n), np.zeros(n), np.zeros(n)

        for i in range(n):
            start[i] = arrivals[i] if i == 0 else max(arrivals[i], finish[i-1])
            wait[i] = start[i] - arrivals[i]
            finish[i] = start[i] + services[i]

        return wait

    except Exception as e:
        print(f"Erreur dans simulate_mm1 : {e}")
        return np.array([])


# Simulation des modèles M/G/1
def simulate_mg1(lam, mu, n):
    try:
        if lam <= 0 or mu <= 0 or n <= 0:
            raise ValueError("Paramètres invalides")

        arrivals = np.cumsum(np.random.exponential(1/lam, n))
        
        # Service plus variable pour bien distinguer M/G/1
        services = np.random.uniform(0, 4/mu, n)

        start, finish, wait = np.zeros(n), np.zeros(n), np.zeros(n)

        for i in range(n):
            start[i] = arrivals[i] if i == 0 else max(arrivals[i], finish[i-1])
            wait[i] = start[i] - arrivals[i]
            finish[i] = start[i] + services[i]

        return wait

    except Exception as e:
        print(f"Erreur dans simulate_mg1 : {e}")
        return np.array([])