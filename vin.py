import sys


lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
           "n","o","p","q","r","s","t","u","v","w","x","y","z"]


valeurs = {}
for i in range(len(lettres)):
    valeurs[lettres[i]] = i


cle = ["o","u","i"]


def encrypt(texte, cle):
    resultat = ""
    for i in range(len(texte)):
        lettre = texte[i]
        if lettre in valeurs:
            valeur_texte = valeurs[lettre]
            valeur_cle = valeurs[cle[i % len(cle)]]
            valeur_chiffree = valeur_texte + valeur_cle
            if valeur_chiffree > 25:
                valeur_chiffree -= 26
            lettre_chiffree = lettres[valeur_chiffree]

            
            print(f"Lettre: {lettre} (val={valeur_texte}) + Clé: {cle[i % len(cle)]} (val={valeur_cle}) => {lettre_chiffree} (val={valeur_chiffree})")

            resultat += lettre_chiffree
        else:
            resultat += lettre
    return resultat


def decrypt(texte_chiffre, cle):
    resultat = ""
    for i in range(len(texte_chiffre)):
        lettre = texte_chiffre[i]
        if lettre in valeurs:
            valeur_chiffree = valeurs[lettre]
            valeur_cle = valeurs[cle[i % len(cle)]]
            valeur_origine = valeur_chiffree - valeur_cle
            if valeur_origine < 0:
                valeur_origine += 26
            lettre_origine = lettres[valeur_origine]

            print(f"Lettre chiffrée: {lettre} (val={valeur_chiffree}) - Clé: {cle[i % len(cle)]} (val={valeur_cle}) => {lettre_origine} (val={valeur_origine})")

            resultat += lettre_origine
        else:
            resultat += lettre
    return resultat


if len(sys.argv) > 1:
    action = sys.argv[1]  # 'encrypt' ou 'decrypt'
    texte = sys.argv[2]   # texte

    if action == "encrypt":
        print("\n--- Chiffrement ---\n")
        texte_chiffre = encrypt(texte, cle)
        print("\nTexte chiffré :", texte_chiffre)
    elif action == "decrypt":
        print("\n--- Déchiffrement ---\n")
        texte_dechiffre = decrypt(texte, cle)
        print("\nTexte déchiffré :", texte_dechiffre)
    else:
        print("tape python script.py ta fonction + le texte")
else:
    print("tape python script.py ta fonction + le texte")
