# Simulation des files d’attente (M/M/1 et M/G/1)

## Contexte

Dans les systèmes informatiques modernes (réseaux, serveurs, cloud), la gestion du trafic est un enjeu majeur. Les files d’attente permettent de modéliser l’arrivée et le traitement des requêtes afin d’évaluer les performances du système.

Ce projet s’inscrit dans ce cadre en proposant une étude basée sur les probabilités et statistiques.


## Objectifs

- Modéliser un système de file d’attente à l’aide des modèles **M/M/1** et **M/G/1**
- Étudier les comportements **stables, saturés et instables**
- Comparer les résultats **théoriques et simulés**
- Analyser l’impact de la **variabilité des temps de service**
- Intégrer une approche **discrète (loi de Poisson)** et **continue**


## Fonctionnalités

Simulation des modèles :
- M/M/1 (service exponentiel)
- M/G/1 (service variable)

Analyse complète :
- Temps d’attente
- Histogrammes
- Courbes cumulatives
- Comparaison des modèles

Étude avancée :
- Convergence des simulations
- Analyse de la stabilité ($\rho$)
- Calcul des indicateurs statistiques (moyenne, variance, écart-type)

Interface graphique :
- Saisie des paramètres
- Choix du modèle
- Visualisation des résultats


## Méthodologie

Le projet repose sur :

- Modélisation mathématique des files d’attente
- Simulation Monte Carlo avec Python
- Analyse statistique des résultats
- Comparaison entre théorie et simulation


## Exemples de scénarios étudiés

| Cas | Paramètres | Description |
|-----|----------|------------|
| Stable | λ = 4, μ = 10 | Système fluide |
| Variable | λ = 4, μ = 10 (M/G/1) | Impact de la variabilité |
| Saturation | λ = 9.5, μ = 10 | Forte congestion |
| Instable | λ = 12, μ = 10 | Effondrement du système |
| Discret | λ = 9 | Arrivées (Poisson) |

---

## 📂 Structure du projet
projet/
└── README.md # A lire absolument
│── 📂 __pycache__
├── dashboard.py
├── logic.py # Logique de simulation
├── login.py # connexion et authentification
├── main.py # Lancement de l'application
│── network.png #cimage de l'interface d'accueil
├── simulation.py # Modèles M/M/1 et M/G/1
│── Rapport_de_Proba_Stats.pdf
├── ui.py # Interface graphique



## Lancer le projet

### Installer les dépendances
```bash
pip install numpy matplotlib

python main.py

---

## Accès à l'application

Une interface de connexion est mise en place pour accéder à la simulation.

### Identifiants par défaut :

- **Nom d'utilisateur** : `admin`
- **Mot de passe** : `1234`

Ces identifiants permettent d’accéder à l’interface principale de simulation.
