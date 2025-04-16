import pandas as pd

def clean_csv(
    input_path: str,
    output_path: str,
    sep: str = ',',
    unify_case: bool = False
):
    """
    Nettoie un fichier CSV en supprimant les espaces parasites et,
    optionnellement, en unifiant la casse des valeurs textuelles.
    Enregistre ensuite le résultat dans un nouveau fichier CSV.

    :param input_path: Chemin du fichier CSV d'origine.
    :param output_path: Chemin du fichier CSV nettoyé.
    :param sep: Séparateur utilisé dans le CSV (par défaut ',').
    :param unify_case: Si True, convertit toutes les chaînes en minuscules.
    """
    # Chargement du CSV
    df = pd.read_csv(input_path, sep=sep)
    
    # Nettoyage des noms de colonnes (suppression des espaces superflus)
    df.columns = df.columns.str.strip()
    
    # Nettoyage des colonnes de type texte
    for col in df.select_dtypes(include=['object']):
        # Suppression des espaces avant/après
        df[col] = df[col].str.strip()
        # Remplacement des espaces multiples par un seul
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
        # Optionnel : transformer en minuscules pour homogénéiser (si nécessaire)
        if unify_case:
            df[col] = df[col].str.lower()
    
    # Enregistrement du fichier nettoyé
    df.to_csv(output_path, index=False)
    print(f"Fichier nettoyé enregistré sous : {output_path}")

if __name__ == "__main__":
    # Chemin du fichier CSV d'origine et du fichier de sortie
    input_csv = "donnees_cleaned.csv"         # fichier d'origine (avec éventuels espaces parasites)
    output_csv = "donnees.csv"  # fichier propre à générer

    # Appel de la fonction de nettoyage
    # Passez unify_case=True si vous souhaitez uniformiser toutes les valeurs en minuscules
    clean_csv(
        input_path=input_csv,
        output_path=output_csv,
        sep=',',
        unify_case=False  # Modifier à True si besoin d'unifier la casse
    )