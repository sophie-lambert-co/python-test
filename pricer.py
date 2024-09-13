# import random
# from random import randint

# max_tentatives = 5
# tentatives = 0

# nombre_aleatoire = random.randint(0, 100)
# print(nombre_aleatoire)

# while tentatives < max_tentatives:
#     try:
#         print("Entrez une valeur")
#         nombre_test = int(input())
        
#         if nombre_test >= 100:
#             print("veuillez entrer un nombre entre 0 et 100")
#             continue

#         if nombre_test == nombre_aleatoire:
#             print("Bravo")
#             break
#         elif nombre_test > nombre_aleatoire:
#             print("Trop grand")
#         elif nombre_test < nombre_aleatoire:
#             print("Trop petit")

#         Incrémente le compteur de tentatives après chaque essai
#         tentatives += 1

#         if tentatives >= max_tentatives:
#             print("Perdu. Le nombre était " + str(nombre_aleatoire))


#     except ValueError:
#         Si une ValueError se produit (par exemple si l'utilisateur entre autre chose qu'un nombre), afficher un message d'erreur
#         print("Ce n'est pas un nombre valide. Veuillez essayer encore.")
#         continue  # Passe à la prochaine itération de la boucle while

       

# ###


# from random import randint

# price = randint(1, 10)
# res = -1
# print(type(res))
# while price != res:
#     print("Insérez un prix")
#     try:
#         res = int(input())
#         if res > 11 or res < -1:
#             raise Exception('Not interval')
#         if res == price:
#             print("You won !")
#         elif res < price:
#             print("Supérieur")
#         elif res > price:
#             print("Inférieur")
#     except ValueError:
#         print("Insert a numbers")
#     except Exception as e:
#         print(e)

        