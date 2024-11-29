
import random
def number_guessing_game():
    # 1. Introduction and Instructions
    print("Bienvenue dans le jeu de devinettes !")
    print("Je vais choisir un nombre entre 1 et 100, et vous aurez 10 tentatives pour le deviner.")

    # 2. Generating a Random Number
    secret_number = random.randint(1, 100)

    # 3. Number of Attempts
    attempts = 10

    # 4. Player's Guess Loop
    for attempt in range(1, attempts + 1):
        try:
            # 5. Getting and Validating Input
            guess = int(input(f"Tentative {attempt}/{attempts} : Entrez un nombre entre 1 et 100 : "))
            if guess < 1 or guess > 100:
                print("Veuillez entrer un nombre valide entre 1 et 100.")
                continue  # Revenir au début de la boucle
            
            # 6. Comparing the Guess
            if guess < secret_number:
                print("Trop bas !")
            elif guess > secret_number:
                print("Trop haut !")
            else:
                print(f"Félicitations ! Vous avez deviné le bon nombre : {secret_number} en {attempt} tentative(s).")
                break  # Sortie de la boucle car le joueur a gagné
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    # 7. If the Player Fails
    else:
        print(f"Dommage ! Vous avez utilisé vos {attempts} tentatives. Le nombre secret était {secret_number}.")

# 8. Starting the Game
if  __name__ == "__main__":
    number_guessing_game()