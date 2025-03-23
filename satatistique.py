import statistics

def saisir_donnees():
    while True:
        try:
            valeurs = list(map(float, input("Entrez les valeurs séparées par des espaces : ").split()))
            if len(valeurs) == 0:
                raise ValueError("Vous devez entrer au moins une valeur.")
            return valeurs
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

def calculer_tendance_centrale(valeurs):
    moyenne = statistics.mean(valeurs)
    mediane = statistics.median(valeurs)
    try:
        mode = statistics.mode(valeurs)
    except statistics.StatisticsError:
        mode = "Aucun mode unique"
    
    return moyenne, mediane, mode

def calculer_dispersion(valeurs):
    etendue = max(valeurs) - min(valeurs)
    variance = statistics.variance(valeurs) if len(valeurs) > 1 else 0
    ecart_type = statistics.stdev(valeurs) if len(valeurs) > 1 else 0
    
    return etendue, variance, ecart_type

def afficher_resultats(moyenne, mediane, mode, etendue, variance, ecart_type):
    print("\nRésultats des mesures statistiques :")
    print(f"Moyenne : {moyenne:.2f}")
    print(f"Médiane : {mediane:.2f}")
    print(f"Mode : {mode}")
    print(f"Étendue : {etendue:.2f}")
    print(f"Variance : {variance:.2f}")
    print(f"Écart-type : {ecart_type:.2f}")

def main():
    valeurs = saisir_donnees()
    moyenne, mediane, mode = calculer_tendance_centrale(valeurs)
    etendue, variance, ecart_type = calculer_dispersion(valeurs)
    afficher_resultats(moyenne, mediane, mode, etendue, variance, ecart_type)

if __name__ == "__main__":
    main()