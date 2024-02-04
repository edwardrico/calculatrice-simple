def calculatrice():
    print("Bonjour, veuillez choisir une option parmi les options suivantes !")

    print(" Options : ")
    print()
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Division")
    print("4 - Multiplication")
    print("5 - Terminé")
    print()
    try:
        option = int(input("Choisissez votre option (1/2/3/4/5) : "))
        if option < 1 or option > 5:
            print("Erreur, les options sont numérotées de 1 à 5.")
        elif option == 5:
            print("Merci au revoir!")


        else:
            tipe_operation(option)

    except ValueError:
        print("Erreur vous doit choisir une nombre pour les option ")


def tipe_operation(option):
    operations = {
        1: "Addition",
        2: "Soustraction",
        3: "Division",
        4: "Multiplication",
    }

    if option in operations:
        print(f"Parfait vous avais choisir la option : {operations[option]}")
        resultat = choix(option)
        print(f"Le resultat est : {resultat}")
    else:
        print(f"Option :{option} non reconnue")


def choix(option):
    try:
        choix1 = float(input("Rentre votre promiere nombre : "))
        choix2 = float(input("Rentre votre dexieme nombre : "))
        return calcule(option, choix1, choix2)
    except ValueError:
        print("Erreur vous doit rentre une nombre ")


def calcule(option, choix1, choix2):
    if option == 1:
        return choix1 + choix2
    elif option == 2:
        return choix1 - choix2
    elif option == 3:
        return choix1 / choix2
    elif option == 4:
        return choix1 * choix2
    else:
        print(f"option : {option} ne reconneu. ")


calculatrice()
