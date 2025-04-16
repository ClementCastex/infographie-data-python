# Infographie – Analyse de la Campagne Publicitaire : Thé Noir Darjeeling Bio (Mars–Avril 2025)

## Contexte du Projet

Ce projet a été réalisé dans le cadre de l'exercice **Évaluation Data A2 2024-2025**. L'objectif était de produire individuellement un traitement visuel des données de navigation issues d'un client fictif.  
Le client est une entreprise française spécialisée dans la vente de thé bio, qui a su se constituer une clientèle dans de nombreux pays francophones. Entre le **7 mars 2025** et le **6 avril 2025**, une campagne Facebook Ads a été déployée pour promouvoir le thé noir Darjeeling bio, lequel était également en promotion durant cette période.

## Description de l'Infographie

L'infographie présente plusieurs visualisations générées en Python, permettant d'analyser :

- **Les pages les plus consultées** : Top 10 des destinations clés sur le site.
- **Les actions et le temps d'engagement** : Durée totale d'utilisation par type d'action.
- **La répartition géographique** : Top 10 des villes d'origine des utilisateurs.
- **La répartition par type d'appareil** : Analyse des supports (Mobile, Desktop, Tablet).
- **Les produits les plus achetés** : Top 10 des produits les plus demandés.
- **L'analyse des intentions** : Répartition des visites entre intents transactionnelles et commerciales.
- **L'évolution du trafic** : Nombre de sessions uniques par jour, indiquant la dynamique du trafic.

## Sources de Données

Les graphiques sont générés à partir de fichiers CSV.  
- `donnees_test.csv` : Contient les données de navigation brutes.  
- `donnees_cleaned.csv` : Fichier issu du nettoyage des données (suppression des espaces superflus, correction des lignes mal formées, conversion en type numérique, etc.).  
- `Intentions_par_session.csv` : Concerne les intentions associées aux sessions de navigation.

## Guide d'Utilisation

### Prérequis

- **Python 3.x**  
- **pandas** et **matplotlib**

Pour installer les dépendances nécessaires :

```bash
pip install pandas matplotlib
```
### Génération des Graphiques
Le script principal infographie_graphiques.py se charge de :

- **Charger et nettoyer les données depuis les fichiers CSV.**

- **Générer les différents graphiques (bar charts, pie charts, line charts) illustrant les indicateurs d'analyse.**

- **Sauvegarder ces graphiques sous forme d'images PNG dans le répertoire courant.**

Pour exécuter le script, lancez depuis le terminal :

```bash
python infographie_graphiques.py
```

## Publication de l’Infographie
Une fois les graphiques générés, ils peuvent être intégrés dans une page HTML pour présenter l'infographie complète. Cette page peut inclure :

- **Un titre et un sous-titre décrivant le projet et son contexte.**

- **Pour chaque graphique, une description détaillée expliquant son intérêt et les conclusions à en tirer.**

- **Un onglet « Sources » affichant les données brutes (via un tableau avec défilement, par exemple).**

## Remarques Complémentaires
Ce projet a été réalisé dans le cadre d'une mission pour Normandie Web School.

- **Tout le traitement des données et la génération des visualisations ont été réalisés en Python.**

- **L'approche de nettoyage automatique (gestion des espaces superflus, des lignes mal formées, etc.) permet d'assurer la qualité et la cohérence des analyses.**
