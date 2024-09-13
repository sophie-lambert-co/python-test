# import random
# from random import randint


# print("Entrez une valeur")
# compteur = int(input())
# for i in range(compteur):
#     print(i)

# print("Entrez une valeur")
# compteur = int(input())
# for i in range(11):   
#     print(i * compteur)


# for i in range(1,21):
#     print(i)

#     if (i % 3 == 0 )and (i % 5 == 0):
#         print("FizzBuzz")

#     elif i % 3 == 0:
#         print("Fizz")

#     elif i % 5 == 0:
#         print("Buzz")


# print(random.randint(1, 100))


# try:
#     for i in range(5):
#         print("entrez une valeur")
#         int(input())
#         continue
# except:
#     print('Erreur sauvage')


# banane = { "one": 1, "two": 5 }

# banane["five"] = 18

# print(banane["five"])
# print(banane.get("five"))


# from flask import Flask, request

# app = Flask(__name__)

# data = [
# 	{ "id": 1, "nom": "Pickles", "prenom": "Angelica", "ville": "Cesson-Sévigné" },
# 	{ "id": 2, "nom": "Pickles", "prenom": "Tommy", "ville": "Saint-Grégoire" },
# 	{ "id": 3, "nom": "Finster", "prenom": "Chuckie", "ville": "Betton" },
# 	{ "id": 4, "nom": "DeVille", "prenom": "Phil", "ville": "Chantepie" },
# 	{ "id": 5, "nom": "DeVille", "prenom": "Lil", "ville": "Pacé" },
# 	{ "id": 6, "nom": "Carmichael", "prenom": "Susie", "ville": "Vezin-le-Coquet" }
# ]

# @app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

# @app.route('/users/<int:user_id>')
# def users(user_id):
#     for row in data:
#         if row["id"]==user_id:
#             return row
#     return "Not Found"


# @app.route('/users')
# def fetch_users():
    
#     query_params = request.args.to_dict()
#     print(query_params)

#     results = []
#     if len(request.args) == 0: return data
#     for row in data:
#         Permet de caster id  de data en string
#         row['id'] = str(row['id'])
#         La flèche <= permet de vérifier que le dictionnaire de paramètre est contenu dans notre ligne
#         La "flèche" que tu mentionnes est en fait un opérateur de comparaison d'ensembles en Python, 
#         et il s'agit de l'opérateur <=. Cet opérateur est utilisé pour vérifier si un ensemble est un sous-ensemble d'un autre ensemble.
#         if query_params.items() <= row.items():
#             results.append(row)
#     return results



# @app.route('/chat')
# def chat():
#     query_params = request.args.to_dict()
#     print(query_params)
    
#     Si aucun paramètre n'est passé, renvoyer toutes les données
#     if not query_params:
#         return str(data)

#     results = []
#     for row in data:
#         match = True
#         for key, value in query_params.items():
#             if key not in row or str(row[key]) != value:
#                 match = False
#                 break
#         if match:
#             results.append(row)
    
#     if results:
#         return str(results)
#     else:
#         return "Aucun résultat trouvé", 404
    


# @app.route('/profil/<user>')
# def profil(user):
#     return f"<p>Profile de {user}</p>"

# @app.route('/search')
# def recherche():
#     q = request.args.get('q', default="")
#     return f"On recherche {q}"