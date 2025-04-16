import pandas as pd
import matplotlib.pyplot as plt

# Création du DataFrame à partir des données fournies
data = {
    'User': [
        'U001', 'U002', 'U003', 'U004', 'U005', 'U006', 'U007', 'U008',
        'U009', 'U010', 'U011', 'U012', 'U014', 'U015', 'U016', 'U017',
        'U018', 'U019', 'U020', 'U022', 'U023', 'U024', 'U025', 'U026',
        'U027', 'U028', 'U029', 'U030'
    ],
    'Intention': [
        'Commercial', 'Transactionnel', 'Commercial', 'Transactionnel', 'Transactionnel', 'Transactionnel', 'Transactionnel', 'Transactionnel',
        'Transactionnel', 'Commercial', 'Transactionnel', 'Transactionnel', 'Transactionnel', 'Transactionnel', 'Transactionnel', 'Transactionnel',
        'Transactionnel', 'Information', 'Information', 'Transactionnel', 'Transactionnel', 'Transactionnel', 'Transactionnel', 'Transactionnel',
        'Information', 'Commercial', 'Transactionnel', 'Transactionnel'
    ]
}

df_intention = pd.DataFrame(data)

# Calcul du nombre d'utilisateurs par intention
intent_counts = df_intention['Intention'].value_counts()

# Création du graphique en barres
plt.figure(figsize=(6, 4))
intent_counts.plot(kind='bar', color='purple')
plt.xlabel("Intention")
plt.ylabel("Nombre d'utilisateurs")
plt.title("Distribution des intentions des utilisateurs")
plt.xticks(rotation=45)
plt.tight_layout()

# Sauvegarder le graphique en fichier image (optionnel)
plt.savefig("distribution_intentions.png")
plt.show()