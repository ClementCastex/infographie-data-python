import pandas as pd
import matplotlib.pyplot as plt

# Définition de la palette de couleurs
COLORS = {
    'primary': '#3498db',    # Bleu principal
    'secondary': '#e67e22',  # Orange complémentaire
    'accent': '#2ecc71'      # Vert d'accent
}

# Fonction générique pour charger et nettoyer un fichier CSV
def load_and_clean_csv(filepath, sep=',', numeric_columns=None):
    """
    Charge un fichier CSV en appliquant un nettoyage basique des noms de colonnes
    et des valeurs textuelles. Utilise le moteur 'python' et ignore les lignes
    mal formées grâce à on_bad_lines='skip'.

    :param filepath: Chemin vers le fichier CSV
    :param sep: Séparateur utilisé dans le CSV (par défaut la virgule)
    :param numeric_columns: Liste des colonnes à convertir en numérique
    :return: DataFrame nettoyé
    """
    try:
        # Lecture en ignorant les lignes problématiques
        df = pd.read_csv(filepath, sep=sep, engine='python', on_bad_lines='skip')
    except Exception as e:
        print(f"Erreur lors du chargement du fichier CSV : {e}")
        raise

    # Suppression des espaces superflus autour des noms de colonnes
    df.columns = df.columns.str.strip()

    # Nettoyage des colonnes de type texte
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()                           # Suppression des espaces extérieurs
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)    # Conversion de multiples espaces en un seul

    # Conversion des colonnes numériques si nécessaire
    if numeric_columns:
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        # Suppression des lignes où la conversion a échoué
        df = df.dropna(subset=numeric_columns)
    
    return df

# Chargement des données
donnees = load_and_clean_csv("/var/www/html/temp-python/donnees_cleaned.csv", sep=',', numeric_columns=['duration_seconds'])
intentions = load_and_clean_csv("/var/www/html/temp-python/Intentions_par_session.csv", sep=',')

# Configuration du style global pour les graphiques Matplotlib
plt.style.use('default')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 12

# 1. Pages les plus visitées
top_pages = donnees['page_visited'].value_counts().head(10)
plt.figure(figsize=(12, 6))
top_pages.plot(kind='bar', color=COLORS['primary'])
plt.title('Analyse des Pages les Plus Consultées : Top 10 des Destinations Clés', pad=20)
plt.xlabel('Pages du Site')
plt.ylabel('Nombre Total de Visites')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("top_pages.png", dpi=300, bbox_inches='tight')
plt.close()

# 2. Actions par rapport en minutes
# Conversion de la durée de l'action (en secondes) en minutes
donnees['minute'] = donnees['duration_seconds'] / 60
action_minutes = donnees.groupby('action')['minute'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
action_minutes.plot(kind='bar', color=COLORS['secondary'])
plt.title("Analyse du Temps d'Engagement : Durée Totale par Type d'Action", pad=20)
plt.xlabel("Types d'Actions Utilisateur")
plt.ylabel("Temps Total d'Engagement (minutes)")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("action_minutes.png", dpi=300, bbox_inches='tight')
plt.close()

# 3. Répartition des utilisateurs par ville
city_counts = donnees['location'].value_counts().head(10)
plt.figure(figsize=(12, 6))
city_counts.plot(kind='bar', color=COLORS['accent'])
plt.title("Distribution Géographique : Top 10 des Villes d'Origine des Utilisateurs", pad=20)
plt.xlabel('Villes')
plt.ylabel("Nombre d'Utilisateurs Uniques")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("cities.png", dpi=300, bbox_inches='tight')
plt.close()

# 4. Répartition par appareil
# Filtrage des lignes avec les valeurs attendues pour 'device'
filtered_devices = donnees[donnees['device'].str.lower().isin(['mobile', 'desktop', 'tablet'])]
# Comptage du nombre d'occurrences pour chaque type d'appareil
device_counts = filtered_devices['device'].value_counts()

plt.figure(figsize=(10, 10))
plt.pie(device_counts, labels=device_counts.index, autopct='%1.1f%%',
        colors=[COLORS['primary'], COLORS['secondary'], COLORS['accent']],
        startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title("Analyse des Supports : Répartition des Accès par Type d'Appareil", pad=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig("devices.png", dpi=300, bbox_inches='tight')
plt.close()

# 5. Produits les plus achetés
product_counts = donnees['product_id'].value_counts().head(10)
plt.figure(figsize=(12, 6))
product_counts.plot(kind='bar', color=COLORS['primary'])
plt.title("Analyse des Ventes : Top 10 des Produits les Plus Demandés", pad=20)
plt.xlabel('Identifiants des Produits')
plt.ylabel("Volume Total des Achats")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("products.png", dpi=300, bbox_inches='tight')
plt.close()

# 6. Analyse des intentions
intent_counts = intentions['intent'].value_counts()
plt.figure(figsize=(10, 10))
plt.pie(intent_counts, labels=intent_counts.index, autopct='%1.1f%%',
        colors=[COLORS['primary'], COLORS['secondary'], COLORS['accent']],
        startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title("Analyse des Intentions : Répartition des Types de Visites", pad=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig("intentions.png", dpi=300, bbox_inches='tight')
plt.close()

# 7. Sessions par jour
donnees['date'] = pd.to_datetime(donnees['timestamp']).dt.date
sessions_par_jour = donnees.groupby('date')['session_id'].nunique()
plt.figure(figsize=(12, 6))
sessions_par_jour.plot(kind='line', marker='o', color=COLORS['primary'], linewidth=2)
plt.title("Analyse Temporelle : Évolution du Trafic Journalier", pad=20)
plt.xlabel('Dates')
plt.ylabel("Nombre de Sessions Uniques")
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("sessions_par_jour.png", dpi=300, bbox_inches='tight')
plt.close()

print("Tous les graphiques ont été enregistrés.")
